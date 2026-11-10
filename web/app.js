'use strict';
const $=(s,root=document)=>root.querySelector(s), $$=(s,root=document)=>[...root.querySelectorAll(s)];
const chapters=$$('.chapter'), panelNames=['structure','screens','originals','ready'];
let current=0, toastTimer, searchTimer;
const escapeHTML=s=>String(s||'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
function toast(message){const el=$('#toast');el.textContent=message;el.style.display='block';clearTimeout(toastTimer);toastTimer=setTimeout(()=>el.style.display='none',2200)}
function closeMenu(){document.body.classList.remove('menu-open');$('#menu').setAttribute('aria-expanded','false')}
function updateProgress(){const max=document.documentElement.scrollHeight-innerHeight;$('#reading-progress').style.width=(max>0?Math.min(100,scrollY/max*100):0)+'%'}
function applyRoute(scroll=true){
  const [id,pane]=location.hash.slice(1).split('/');
  current=Math.max(0,chapters.findIndex(c=>c.id===id));const chapter=chapters[current];
  const panel=panelNames.includes(pane)?pane:'structure';
  chapters.forEach((el,i)=>el.classList.toggle('active',i===current));
  $$('.stage-tabs button',chapter).forEach(b=>{const active=b.dataset.panel===panel;b.setAttribute('aria-selected',String(active));b.tabIndex=active?0:-1});
  $$('.stage-panel',chapter).forEach(el=>el.hidden=el.dataset.panel!==panel);
  $$('aside nav a').forEach(a=>{const active=a.hash==='#'+chapter.id;a.classList.toggle('selected',active);if(active)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
  const title=chapter.id==='overview'?'先看全周期':$('h2',chapter).textContent;
  $('#breadcrumb').textContent=title;$('#position').textContent=String(current+1).padStart(2,'0')+' / '+chapters.length;
  document.title=(chapter.id==='overview'?'':title+' · ')+'Rebuttal 全周期写作手册';
  closeMenu();
  if(scroll){if(document.body.classList.contains('continuous'))chapter.scrollIntoView({block:'start'});else window.scrollTo({top:0,behavior:'instant'})}
  updateProgress();
}
function go(id,panel='structure'){const hash='#'+id+(id==='overview'||id==='appendix'?'':'/'+panel);if(location.hash!==hash)history.pushState(null,'',hash);applyRoute()}
window.addEventListener('hashchange',()=>applyRoute());
window.addEventListener('popstate',()=>applyRoute());
document.addEventListener('click',e=>{const a=e.target.closest('a[href^="#"]');if(!a)return;const [id,pane]=a.hash.slice(1).split('/');if(chapters.some(c=>c.id===id)){e.preventDefault();go(id,pane||'structure')}});
$$('.stage-tabs').forEach((tabs,index)=>{
  const chapter=tabs.closest('.chapter');
  $$('button',tabs).forEach(b=>{const pane=$('.stage-panel[data-panel="'+b.dataset.panel+'"]',chapter);const key=chapter.id+'-'+b.dataset.panel;b.id='tab-'+key;b.setAttribute('aria-controls','panel-'+key);pane.id='panel-'+key;pane.setAttribute('role','tabpanel');pane.setAttribute('aria-labelledby',b.id);b.onclick=()=>go(chapter.id,b.dataset.panel)});
  tabs.addEventListener('keydown',e=>{if(!['ArrowLeft','ArrowRight','Home','End'].includes(e.key))return;e.preventDefault();e.stopPropagation();const buttons=$$('button',tabs);let i=buttons.indexOf(document.activeElement);if(e.key==='Home')i=0;else if(e.key==='End')i=buttons.length-1;else i=(i+(e.key==='ArrowRight'?1:-1)+buttons.length)%buttons.length;buttons[i].focus();buttons[i].click()});
});
async function copyText(text,element,label){try{await navigator.clipboard.writeText(text);toast(label)}catch{const range=document.createRange();range.selectNodeContents(element);const selection=getSelection();selection.removeAllRanges();selection.addRange(range);toast('已选中文字，请按 Ctrl / Cmd + C')}}
$$('.copy').forEach(b=>b.onclick=()=>{const el=$('pre',b.parentElement);if(el)copyText(el.textContent,el,'模板已复制')});
$$('.copy-original').forEach(b=>b.onclick=()=>{const el=$('.original-quote',b.closest('.pattern-card'));copyText(el.textContent,el,'原句已复制')});
$$('.expression-filter').forEach(input=>{const empty=document.createElement('p');empty.className='empty-filter';empty.hidden=true;empty.textContent='没有匹配的原句，试试更短的关键词。';input.parentElement.append(empty);input.addEventListener('input',()=>{let found=0;$$('.pattern-card',input.parentElement).forEach(card=>{card.hidden=!card.textContent.toLowerCase().includes(input.value.trim().toLowerCase());if(!card.hidden)found++});empty.hidden=found>0})});
$$('.bottomnav').forEach(nav=>{const share=document.createElement('button');share.className='share-stage';share.textContent='分享此处';share.onclick=()=>copyText(location.href,share,'当前阶段链接已复制');$('.next',nav).before(share)});
$$('.previous').forEach(b=>b.onclick=()=>go(chapters[(current-1+chapters.length)%chapters.length].id));
$$('.next').forEach(b=>b.onclick=()=>go(chapters[(current+1)%chapters.length].id));
$('#viewmode').onclick=e=>{const enabled=document.body.classList.toggle('continuous');e.target.textContent=enabled?'按阶段阅读':'连续阅读';applyRoute(false)};
$('#menu').onclick=()=>{const open=document.body.classList.toggle('menu-open');$('#menu').setAttribute('aria-expanded',String(open))};
document.addEventListener('click',e=>{if(document.body.classList.contains('menu-open')&&!e.target.closest('aside,#menu'))closeMenu()});
$$('.shot').forEach(b=>b.onclick=()=>{$('#zoomimage').src=$('img',b).src;$('#zoomimage').alt=$('img',b).alt;$('#zoom').showModal()});
$('#closezoom').onclick=()=>$('#zoom').close();
$$('dialog').forEach(dialog=>dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close()}}));

// Search the verified content already in the document; no network or account needed.
const searchIndex=[],seen=new Set();
chapters.forEach(chapter=>{
  const stage=chapter.id==='overview'?'全周期':$('h2',chapter).textContent;
  const add=(node,title,text,panel,type)=>{const key=title+'|'+text;if(seen.has(key))return;seen.add(key);searchIndex.push({node,title,text,stage,id:chapter.id,panel,type,key:(title+' '+text+' '+stage).toLowerCase()})};
  $$('.pattern-card',chapter).forEach(card=>add(card,$('h4',card).textContent,$('.original-quote',card).textContent,'originals','原句'));
  $$('.stage-panel[data-panel="ready"] .template',chapter).forEach(el=>{const title=el.previousElementSibling?.classList.contains('tpl-label')?el.previousElementSibling.textContent:stage;add(el,title,$('pre',el).textContent,'ready','模板')});
  $$('.stage-panel[data-panel="structure"] h3,.stage-panel[data-panel="structure"] p',chapter).forEach(el=>{if(el.textContent.length>12)add(el,el.tagName==='H3'?el.textContent:stage,el.textContent,'structure','说明')});
});
function openSearch(){if(!$('#find-dialog').open)$('#find-dialog').showModal();$('#global-search').focus()}
$('#open-search').onclick=openSearch;$('#close-search').onclick=()=>$('#find-dialog').close();
function renderSearch(){
  const q=$('#global-search').value.trim().toLowerCase(),out=$('#find-results');out.replaceChildren();
  if(!q){$('#find-count').textContent='输入关键词，搜索所有阶段的原句、模板与说明。';return}
  const tokens=q.split(/\s+/),matches=searchIndex.filter(item=>tokens.every(t=>item.key.includes(t)));
  $('#find-count').textContent=matches.length?('找到 '+matches.length+' 条'+(matches.length>35?'，显示前 35 条':'')):'没有匹配内容，试试 happy、novelty 或更短的关键词。';
  matches.slice(0,35).forEach(item=>{const button=document.createElement('button');button.className='find-result';const context=item.text.replace(/\s+/g,' ');const at=Math.max(0,context.toLowerCase().indexOf(tokens[0])-40);button.innerHTML='<small>'+escapeHTML(item.stage+' / '+item.type)+'</small><strong>'+escapeHTML(item.title)+'</strong><span>'+escapeHTML((at?'…':'')+context.slice(at,at+180))+'</span>';button.onclick=()=>{$('#find-dialog').close();const chapter=document.getElementById(item.id);const filter=$('.expression-filter',chapter);if(filter){filter.value='';filter.dispatchEvent(new Event('input'))}go(item.id,item.panel);requestAnimationFrame(()=>requestAnimationFrame(()=>{item.node.scrollIntoView({block:'center'});item.node.setAttribute('tabindex','-1');item.node.focus({preventScroll:true})}))};out.append(button)});
}
$('#global-search').addEventListener('input',()=>{clearTimeout(searchTimer);searchTimer=setTimeout(renderSearch,80)});
document.addEventListener('keydown',e=>{if((e.ctrlKey||e.metaKey)&&e.key.toLowerCase()==='k'){e.preventDefault();openSearch();return}if(e.key==='Escape')closeMenu();if(e.defaultPrevented||e.ctrlKey||e.metaKey||e.altKey||/INPUT|TEXTAREA|SELECT/.test(e.target.tagName)||e.target.isContentEditable||$$('dialog').some(d=>d.open)||getSelection().toString())return;if(e.key==='ArrowRight'){e.preventDefault();go(chapters[(current+1)%chapters.length].id)}if(e.key==='ArrowLeft'){e.preventDefault();go(chapters[(current-1+chapters.length)%chapters.length].id)}});

const all=JSON.parse($('#archive-data').textContent);
function renderArchive(){const q=$('#search').value.trim().toLowerCase(),paper=$('#paper').value;const matches=all.filter(n=>(!paper||n.paper===paper)&&(!q||[n.title,n.meta,n.body,n.paper].join(' ').toLowerCase().includes(q)));$('#results').textContent=matches.length+' / '+all.length+' 条帖子';$('#notes').innerHTML=matches.map(n=>'<details><summary>'+escapeHTML(n.paper+' / '+n.title)+'</summary><p class="meta">'+escapeHTML(n.meta)+'</p><a target="_blank" rel="noreferrer" href="https://openreview.net/forum?id='+encodeURIComponent(n.forum)+'&noteId='+encodeURIComponent(n.id)+'">在线原帖</a><div class="raw">'+escapeHTML(n.body)+'</div></details>').join('')}
$('#search').oninput=renderArchive;$('#paper').onchange=renderArchive;renderArchive();
window.addEventListener('scroll',updateProgress,{passive:true});window.addEventListener('resize',updateProgress);
applyRoute(false);
