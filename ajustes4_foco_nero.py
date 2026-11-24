# Foco total na NERO (pedido de 23/11/2026). Roda depois do ajustes3.
# - index.html passa a ser so a manta NERO, com foco em venda e apresentacao
# - as demais frentes da FOCO360 vao para solucoes.html
# - sai o que dizia que a FOCO360 faz treinamento e avaliacao
import sys, os, re
p = sys.argv[1]
raiz = os.path.dirname(p) or '.'
base = open(p, encoding='utf-8').read()
U = 'https://grupofoco360.com.br/'
WA = 'https://wa.me/5547999110090?text=Ol%C3%A1%2C%20quero%20uma%20proposta%20da%20manta%20antichamas%20NERO.'

def troca(s, a, b, n=1):
    assert s.count(a) == n, (s.count(a), a[:70])
    return s.replace(a, b)
def corta(s, ini, fim, incluir_fim=True):
    a = s.index(ini); b = s.index(fim, a) + (len(fim) if incluir_fim else 0)
    return s[:a] + s[b:], s[a:b]
def cabeca(s, titulo, desc, url):
    s = re.sub(r'<title>[^<]*</title>', '<title>' + titulo + '</title>', s, count=1)
    s = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + desc, s, count=1)
    s = re.sub(r'(<meta property="og:title" content=")[^"]*', lambda m: m.group(1) + titulo, s, count=1)
    s = re.sub(r'(<meta property="og:description" content=")[^"]*', lambda m: m.group(1) + desc, s, count=1)
    s = re.sub(r'(<meta property="og:url" content=")[^"]*', lambda m: m.group(1) + url, s, count=1)
    s = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + url, s, count=1)
    return s

# blocos do script principal, para cada pagina levar so o que usa
MARCAS = ['/* menu */', '/* hero: mira', '/* qualidade progressiva', '/* fundo em vídeo', '/* abas de serviços */',
          '/* roda 360 */', '/* contagem do 10% */', '/* vídeo NERO', '/* passos de uso */']
def sem_blocos(s, fora):
    a = s.index('(function(){\nvar RM='); b = s.index('})();', s.index(MARCAS[-1]))
    js = s[a:b]
    pos = [js.index(m) for m in MARCAS] + [len(js)]
    assert pos == sorted(pos)
    novo = js[:pos[0]] + ''.join(js[pos[i]:pos[i + 1]] for i in range(len(MARCAS)) if i not in fora)
    return s[:a] + novo + s[b:]

CSS = '''
/* foco NERO */
.sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.menu a.sol{border:1px solid rgba(255,255,255,.6);border-radius:3px;padding:9px 14px}
.menu a.sol:hover{background:rgba(255,255,255,.1)}
body.so-nero .nero-hero{min-height:94svh;display:flex;align-items:center}
body.so-nero .nero-hero .wrap{width:100%;padding-top:140px}
.nero-hero .mais{display:inline-block;margin-top:26px;color:#fff;font-weight:600;font-size:17px;text-underline-offset:4px}
.nx-mais{background:var(--aco);color:#fff;padding:72px 0}
.nx-mais .wrap{display:flex;gap:40px;align-items:center;justify-content:space-between;flex-wrap:wrap}
.nx-mais img{width:230px;height:auto;display:block;margin-bottom:18px}
.nx-mais h2{font-size:clamp(30px,3.4vw,44px);font-weight:700;text-transform:uppercase;color:#fff;line-height:1.05}
.nx-mais p{margin-top:10px;color:#C3CDD6;max-width:56ch}
body.so-nero .menu a{white-space:nowrap}
@media (min-width:981px) and (max-width:1180px){body.so-nero .menu{gap:18px}body.so-nero .menu a{font-size:15px}.menu a.sol{padding:8px 10px}.menu a.sol i{display:none}}
</style>'''

# ---------------------------------------------------------------- pagina inicial: so NERO
s = troca(base, '</style>', CSS)
s = cabeca(s, 'Manta antichamas NERO em Santa Catarina | FOCO360, distribuidor exclusivo',
           'Manta antichamas NERO para veículos elétricos, híbridos e a combustão. A FOCO360 é distribuidora autorizada e exclusiva em Santa Catarina. Peça a sua proposta.', U)
s = troca(s, '<body>', '<body class="so-nero">')
s, _ = corta(s, '<div class="palco" aria-hidden="true">', 'Pausar fundo</button>\n')
s, _ = corta(s, '<section class="hero com-fundo" id="inicio"', '</section>\n')
s, _ = corta(s, '<section class="sec sec-branca" id="sobre">', '</main>', incluir_fim=False)
s = troca(s, '<a href="#inicio" aria-label="FOCO360, início">', '<a href="#distribuicao" aria-label="FOCO360, início">')
s, _ = corta(s, '      <a href="#distribuicao">Manta NERO</a>', '      <a class="cta" href="#contato">Fale conosco</a>\n')
s = troca(s, '<nav class="menu" id="menu" aria-label="Principal">\n', '''<nav class="menu" id="menu" aria-label="Principal">
      <a href="#nero-ficha">Equipamento</a>
      <a href="#nero-aplic">Aplicações</a>
      <a href="#nero-uso">Como utilizar</a>
      <a href="#nero-faq">Dúvidas</a>
      <a class="sol" href="solucoes.html">Demais soluções<i style="font-style:normal"> FOCO360</i></a>
      <a class="cta" href="#nero-contato">Pedir proposta</a>
''')
# abertura NERO primeiro; "Distribuidor exclusivo" e Panspar logo depois dos numeros
s, cab = corta(s, '<section id="distribuicao" aria-labelledby="rep-t">', '<div class="nero-hero">', incluir_fim=False)
cab = cab.replace('<section id="distribuicao" aria-labelledby="rep-t">', '')
s = troca(s, '<div class="nero-hero">', '<section id="distribuicao" aria-labelledby="rep-t">\n  <h1 class="sr">Manta antichamas NERO: FOCO360, distribuidor exclusivo em Santa Catarina</h1>\n  <div class="nero-hero">')
s = troca(s, '  <div class="sec nx-imp">', cab.strip('\n') + '\n\n  <div class="sec nx-imp">')
s = troca(s, '''        <a class="bt bt-linha" href="#nero-ficha">Conhecer o equipamento</a>
      </div>
''', '''        <a class="bt bt-linha" href="#nero-ficha">Conhecer o equipamento</a>
      </div>
      <a class="mais" href="solucoes.html">Conheça as demais soluções da FOCO360 →</a>
''')
# foco em venda e apresentacao: sai treinamento e avaliacao pela FOCO360
s = troca(s, '<li>Ensaio IPT com relatório</li><li>Treinamento FOCO360</li>', '<li>Ensaio IPT com relatório</li><li>Pronta entrega</li>')
s, _ = corta(s, '        <div class="aviso treino">', '        </div>\n')
s = troca(s, 'Resposta simples, em quatro passos. A equipe FOCO360 treina o seu time.', 'Resposta simples, em quatro passos.')
s = troca(s, ' A equipe FOCO360 avalia o seu espaço e indica a quantidade e o ponto de instalação.</p>', ' Conte para a nossa equipe comercial como é a sua garagem e receba a proposta.</p>')
s, _ = corta(s, '        <details><summary>Quem treina a equipe do meu prédio?</summary>', '</details>\n')
s = troca(s, '<div class="sec sec-clara" style="padding-top:88px">', '<div class="sec sec-clara" id="nero-aplic" style="padding-top:88px">')
s = troca(s, '''  <div class="sec nero-corpo">
    <div class="wrap">
      <h3 style="font-size:44px;font-weight:700;text-transform:uppercase">Como utilizar</h3>''', '''  <div class="sec nero-corpo" id="nero-uso">
    <div class="wrap">
      <h3 style="font-size:44px;font-weight:700;text-transform:uppercase">Como utilizar</h3>''')
s = troca(s, '''  <div class="sec sec-clara">
    <div class="wrap">
      <h3 style="font-size:44px;font-weight:700;text-transform:uppercase">Antes de decidir</h3>''', '''  <div class="sec sec-clara" id="nero-faq">
    <div class="wrap">
      <h3 style="font-size:44px;font-weight:700;text-transform:uppercase">Antes de decidir</h3>''')
a = s.index('        <h3>Agende uma demonstração técnica</h3>'); b = s.index('        <p class="nx-pans">', a)
s = s[:a] + '''        <h3>Peça a sua proposta</h3>
        <p>Fale com a nossa equipe comercial e receba a apresentação da manta NERO e a proposta para a sua estrutura.</p>
        <div class="acoes">
          <a class="bt bt-branco" href="''' + WA + '''" target="_blank" rel="noopener">WhatsApp (47) 99911-0090</a>
          <a class="bt bt-linha-b" style="border:2px solid #fff" href="mailto:rosinei360@gmail.com?subject=Proposta%20manta%20NERO">rosinei360@gmail.com</a>
        </div>
''' + s[b:]
s = troca(s, '</main>', '''<section class="nx-mais" aria-labelledby="mais-t">
  <div class="wrap">
    <div>
      <img src="assets/img/img-6.png" alt="FOCO360" width="304" height="70" loading="lazy">
      <h2 id="mais-t">A FOCO360 vai além da NERO</h2>
      <p>Gerenciamento de ferramentas, auditoria, consultoria e treinamentos para a indústria.</p>
    </div>
    <a class="bt bt-palha" href="solucoes.html">Conheça as demais soluções da FOCO360</a>
  </div>
</section>

</main>''')
s = troca(s, ' Vídeos de fundo: Mixkit.</span>', '</span>')
s = sem_blocos(s, {1, 3, 4, 5, 6})
for proibido in ('reinamento', 'avalia o seu', 'demonstração técnica', 'data-fundo', 'id="mira"'):
    assert proibido not in s.replace('consultoria e treinamentos', '').replace('consultoria, treinamentos', ''), proibido
open(p, 'w', encoding='utf-8').write(s)

# ---------------------------------------------------------------- solucoes.html: as demais frentes
t = troca(base, '</style>', CSS)
t = cabeca(t, 'FOCO360 | Gerenciamento de ferramentas, auditoria, consultoria e treinamentos',
           'A FOCO360, de Joinville (SC), presta serviços de gerenciamento de ferramentas, auditoria, consultoria em gestão de negócios, processos e recursos e treinamentos para a indústria.', U + 'solucoes.html')
t, _ = corta(t, '<section id="distribuicao" aria-labelledby="rep-t">', '</section>\n')
t = troca(t, '      <a href="#distribuicao">Manta NERO</a>', '      <a class="sol" href="./">Manta NERO</a>')
t = troca(t, '<a class="bt bt-nero" href="#distribuicao">Conhecer a manta NERO</a>', '<a class="bt bt-nero" href="./">Conhecer a manta NERO</a>')
t, _ = corta(t, '<div class="nx-modal" id="nx-modal"', '</script>\n')
t = sem_blocos(t, {7, 8})
assert 'nvid' not in t and 'nx-redes' not in t.split('</style>')[1]
open(os.path.join(raiz, 'solucoes.html'), 'w', encoding='utf-8').write(t)

open(os.path.join(raiz, 'sitemap.xml'), 'w', encoding='utf-8').write(
    '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>%s</loc></url>\n  <url><loc>%ssolucoes.html</loc></url>\n</urlset>\n' % (U, U))
print('foco nero ok', len(s), len(t))
