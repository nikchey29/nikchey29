/* No dependencies. Every movement has a reduced-motion escape hatch. */
(()=>{'use strict';
 const root=document.documentElement;root.classList.add('js');const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
 let saved;try{saved=localStorage.getItem('cv-theme')}catch(_){}if(saved==='light'||saved==='dark')root.dataset.theme=saved;
 const theme=document.querySelector('[data-theme-toggle]');
 const syncTheme=()=>{if(theme){const light=root.dataset.theme==='light';theme.textContent=light?'☾':'☼';theme.setAttribute('aria-label',light?'Switch to dark theme':'Switch to light theme')}};
 syncTheme();theme?.addEventListener('click',()=>{root.dataset.theme=root.dataset.theme==='light'?'dark':'light';try{localStorage.setItem('cv-theme',root.dataset.theme)}catch(_){}syncTheme()});
 const menu=document.querySelector('[data-menu-toggle]'),links=document.querySelector('.links');
 const closeMenu=()=>{links?.classList.remove('open');menu?.setAttribute('aria-expanded','false');if(menu)menu.textContent='☰'};
 menu?.addEventListener('click',()=>{const open=links?.classList.toggle('open')??false;menu.setAttribute('aria-expanded',String(open));menu.textContent=open?'✕':'☰'});
 links?.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));document.addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu()});
 const progress=document.querySelector('.progress');let pendingScroll=false;
 function updateScroll(){const h=document.documentElement;const ratio=h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight);if(progress)progress.style.width=`${Math.max(0,Math.min(100,ratio*100))}%`;pendingScroll=false}
 window.addEventListener('scroll',()=>{if(!pendingScroll){requestAnimationFrame(updateScroll);pendingScroll=true}},{passive:true});updateScroll();
 const reveals=document.querySelectorAll('.reveal');if('IntersectionObserver'in window&&!reduced){const io=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.07,rootMargin:'0px 0px -20px 0px'});reveals.forEach((el,i)=>{el.style.transitionDelay=`${Math.min(i%3,2)*100}ms`;io.observe(el)})}else reveals.forEach(el=>el.classList.add('in'));
 const filterButtons=document.querySelectorAll('[data-filter]'),projects=document.querySelectorAll('[data-project-type]');filterButtons.forEach(btn=>btn.addEventListener('click',()=>{const filter=btn.dataset.filter;filterButtons.forEach(b=>b.setAttribute('aria-pressed',String(b===btn)));projects.forEach(p=>{p.hidden=filter!=='all'&&!p.dataset.projectType.split(' ').includes(filter);if(!p.hidden)p.classList.add('in')})}));
 const year=document.querySelector('[data-year]');if(year)year.textContent=String(new Date().getFullYear());
 if(reduced||!window.matchMedia('(hover:hover) and (pointer:fine)').matches)return;
 const light=document.querySelector('.pointer-light');let pointerFrame=false;let px=-999,py=-999;
 window.addEventListener('pointermove',e=>{px=e.clientX;py=e.clientY;if(!pointerFrame&&light){pointerFrame=true;requestAnimationFrame(()=>{root.style.setProperty('--cursor-x',px+'px');root.style.setProperty('--cursor-y',py+'px');pointerFrame=false})}},{passive:true});
 const scope=document.querySelector('[data-parallax-scope]');if(scope){const layers=scope.querySelectorAll('[data-parallax]');scope.addEventListener('pointermove',e=>{const r=scope.getBoundingClientRect(),nx=(e.clientX-r.left)/r.width-.5,ny=(e.clientY-r.top)/r.height-.5;layers.forEach(layer=>{const amt=Number(layer.dataset.parallax)||0;layer.style.translate=`${(nx*amt).toFixed(1)}px ${(ny*amt).toFixed(1)}px`})});scope.addEventListener('pointerleave',()=>layers.forEach(layer=>layer.style.translate='0px 0px'))}
 document.querySelectorAll('.case-card').forEach(card=>{card.addEventListener('pointermove',e=>{const r=card.getBoundingClientRect();card.style.setProperty('--card-x',(e.clientX-r.left)+'px');card.style.setProperty('--card-y',(e.clientY-r.top)+'px')})});
 document.querySelectorAll('.magnetic').forEach(el=>{el.addEventListener('pointermove',e=>{const r=el.getBoundingClientRect();const dx=e.clientX-r.left-r.width/2,dy=e.clientY-r.top-r.height/2;el.style.translate=`${(dx*.11).toFixed(1)}px ${(dy*.12).toFixed(1)}px`});el.addEventListener('pointerleave',()=>{el.style.translate='0px 0px'})});
})();
