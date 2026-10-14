const bag=[];
const status=document.querySelector('[data-cart-status]');
function renderBag(){
 const container=document.querySelector('[data-bag-items]');if(!container)return;
 container.replaceChildren();const count=bag.reduce((n,item)=>n+item.quantity,0);
 if(!bag.length){const p=document.createElement('p');p.textContent='Your bag is empty. Browse homeware above and add an item to try it.';container.append(p);}
 bag.forEach((item,i)=>{
  const row=document.createElement('div');row.className='basketitem';const text=document.createElement('span');text.textContent=item.name;const controls=document.createElement('div');controls.className='quantitycontrols';
  function button(label,value,fn){const b=document.createElement('button');b.type='button';b.textContent=value;b.setAttribute('aria-label',label);b.addEventListener('click',fn);return b;}
  const quantity=document.createElement('span');quantity.textContent=item.quantity;quantity.setAttribute('aria-label','Quantity '+item.quantity);
  const minus=button('Decrease '+item.name,'−',()=>{if(item.quantity>1)item.quantity--;else bag.splice(i,1);renderBag();status.textContent=item.name+' quantity updated. '+document.querySelector('[data-count]').textContent+' items in your demo bag.';const next=[...container.querySelectorAll('button')].find(b=>b.getAttribute('aria-label')==='Decrease '+item.name);(next||document.querySelector('[data-reset]')).focus();});
  const plus=button('Increase '+item.name,'+',()=>{item.quantity++;renderBag();status.textContent=item.name+' quantity '+item.quantity+'.';[...container.querySelectorAll('button')].find(b=>b.getAttribute('aria-label')==='Increase '+item.name)?.focus();});
  const remove=button('Remove '+item.name,'Remove',()=>{bag.splice(i,1);renderBag();status.textContent=item.name+' removed from the demo bag.';document.querySelector('[data-reset]').focus();});controls.append(minus,quantity,plus,remove);row.append(text,controls);container.append(row);
 });
 document.querySelector('[data-count]').textContent=count;document.querySelector('[data-total]').textContent='Demo items: '+count;document.querySelectorAll('[data-add]').forEach(b=>{const item=bag.find(i=>i.name===b.dataset.add);b.textContent=item?'Add another ('+item.quantity+' in bag) +':'Add to demo bag +';});
}
document.querySelectorAll('[data-add]').forEach(btn=>{btn.setAttribute('aria-label','Add '+btn.dataset.add+' to demo bag');btn.addEventListener('click',()=>{const item=bag.find(i=>i.name===btn.dataset.add);if(item)item.quantity++;else bag.push({name:btn.dataset.add,quantity:1});renderBag();status.textContent=btn.dataset.add+' added to the demo bag. No order created.';});});
document.querySelector('[data-reset]')?.addEventListener('click',()=>{bag.length=0;renderBag();status.textContent='Demo bag emptied.';document.querySelectorAll('[data-add]').forEach(b=>b.textContent='Add to demo bag +');});
document.querySelectorAll('[data-filter]').forEach(btn=>btn.addEventListener('click',()=>{let count=0;document.querySelectorAll('[data-filter]').forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));document.querySelectorAll('[data-category]').forEach(card=>{card.hidden=btn.dataset.filter!=='All'&&card.dataset.category!==btn.dataset.filter;if(!card.hidden)count++;});document.querySelector('[data-filter-status]').textContent='Showing '+count+' '+(count===1?'item':'items')+(btn.dataset.filter==='All'?'':' in '+btn.dataset.filter);}));
document.querySelector('#demo-consultation')?.addEventListener('submit',e=>{e.preventDefault();const f=e.currentTarget;if(!f.reportValidity())return;const d=new FormData(f);const s=f.querySelector('[data-consultation-status]');s.textContent='Your demo brief: '+d.get('type')+' in '+d.get('location')+(d.get('area')?' · '+d.get('area')+' sq. ft.':'')+' — Goal: '+d.get('goal')+' — Local preview only. No enquiry or appointment sent.';s.focus();});
