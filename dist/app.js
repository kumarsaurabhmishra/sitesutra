// Each tablist has its own keyboard navigation and panel ownership.
const heroFilm=document.querySelector('[data-sutra-film]');
document.querySelectorAll('[role="tablist"]').forEach(list=>{
 const tabs=[...list.querySelectorAll('[role="tab"]')];
 function select(tab){tabs.forEach(t=>{const on=t===tab;t.setAttribute('aria-selected',String(on));t.tabIndex=on?0:-1;document.getElementById(t.getAttribute('aria-controls')).hidden=!on;});}
 tabs.forEach((tab,i)=>{tab.addEventListener('click',()=>select(tab));tab.addEventListener('keydown',e=>{let n;if(e.key==='ArrowRight')n=(i+1)%tabs.length;if(e.key==='ArrowLeft')n=(i-1+tabs.length)%tabs.length;if(e.key==='Home')n=0;if(e.key==='End')n=tabs.length-1;if(n!==undefined){e.preventDefault();select(tabs[n]);tabs[n].focus();}});});
});
if(heroFilm&&!window.matchMedia('(prefers-reduced-motion: reduce)').matches){
 const setPlaying=playing=>heroFilm.classList.toggle('is-playing',playing&&!document.hidden);
 if('IntersectionObserver' in window){new IntersectionObserver(entries=>setPlaying(entries[0].isIntersecting),{threshold:.3}).observe(heroFilm);}else setPlaying(true);
 document.addEventListener('visibilitychange',()=>setPlaying(!document.hidden));
}
document.querySelectorAll('[data-device]').forEach(btn=>btn.addEventListener('click',()=>{document.querySelectorAll('[data-device]').forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));document.querySelector('[data-device-preview]').classList.toggle('mobile',btn.dataset.device==='mobile');}));
document.querySelectorAll('[data-compare]').forEach(btn=>btn.addEventListener('click',()=>{document.querySelectorAll('[data-compare]').forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));document.querySelectorAll('[data-comparison]').forEach(panel=>panel.hidden=panel.dataset.comparison!==btn.dataset.compare);}));
const form=document.getElementById('enquiry');
form?.addEventListener('submit',async e=>{
 e.preventDefault();if(!form.reportValidity())return;
 const status=document.getElementById('formstatus');const config=window.SITESUTRA_CONFIG||{};
 function announce(message,error=false){status.textContent=message;status.setAttribute('role',error?'alert':'status');status.focus();}
 if(!config.formEndpoint){
  const data=new FormData(form);const fields=[['name','Name'],['email','Email'],['business','Business or agency'],['website','Existing website'],['service','Service'],['goal','Project description'],['budget','Budget'],['timeline','Preferred timeline']];
  const body=fields.map(([key,label])=>label+': '+(data.get(key)||'Not specified')).join('\n\n');
  const draft='mailto:'+config.email+'?subject='+encodeURIComponent('SiteSutra project enquiry from '+data.get('name'))+'&body='+encodeURIComponent(body);
  announce('Your email app has been requested. Review and send the draft there. No enquiry has been received by this website. If it does not open, email '+config.email+' directly.');
  window.location.href=draft;return;
 }
 const button=form.querySelector('[type=submit]');button.disabled=true;form.setAttribute('aria-busy','true');status.textContent='Sending your project brief…';
 try{
  const controller=new AbortController();const timer=setTimeout(()=>controller.abort(),15000);
  let response;try{response=await fetch(config.formEndpoint,{method:'POST',body:new FormData(form),headers:{Accept:'application/json'},signal:controller.signal});}finally{clearTimeout(timer);}
  let result;try{result=await response.json();}catch{throw new Error('Unconfirmed provider response');}
  if(!response.ok||result.ok!==true)throw new Error('Submission not confirmed');
  announce('Your enquiry has been received. Thank you for sharing your project.');form.reset();
 }catch(error){announce('Your enquiry could not be sent. Please try again or contact me by email: '+config.email+' Your details remain in the form. Delivery was not confirmed.',true);}
 finally{button.disabled=false;form.removeAttribute('aria-busy');}
});
// Month browsing shows dates only; never invent live availability.
const dateGrid=document.getElementById('booking-dates');
if(dateGrid){
 const now=new Date();let month=new Date(now.getFullYear(),now.getMonth(),1);
 function renderMonth(){
  const label=new Intl.DateTimeFormat('en',{month:'long',year:'numeric'}).format(month);
  document.getElementById('booking-month').textContent=label;dateGrid.replaceChildren();
  const offset=(month.getDay()+6)%7;const count=new Date(month.getFullYear(),month.getMonth()+1,0).getDate();
  for(let i=0;i<offset;i++){const blank=document.createElement('span');blank.className='calblank';blank.setAttribute('aria-hidden','true');dateGrid.append(blank);}
  for(let d=1;d<=count;d++){const day=document.createElement('span');day.textContent=d;day.className='calday';day.setAttribute('aria-label',d+' '+label+' — booking unavailable');if(d===now.getDate()&&month.getMonth()===now.getMonth()&&month.getFullYear()===now.getFullYear()){day.classList.add('today');day.setAttribute('aria-current','date');}dateGrid.append(day);}
 }
 document.querySelectorAll('[data-month]').forEach(btn=>btn.addEventListener('click',()=>{month=new Date(month.getFullYear(),month.getMonth()+(btn.dataset.month==='next'?1:-1),1);renderMonth();}));renderMonth();
}
// Official Cal.com embed queue; no booking or success state is fabricated locally.
const calContainer=document.getElementById('cal-inline');
if(calContainer){
 function loadCalendar(){
 (function(C,A,L){const push=function(fn,args){fn.q.push(args);};const d=C.document;C.Cal=C.Cal||function(){const cal=C.Cal;const args=arguments;if(!cal.loaded){cal.ns={};cal.q=cal.q||[];const script=d.createElement('script');script.src=A;script.onerror=()=>{const note=document.getElementById('cal-fallback');note.textContent='The booking calendar could not load. Please use the Cal.com link below.';note.setAttribute('role','alert');const loading=calContainer.querySelector('.cal-loading');if(loading)loading.textContent='Calendar unavailable in this browser.';};d.head.appendChild(script);cal.loaded=true;}if(args[0]===L){const api=function(){push(api,arguments);};const namespace=args[1];api.q=api.q||[];if(typeof namespace==='string'){cal.ns[namespace]=cal.ns[namespace]||api;push(cal.ns[namespace],args);push(cal,['initNamespace',namespace]);}else push(cal,args);return;}push(cal,args);};})(window,'https://cal.com/embed/embed.js','init');
 window.Cal('init',{origin:'https://cal.com'});
 window.Cal('inline',{elementOrSelector:'#cal-inline',calLink:calContainer.dataset.calLink,config:{layout:'month_view',theme:'light'}});
 window.Cal('ui',{theme:'light',styles:{branding:{brandColor:'#244CFF'}},hideEventTypeDetails:false,layout:'month_view'});
 const observer=new MutationObserver(()=>{if(calContainer.querySelector('iframe')){calContainer.querySelector('iframe').title='Book a '+window.SITESUTRA_CONFIG.bookingDurationMinutes+'-minute discovery call with Kumar on Cal.com';calContainer.querySelector('.cal-loading')?.remove();observer.disconnect();}});observer.observe(calContainer,{childList:true,subtree:true});
 }
 if('IntersectionObserver' in window){
  const calendarVisibility=new IntersectionObserver(entries=>{
   if(entries.some(entry=>entry.isIntersecting)){calendarVisibility.disconnect();loadCalendar();}
  },{rootMargin:'200px'});
  calendarVisibility.observe(calContainer);
 }else{loadCalendar();}
}
// A standard disclosure navigation: regular links, keyboard focus and Escape.
const menuButton=document.querySelector('.menu-toggle');
if(menuButton){
 const header=menuButton.closest('header');const navigation=document.getElementById('main-navigation');header.classList.add('nav-ready');
 function setMenu(open,returnFocus=false){header.classList.toggle('nav-open',open);menuButton.setAttribute('aria-expanded',String(open));menuButton.setAttribute('aria-label',open?'Close navigation':'Open navigation');if(returnFocus)menuButton.focus();}
 menuButton.addEventListener('click',()=>setMenu(menuButton.getAttribute('aria-expanded')!=='true'));
 navigation.querySelectorAll('a').forEach(link=>{if(new URL(link.href).pathname===location.pathname&&!new URL(link.href).hash)link.setAttribute('aria-current','page');link.addEventListener('click',()=>{setMenu(false);const destination=new URL(link.href);if(destination.pathname===location.pathname&&destination.hash){const target=document.querySelector(destination.hash);if(target){target.setAttribute('tabindex','-1');target.focus({preventScroll:true});}}});});
 document.addEventListener('keydown',e=>{if(e.key==='Escape'&&header.classList.contains('nav-open'))setMenu(false,true);});
 document.addEventListener('pointerdown',e=>{if(!header.contains(e.target))setMenu(false);});
 header.addEventListener('focusout',()=>{setTimeout(()=>{if(!header.contains(document.activeElement))setMenu(false);},0);});
 window.matchMedia('(min-width: 1101px)').addEventListener('change',()=>setMenu(false));
}

// Buyer-guide demonstrations never save or publish content.
const editHeading=document.getElementById('demo-heading');
if(editHeading){const original=editHeading.value;function renderEdit(){document.getElementById('edited-heading').textContent=editHeading.value.trim()||'Your service heading';document.getElementById('edit-status').textContent='Local preview updated. Nothing is saved or published.';}editHeading.addEventListener('input',renderEdit);document.getElementById('reset-edit').addEventListener('click',()=>{editHeading.value=original;renderEdit();editHeading.focus();});}
const maintenance=document.getElementById('maintenance-demo');
if(maintenance){maintenance.addEventListener('change',()=>{const count=maintenance.querySelectorAll('input:checked').length;document.getElementById('maintenance-status').textContent=count+' of 4 review items marked.'+(count===4?' Demo checklist complete; actual release approval is still required.':'');});}
