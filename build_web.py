"""Build GitHub Pages from the verified offline handbook without rewriting sources."""
from pathlib import Path
import re, base64, hashlib

ROOT = Path(__file__).parent
source = (ROOT / 'Rebuttal实战手册.html').read_text()
images = {hashlib.sha256(p.read_bytes()).hexdigest(): p.relative_to(ROOT).as_posix()
          for p in (ROOT / 'screenshots').glob('*.jpg')}
def external_image(m):
    data = base64.b64decode(m[1])
    path = images.get(hashlib.sha256(data).hexdigest())
    if not path:
        raise ValueError('An embedded source screenshot has no local file')
    return 'src="' + path + '"'
page = re.sub(r'src="data:image/jpeg;base64,([^"]+)"', external_image, source)
page = page.replace('<html lang="zh-CN">', '<html lang="zh-CN"><head>')
page = page.replace('<body>', '</head><body>')
page = page.replace('</style>', '</style><link rel="stylesheet" href="web/style.css">', 1)
page = page.replace('<title>Rebuttal 全周期写作手册 · 同阶段截图与共性模板</title>',
'''<title>Rebuttal 全周期写作手册</title>
<meta name="description" content="基于五篇顶会论文的真实讨论，按阶段整理原帖截图、英文原句、回复骨架和可复用模板。">
<meta name="theme-color" content="#5143a5">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">''')
page = re.sub(r'<aside><b>.*?</b><p>.*?</p>', '''<a class="skip" href="#content">跳到正文</a>
<aside id="sidebar"><a class="brand" href="#overview"><span class="brand-mark">R<span>.</span></span><span>Rebuttal<br><small>全周期写作手册</small></span></a><p class="sidebar-caption">从第一轮回复，到讨论结束</p>''', page, count=1, flags=re.S)
page = page.replace('<nav>', '<nav aria-label="手册目录">', 1)
page = page.replace('全周期</div>', '讨论进程</div>', 1)
page = page.replace('贯穿各阶段的写作工具</div>', '写作工具</div>', 1)
page = page.replace('<main><header>', '<main id="content" tabindex="-1"><header>', 1)
page = re.sub(r'<header>.*?</header>', '''<header class="topbar"><button id="menu" aria-expanded="false" aria-controls="sidebar">目录</button><span id="breadcrumb">先看全周期</span><div class="top-actions"><button id="open-search" aria-haspopup="dialog"><svg width="16" height="16" viewBox="0 0 20 20" fill="none" aria-hidden="true"><circle cx="8" cy="8" r="5.5" stroke="currentColor" stroke-width="1.7"/><path d="m12 12 5 5" stroke="currentColor" stroke-width="1.7"/></svg><span>搜索原句与模板</span><kbd>⌘ K</kbd></button><a href="https://github.com/junzhang-zj/rebuttal-handbook" target="_blank" rel="noreferrer">GitHub</a></div></header><div class="reading-progress" aria-hidden="true"><span id="reading-progress"></span></div>''', page, count=1, flags=re.S)
page = page.replace('<button id="open-search"', '<button id="open-search" aria-label="搜索原句与模板"', 1)
hero = '''<div class="intro-heading"><p class="byline">Jun Zhang · 五篇论文的真实讨论</p><h1>Rebuttal<br>全周期写作手册<span class="title-period">.</span></h1><p class="hero-description">从读懂 concern，到让 AC 看清贡献。<br>沿着讨论进程，找到此刻需要的写法。</p><div class="hero-actions"><a class="primary-link" href="#initial/structure">开始逐条回复 <span aria-hidden="true">↗</span></a><a href="#general/screens">先看真实案例</a></div><div class="paper-strip"><a href="https://openreview.net/forum?id=s7DkcgpRxL" target="_blank" rel="noreferrer">LoRAM</a><a href="https://openreview.net/forum?id=i5aHAkkhJH" target="_blank" rel="noreferrer">FloE</a><a href="https://openreview.net/forum?id=xyXsaQEmCu" target="_blank" rel="noreferrer">LVSpec</a><a href="https://openreview.net/forum?id=wvlizZdYc1" target="_blank" rel="noreferrer">LVLM Survey</a><a href="https://openreview.net/forum?id=jFuN2yI2D7" target="_blank" rel="noreferrer">HybridKV</a></div></div>
<div class="how-to-read"><h2>先选阶段，再选读法</h2><div class="reading-lanes"><div><span>骨架</span><p>什么时候发、谁能看，按什么顺序写。</p></div><div><span>截图</span><p>把同阶段的原帖放在一起，对照着看。</p></div><div><span>原句</span><p>找到原话、上下文，以及重复使用的范围。</p></div><div><span>模板</span><p>把真实事实填入槽位，完成这一轮回应。</p></div></div></div>'''
start = page.index('<section class="chapter" id="overview">')
end = page.index('</section>', start) + len('</section>')
overview = page[start:end]
overview = re.sub(r'<div class="chapter-title">.*?</div>', '', overview, count=1, flags=re.S)
overview = re.sub(r'<div class="overview-facts">.*?</div>', '', overview, flags=re.S)
overview = re.sub(r'<div class="route">.*?</div>', '', overview, flags=re.S)
overview = re.sub(r'<div class="bottomnav">.*?</div>', '', overview, flags=re.S)
overview = re.sub(r'^<section[^>]*>', '', overview).removesuffix('</section>')
journey = [('initial','逐条回复','正面回答，建立证据链'), ('general','General Response','汇总认可、贡献与更新'), ('followup','后续交流','跟进新问题与实验结果'), ('reminders','提醒与协调','在讨论窗口内争取反馈'), ('summary','讨论总结','让 AC 看清结果与分歧'), ('reports','评审问题反馈','用事实、证据与请求收束'), ('recommend','决定后回应','落实修订，准确表达推荐')]
rows = ''.join(f'<a href="#{sid}"><span class="journey-number">{i+1:02}</span><strong>{name}</strong><span class="journey-description">{desc}</span><span class="journey-arrow" aria-hidden="true">↗</span></a>' for i,(sid,name,desc) in enumerate(journey))
new = '<section class="chapter" id="overview">'+hero+'<div class="journey"><h2>现在进行到哪一步？</h2>'+rows+'</div><details class="full-timeline"><summary>展开完整时间线与可见性说明</summary>'+overview+'</details><p class="corpus-caption">基于 104 条可读作者帖，精选 69 条原句条目与 37 张原帖截图。原句、派生模板与作者主张分别标注，保留出处供核对。</p></section>'
page = page[:start]+new+page[end:]
page = page.replace('<section class="chapter" id="appendix"><h2>', '<section class="chapter" id="appendix"><h2>')
page = re.sub(r'<script>.*?</script>', '<script src="web/app.js" defer></script>', page, flags=re.S)
page = page.replace('所有图片已嵌入 HTML，可离线打开。', '在线版按需加载截图；离线阅读请下载独立 HTML。')
page = page.replace('<a href="共性阶段写作拆解.md">下载共性写作骨架 Markdown</a>', '<a href="https://github.com/junzhang-zj/rebuttal-handbook/archive/refs/heads/main.zip">下载离线手册与素材</a> · <a href="共性阶段写作拆解.md">查看写作骨架 Markdown</a>')
page = page.replace('</body>', '''<dialog id="find-dialog" aria-labelledby="find-title"><div class="find-heading"><h2 id="find-title">找到需要的写法</h2><button id="close-search" aria-label="关闭搜索">关闭 ×</button></div><label class="sr-only" for="global-search">搜索原句、模板或问题</label><input id="global-search" type="search" placeholder="试试 novelty、happy、催审、Summary…" autocomplete="off"><p id="find-count" role="status">输入关键词，搜索所有阶段的原句、模板与说明。</p><div id="find-results"></div></dialog></body>''')
(ROOT/'index.html').write_text(page)
(ROOT/'.nojekyll').write_text('')
print(f'Pages built: {len(page.encode()):,} bytes; source images externalized; all original chapters retained.')
