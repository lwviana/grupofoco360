import re, sys, os, base64, hashlib, subprocess
from PIL import Image, ImageDraw
src, out = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
J = os.path.join
def w(n, c):
    os.makedirs(os.path.dirname(J(out, n)) or out, exist_ok=True)
    open(J(out, n), 'wb').write(c if isinstance(c, bytes) else c.encode('utf-8'))
def sub(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b)

# 1. midias embutidas viram arquivos
ext = {'font/woff2': ('fonts', 'woff2'), 'image/jpeg': ('img', 'jpg'), 'image/png': ('img', 'png'), 'video/mp4': ('video', 'mp4')}
seen = {}; cnt = {}
def rep(m):
    h = hashlib.sha1(m.group(2).encode()).hexdigest()
    if h not in seen:
        d, e = ext[m.group(1)]; cnt[d] = cnt.get(d, 0) + 1
        seen[h] = 'assets/%s/%s-%d.%s' % (d, d, cnt[d], e)
        w(seen[h], base64.b64decode(m.group(2)))
    return seen[h]
s = re.sub(r'data:([a-z]+/[a-z0-9+.-]+);base64,([A-Za-z0-9+/=]+)', rep, s)
m = re.search(r'<script type="application/octet-stream" id="doc-ensaio">([^<]+)</script>\n?', s)
PDF = 'assets/docs/NERO-relatorio-de-ensaio-1160363-203.pdf'
w(PDF, base64.b64decode(m.group(1).strip()))
s = s.replace(m.group(0), '')
sub('<button class="bt bt-doc" type="button" data-doc="ensaio" data-nome="NERO-relatorio-de-ensaio-1160363-203.pdf">Relatório de ensaio nº 1 160 363-203 (PDF)</button>',
    '<a class="bt bt-doc" href="' + PDF + '" target="_blank" rel="noopener">Relatório de ensaio nº 1 160 363-203 (PDF)</a>')
a = s.index('/* documentos embutidos'); b = s.index('/* passos de uso */')
s = s[:a] + s[b:]

# 2. cabecalho: SEO, favicon, previa de compartilhamento
U = 'https://grupofoco360.com.br/'
T = re.search(r'<title>([^<]+)</title>', s).group(1)
D = re.search(r'<meta name="description" content="([^"]+)">', s).group(1)
sub('<style>', '''<link rel="canonical" href="%(U)s">
<meta name="theme-color" content="#1C2833">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon.png" sizes="64x64" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="FOCO360">
<meta property="og:url" content="%(U)s">
<meta property="og:title" content="%(T)s">
<meta property="og:description" content="%(D)s">
<meta property="og:image" content="%(U)sassets/img/og-foco360.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="assets/fonts/fonts-5.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/fonts-1.woff2" as="font" type="font/woff2" crossorigin>
<script type="application/ld+json">{"@context":"https://schema.org","@type":"ProfessionalService","name":"FOCO360","url":"%(U)s","logo":"%(U)sassets/img/img-6.png","image":"%(U)sassets/img/og-foco360.jpg","description":"%(D)s","telephone":"+55 47 99911-0090","email":"rosinei360@gmail.com","address":{"@type":"PostalAddress","addressLocality":"Joinville","addressRegion":"SC","addressCountry":"BR"},"areaServed":"BR"}</script>
<style>''' % {'U': U, 'T': T, 'D': D})

# 3. videos: versao leve primeiro, alta qualidade em data-hq
for i in range(1, 7):
    hq = 'assets/video/video-%d.mp4' % i; lo = hq.replace('.mp4', '-low.mp4')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', J(out, hq), '-an', '-vf', 'scale=270:484' if i == 6 else 'scale=426:240',
                    '-c:v', 'libx264', '-preset', 'veryslow', '-crf', '36', '-profile:v', 'main', '-pix_fmt', 'yuv420p', '-g', '48',
                    '-movflags', '+faststart', J(out, lo)], check=True)
    sub('<source src="%s" type="video/mp4">' % hq, '<source src="%s" type="video/mp4">' % lo)
n = 0
def addhq(m):
    global n
    n += 1
    return '<video muted loop playsinline preload="%s" poster="%s" data-hq="assets/video/video-%d.mp4">' % ('auto' if n == 1 else 'none', m.group(1), n)
s = re.sub(r'<video muted loop playsinline preload="auto" poster="([^"]+)">', addhq, s)
assert n == 5
sub('<video id="nvid" muted loop playsinline preload="metadata"', '<video id="nvid" data-hq="assets/video/video-6.mp4" muted loop playsinline preload="none"')
sub("/* fundo em vídeo que muda conforme a seção */", """/* qualidade progressiva: o vídeo leve toca de imediato; o de alta qualidade baixa inteiro em segundo plano
   e só entra quando está completo, no mesmo ponto da reprodução. Em conexão lenta ou economia de dados, fica no leve. */
var NC=navigator.connection||navigator.mozConnection||navigator.webkitConnection;
var LENTO=!!(NC&&(NC.saveData||/(^|-)2g$/.test(NC.effectiveType||'')));
var filaHQ=Promise.resolve();
function melhora(v,pronto){
  if(!v||!v.dataset.hq||v._hq||LENTO||!window.fetch||!window.URL)return;
  v._hq=1;var hq=v.dataset.hq;
  filaHQ=filaHQ.then(function(){return fetch(hq).then(function(r){if(!r.ok)throw 0;return r.blob();}).then(function(b){return new Promise(function(ok){
    var n=document.createElement('video'),feito=false,u=URL.createObjectURL(b);
    function fim(){if(!feito){feito=true;ok();}}
    n.muted=true;n.loop=true;n.playsInline=true;n.setAttribute('muted','');n.setAttribute('playsinline','');n.preload='auto';
    n.poster=v.poster;n.className=v.className;if(v.id)n.id=v.id;
    if(v.getAttribute('aria-label'))n.setAttribute('aria-label',v.getAttribute('aria-label'));
    n._hq=1;
    function troca(){
      if(feito||!v.parentNode)return fim();
      var tocava=!v.paused;n.className=v.className;
      v.parentNode.replaceChild(n,v);v.pause();v.removeAttribute('src');
      if(tocava)n.play().catch(function(){});
      pronto(n);fim();
    }
    n.addEventListener('loadeddata',function(){
      var t=v.currentTime||0;
      if(t>.05&&n.duration&&isFinite(n.duration)){n.addEventListener('seeked',troca,{once:true});try{n.currentTime=t%n.duration;}catch(e){troca();}}
      else troca();
    },{once:true});
    n.addEventListener('error',function(){URL.revokeObjectURL(u);fim();},{once:true});
    setTimeout(fim,20000);
    n.src=u;n.load();
  });}).catch(function(){v._hq=0;});});
}
function quandoTocar(v,f){if(v.readyState>=3&&!v.paused)f();else v.addEventListener('playing',f,{once:true});}

/* fundo em vídeo que muda conforme a seção */""")
sub("if(j===i){v.classList.add('on');if(!fp)v.play().catch(function(){});}",
    "if(j===i){v.classList.add('on');if(!fp)v.play().catch(function(){});quandoTocar(v,function(){melhora(fv[j],function(n){fv[j]=n;if(j!==fat){n.classList.remove('on');n.pause();}});});}")
sub("frot();qual();", "frot();qual();\nwindow.addEventListener('load',function(){setTimeout(function(){fv.forEach(function(v){if(v.preload==='none'){v.preload='auto';v.load();}});},600);});")
a = s.index("var v=document.getElementById('nvid')"); b = s.index("/* passos de uso */")
s = s[:a] + """var v=document.getElementById('nvid'),vb=document.getElementById('vctl'),pausado=RM,vvis=false;
function rot(){vb.textContent=pausado?'Reproduzir vídeo':'Pausar vídeo';vb.setAttribute('aria-pressed',pausado);}
rot();
function ntoca(){if(vvis&&!pausado){v.play().catch(function(){});quandoTocar(v,function(){melhora(v,function(n){v=n;if(!vvis||pausado)n.pause();});});}else v.pause();}
vb.addEventListener('click',function(){pausado=!pausado;ntoca();rot();});
if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){vvis=e.isIntersecting;ntoca();});},{threshold:.2}).observe(v.parentNode);}else{vvis=true;ntoca();}

""" + s[b:]
assert 'base64' not in s and 'data-doc' not in s
w('index.html', s)

# 4. arquivos de apoio
w('CNAME', 'grupofoco360.com.br\n'); w('.nojekyll', '')
w('robots.txt', 'User-agent: *\nAllow: /\n\nSitemap: %ssitemap.xml\n' % U)
w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>%s</loc></url>\n</urlset>\n' % U)
w('favicon.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="8" fill="#1C2833"/><circle cx="32" cy="32" r="20" fill="none" stroke="#fff" stroke-opacity=".5" stroke-width="3"/><path d="M32 12a20 20 0 0 1 17.3 30" fill="none" stroke="#E3B04B" stroke-width="5" stroke-linecap="round"/><line x1="32" y1="32" x2="32" y2="16" stroke="#fff" stroke-width="3" stroke-linecap="round"/><circle cx="32" cy="32" r="4.5" fill="#E3B04B"/></svg>\n')
w('404.html', '<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Página não encontrada | FOCO360</title><body style="margin:0;min-height:100vh;display:grid;place-items:center;background:#1C2833;color:#fff;font-family:system-ui,sans-serif;text-align:center"><div><h1 style="font-size:48px;margin:0;color:#E3B04B">404</h1><p>Página não encontrada.</p><p><a href="/" style="color:#fff">Voltar para o início</a></p></div></body></html>\n')
logo = Image.open(J(out, 'assets/img/img-6.png')).convert('RGBA')
bg = Image.new('RGB', (1200, 630), '#1C2833')
l = logo.resize((820, round(logo.height * 820 / logo.width)), Image.LANCZOS)
bg.paste(l, (190, (630 - l.height) // 2), l)
ImageDraw.Draw(bg).rectangle([0, 618, 1200, 630], fill='#E3B04B')
bg.save(J(out, 'assets/img/og-foco360.jpg'), quality=88)
for name, sz in (('favicon.png', 64), ('apple-touch-icon.png', 180)):
    k = sz * 4 / 64; im = Image.new('RGB', (sz * 4, sz * 4), '#1C2833'); d = ImageDraw.Draw(im)
    d.ellipse([12 * k, 12 * k, 52 * k, 52 * k], outline='#8b949b', width=round(3 * k))
    d.arc([12 * k, 12 * k, 52 * k, 52 * k], -90, 30, fill='#E3B04B', width=round(5 * k))
    d.line([32 * k, 32 * k, 32 * k, 16 * k], fill='#fff', width=round(3 * k))
    d.ellipse([27.5 * k, 27.5 * k, 36.5 * k, 36.5 * k], fill='#E3B04B')
    im.resize((sz, sz), Image.LANCZOS).save(J(out, name))
print('ok', len(s))
