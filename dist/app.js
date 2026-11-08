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

// The homepage benefit statement reveals once in reading order.
const taglineReveal=document.querySelector('[data-tagline-reveal]');
if(taglineReveal){
 const words=[...taglineReveal.querySelectorAll('[data-reveal-word]')];
 const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 const reveal=()=>words.forEach((word,index)=>{
  if(reduced){word.classList.add('is-visible');return;}
  window.setTimeout(()=>word.classList.add('is-visible'),index*55);
 });
 if(reduced||!('IntersectionObserver' in window)){reveal();}
 else{
  const taglineObserver=new IntersectionObserver(entries=>{
   if(entries.some(entry=>entry.isIntersecting)){taglineObserver.disconnect();reveal();}
  },{threshold:.45});
  taglineObserver.observe(taglineReveal);
 }
}

// The delivery path remains complete in the document, then gains a restrained
// sequential reveal when motion is welcome.
const processFlow=document.querySelector('[data-process-flow]');
if(processFlow){
 const steps=[...processFlow.children];
 const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 if(reduced||!('IntersectionObserver' in window)){
  processFlow.classList.add('is-progressing');
  steps.forEach(step=>step.classList.add('is-active'));
 }else{
  processFlow.classList.add('process-animated');
  const flowObserver=new IntersectionObserver(entries=>{
   if(entries.some(entry=>entry.isIntersecting)){
    flowObserver.disconnect();
    processFlow.classList.add('is-progressing');
    steps.forEach((step,index)=>window.setTimeout(()=>step.classList.add('is-active'),index*110));
   }
  },{threshold:.2});
  flowObserver.observe(processFlow);
 }
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
if(calContainer&&!window.matchMedia('(max-width: 700px)').matches){
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
 function setMenu(open,returnFocus=false){header.classList.toggle('nav-open',open);document.documentElement.classList.toggle('menu-open',open);menuButton.setAttribute('aria-expanded',String(open));menuButton.setAttribute('aria-label',open?'Close navigation':'Open navigation');if(returnFocus)menuButton.focus();}
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

// Article planning aid: local-only state, no schedule or delivery claim.
const launchPlanner=document.querySelector('[data-launch-planner]');
if(launchPlanner){
 const inputs=[...launchPlanner.querySelectorAll('input[type="checkbox"]')];
 const stages=[...launchPlanner.querySelectorAll('[data-launch-stage]')];
 const result=launchPlanner.querySelector('[data-launch-result]');
 const nextActions=['Confirm the audience, offer and primary visitor action.','Collect and approve the business facts and permitted media.','Name one person who can consolidate and approve feedback.','Confirm the domain, form destination and other service access.','Run the agreed mobile, keyboard, link and enquiry checks.'];
 function renderLaunchPlan(){
  const ready=inputs.filter(input=>input.checked).length;
  stages.forEach((stage,index)=>stage.classList.toggle('is-ready',inputs[index].checked));
  const nextIndex=inputs.findIndex(input=>!input.checked);
  result.textContent=nextIndex===-1?'5 of 5 planning inputs marked ready. The project still needs an agreed scope and provider estimate before a launch date is approved.':ready+' of 5 planning inputs marked ready. Next planning action: '+nextActions[nextIndex];
 }
 launchPlanner.addEventListener('change',renderLaunchPlan);
 launchPlanner.addEventListener('reset',()=>requestAnimationFrame(renderLaunchPlan));
 renderLaunchPlan();
}

// Article engagement aid: a local-only scope prompt, never a diagnosis or saved result.
const seoEngagementPlanner=document.querySelector('[data-seo-engagement-planner]');
if(seoEngagementPlanner){
 const result=seoEngagementPlanner.querySelector('[data-seo-engagement-result]');
 const checked=name=>seoEngagementPlanner.elements[name]?.checked;
 function renderSeoEngagement(){
  let message='Start by recording the observed problem, affected business journey and evidence already available.';
  if(checked('unknown'))message='Likely next conversation: a bounded technical SEO audit to diagnose the cause, affected URLs, priorities and implementation effort.';
  if(checked('findings')||checked('implementation'))message='Likely next conversation: an implementation project with approved findings, named owners, release controls and acceptance checks.';
  if(checked('verification'))message='Likely next conversation: independent verification of the live changes, with later search observations recorded separately.';
  if(checked('recurring'))message='Likely next conversation: ongoing consultancy with a defined release cadence, decision log, response boundary and exit condition.';
  if(checked('unknown')&&(checked('implementation')||checked('recurring')))message='Split the work: diagnose the uncertain issues first, then scope implementation or recurring review only for accepted findings.';
  result.textContent=message;
 }
 seoEngagementPlanner.addEventListener('change',renderSeoEngagement);
 seoEngagementPlanner.addEventListener('reset',()=>requestAnimationFrame(renderSeoEngagement));
 renderSeoEngagement();
}

// Article page-boundary aid: local-only guidance, never a ranking or conversion estimate.
const pageBoundaryPlanner=document.querySelector('[data-page-boundary-planner]');
if(pageBoundaryPlanner){
 const inputs=[...pageBoundaryPlanner.querySelectorAll('input[type="checkbox"]')];
 const result=pageBoundaryPlanner.querySelector('[data-page-boundary-result]');
 function renderPageBoundary(){
  const count=inputs.filter(input=>input.checked).length;
  let message='No signals marked. Begin by writing the visitor question and the decision this content should support.';
  if(count===1)message='1 of 5 signals marked. This topic may work as a section on a broader page unless stronger distinct evidence emerges.';
  if(count===2)message='2 of 5 signals marked. Compare the topic with nearby pages before choosing a URL; avoid repeating the same decision.';
  if(count>=3&&count<5)message=count+' of 5 signals marked. This is a credible separate-page candidate. Confirm useful content, overlap and maintenance ownership.';
  if(count===5)message='5 of 5 signals marked. The topic has a strong page case, but a human still needs to review accuracy, overlap and the complete site map.';
  result.textContent=message;
 }
 pageBoundaryPlanner.addEventListener('change',renderPageBoundary);
 pageBoundaryPlanner.addEventListener('reset',()=>requestAnimationFrame(renderPageBoundary));
 renderPageBoundary();
}

// Article link-opportunity aid: local-only review, never an outreach or ranking promise.
const linkOpportunityPlanner=document.querySelector('[data-link-opportunity-planner]');
if(linkOpportunityPlanner){
 const inputs=[...linkOpportunityPlanner.querySelectorAll('input[type="checkbox"]')];
 const result=linkOpportunityPlanner.querySelector('[data-link-opportunity-result]');
 function renderLinkOpportunity(){
  const count=inputs.filter(input=>input.checked).length;
  let message='No checks marked. Start with the audience and the reader problem.';
  if(count===1)message='1 of 5 checks supported. Do not contact the publisher yet; clarify the reader benefit and evidence.';
  if(count===2)message='2 of 5 checks supported. Review the destination and relationship before deciding on outreach.';
  if(count===3)message='3 of 5 checks supported. This may deserve human review, but unresolved permission or commercial details still matter.';
  if(count===4)message='4 of 5 checks supported. Resolve the remaining check before sending a specific, respectful note.';
  if(count===5)message='5 of 5 checks supported. Credible outreach candidate; the publisher still controls whether and how it references the page.';
  result.textContent=message;
 }
 linkOpportunityPlanner.addEventListener('change',renderLinkOpportunity);
 linkOpportunityPlanner.addEventListener('reset',()=>requestAnimationFrame(renderLinkOpportunity));
 renderLinkOpportunity();
}

// Article cadence aid: local-only guidance, never a publishing or ranking estimate.
const cadencePlanner=document.querySelector('[data-cadence-planner]');
if(cadencePlanner){
 const inputs=[...cadencePlanner.querySelectorAll('input[type="checkbox"]')];
 const result=cadencePlanner.querySelector('[data-cadence-result]');
 function renderCadence(){
  const count=inputs.filter(input=>input.checked).length;
  let message='No checks marked. Record the buyer question before assigning a publication date.';
  if(count===1)message='1 of 5 checks supported. Keep researching; this topic has not earned a new page yet.';
  if(count===2)message='2 of 5 checks supported. Check whether an existing page should be updated or consolidated.';
  if(count===3)message='3 of 5 checks supported. A useful idea may exist, but resolve overlap, evidence and ownership before publishing.';
  if(count===4)message='4 of 5 checks supported. Resolve the remaining editorial requirement, then review the complete draft.';
  if(count===5)message='5 of 5 checks supported. The topic is ready for human editorial review; publication and search outcomes remain separate decisions.';
  result.textContent=message;
 }
 cadencePlanner.addEventListener('change',renderCadence);
 cadencePlanner.addEventListener('reset',()=>requestAnimationFrame(renderCadence));
 renderCadence();
}

// Article access aid: local-only review, never a permission grant or provider-role decision.
const accessPlanner=document.querySelector('[data-access-planner]');
if(accessPlanner){
 const inputs=[...accessPlanner.querySelectorAll('input[type="checkbox"]')];
 const result=accessPlanner.querySelector('[data-access-result]');
 function renderAccessReview(){
  const count=inputs.filter(input=>input.checked).length;
  let message='No checks marked. Begin with the exact system and task.';
  if(count===1)message='1 of 5 checks supported. Do not grant access yet; identify the recipient, role and review boundary.';
  if(count===2)message='2 of 5 checks supported. The request still needs a task-specific role and accountable owner.';
  if(count===3)message='3 of 5 checks supported. Resolve the remaining identity, expiry or information-handling gaps first.';
  if(count===4)message='4 of 5 checks supported. Complete the final control before the owner reviews the invitation.';
  if(count===5)message='5 of 5 checks supported. Ready for owner review in the live provider; verify the role after granting and revoke it when the task ends.';
  result.textContent=message;
 }
 accessPlanner.addEventListener('change',renderAccessReview);
 accessPlanner.addEventListener('reset',()=>requestAnimationFrame(renderAccessReview));
 renderAccessReview();
}

// Article enquiry-route aid: local-only guidance, never a conversion estimate.
const enquiryRoutePlanner=document.querySelector('[data-enquiry-route-planner]');
if(enquiryRoutePlanner){
 const options=[...enquiryRoutePlanner.querySelectorAll('input[name="route"]')];
 const result=enquiryRoutePlanner.querySelector('[data-enquiry-route-result]');
 const messages={
  quick:'Recommended route: WhatsApp. Use a pre-filled topic, publish monitored hours and keep phone or email visible as a fallback.',
  brief:'Recommended route: a short contact form. Collect only the context needed for the next decision, then test validation, real delivery and confirmation.',
  call:'Recommended route: calendar booking. State the call purpose and duration, respect the visitor\'s timezone and test confirmation, rescheduling and cancellation.',
  fallback:'Recommended route: direct email or phone. Keep it easy to find and assign a real response owner instead of forcing every visitor through one interface.'
 };
 function renderEnquiryRoute(){
  const selected=options.find(option=>option.checked);
  result.textContent=selected?messages[selected.value]:'Choose a visitor task to review its route.';
 }
 enquiryRoutePlanner.addEventListener('change',renderEnquiryRoute);
 enquiryRoutePlanner.addEventListener('reset',()=>requestAnimationFrame(renderEnquiryRoute));
 renderEnquiryRoute();
}

// Article campaign-readiness aid: local-only review, never a performance forecast.
const campaignReadinessPlanner=document.querySelector('[data-campaign-readiness-planner]');
if(campaignReadinessPlanner){
 const inputs=[...campaignReadinessPlanner.querySelectorAll('input[type="checkbox"]')];
 const result=campaignReadinessPlanner.querySelector('[data-campaign-readiness-result]');
 function renderCampaignReadiness(){
  const count=inputs.filter(input=>input.checked).length;
  let message='No checks marked. Begin with the exact offer and visitor decision.';
  if(count===1)message='1 of 5 checks supported. Resolve the offer and destination foundations before planning wider traffic.';
  if(count===2)message='2 of 5 checks supported. The destination still has blocking evidence gaps; assign them to an owner.';
  if(count===3)message='3 of 5 checks supported. Complete the action, mobile and measurement checks before a launch decision.';
  if(count===4)message='4 of 5 checks supported. Resolve and retest the remaining dependency before the team approves the destination.';
  if(count===5)message='5 of 5 checks supported. Ready for a human launch review; campaign performance and qualified enquiries remain unproven.';
  result.textContent=message;
 }
 campaignReadinessPlanner.addEventListener('change',renderCampaignReadiness);
 campaignReadinessPlanner.addEventListener('reset',()=>requestAnimationFrame(renderCampaignReadiness));
 renderCampaignReadiness();
}
