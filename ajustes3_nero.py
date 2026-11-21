# Secao NERO ampliada com material oficial da NERO (pedido de 21/11/2026). Roda depois do ajustes2.
import sys, os, shutil, subprocess, urllib.request
p = sys.argv[1]
raiz = os.path.dirname(p) or '.'
dest = os.path.join(raiz, 'assets', 'nero')
os.makedirs(dest, exist_ok=True)
FONTE = os.environ.get('NERO_SRC') or ('material-nero' if os.path.isdir('material-nero') else '')   # copia local do material da NERO
BASE = 'https://neroglobal.com.br/'
ARQ = {
    'garagem-1600.mp4': 'assets/video/nero-cena-garagem-1600.mp4',
    'garagem-720.mp4': 'assets/video/nero-cena-garagem-720.mp4',
    'bolsa-giro.mp4': 'assets/video/nero-bolsa-giro-v10.mp4',
    'poster-1600.webp': 'assets/images/cenas/hero-poster-1600.webp',
    'poster-720.webp': 'assets/images/cenas/hero-poster-720.webp',
    'pos-incendio.webp': 'assets/images/cenas/pos-incendio-900.webp',
    'condominio.webp': 'assets/images/cenas/flow-condominio-garagem-640.webp',
    'shopping.webp': 'assets/images/cenas/flow-shopping-estacionamento-640.webp',
    'operadores.webp': 'assets/images/scenarios/frota-operadores.webp',
    'bolsa-frente.webp': 'assets/images/product/01-front.webp',
    'bolsa-diagonal.webp': 'assets/images/product/02-front-right.webp',
    'bolsa-aberta.webp': 'assets/images/product/09-open.webp',
}
for nome, origem in ARQ.items():
    alvo = os.path.join(dest, nome)
    if FONTE and os.path.exists(os.path.join(FONTE, origem)):
        shutil.copyfile(os.path.join(FONTE, origem), alvo)
    else:
        req = urllib.request.Request(BASE + origem, headers={'User-Agent': 'Mozilla/5.0'})
        open(alvo, 'wb').write(urllib.request.urlopen(req, timeout=120).read())
for nome, escala in (('garagem-1600', '640:360'), ('garagem-720', '360:450')):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', os.path.join(dest, nome + '.mp4'), '-an', '-vf', 'scale=' + escala,
                    '-c:v', 'libx264', '-preset', 'veryslow', '-crf', '34', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
                    os.path.join(dest, nome + '-low.mp4')], check=True)

s = open(p, encoding='utf-8').read()
def sub(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b)

WA = 'https://wa.me/5547999110090?text=Ol%C3%A1%2C%20quero%20uma%20proposta%20da%20manta%20antichamas%20NERO.'
WA_DEMO = 'https://wa.me/5547999110090?text=Ol%C3%A1%2C%20quero%20agendar%20uma%20demonstra%C3%A7%C3%A3o%20t%C3%A9cnica%20da%20manta%20NERO.'

# Panspar: e-mail junto do contato
sub('''        <a class="bt bt-palha" href="https://wa.me/5547996095141" target="_blank" rel="noopener">WhatsApp (47) 99609-5141</a>
''', '''        <div class="acoes" style="margin-top:0">
          <a class="bt bt-palha" href="https://wa.me/5547996095141" target="_blank" rel="noopener">WhatsApp (47) 99609-5141</a>
          <a class="bt bt-linha" href="mailto:rodrigo@panspar.com.br">rodrigo@panspar.com.br</a>
        </div>
''')

CSS = '''
/* NERO ampliada */
.nero-hero .wrap{padding-top:120px;padding-bottom:132px}
.nero-hero video{opacity:.78}
.nero-hero::after{background:linear-gradient(90deg,rgba(14,6,7,.95) 0%,rgba(14,6,7,.74) 44%,rgba(14,6,7,.12) 100%)}
.nero-hero .video-ctl{top:24px;bottom:auto}
.nero-hero .nota{position:absolute;left:24px;bottom:16px;z-index:3;font-size:13px;color:#D9C6C8;max-width:60ch}
.nero-hero h2 em{font-style:normal;color:#FF5A6E}
.nx-num{background:var(--nero);color:#fff}
.nx-num .wrap{display:grid;grid-template-columns:repeat(5,minmax(0,1fr))}
.nx-num div{padding:30px 22px;border-right:1px solid rgba(255,255,255,.28)}
.nx-num div:last-child{border-right:0}
.nx-num b{display:block;font-family:var(--disp);font-weight:700;font-size:46px;line-height:1;letter-spacing:.5px}
.nx-num span{display:block;margin-top:8px;font-size:16px;color:#FFE3E6}
.nx-imp{background:#120708;color:#fff;position:relative;overflow:hidden}
.nx-imp .wrap{display:grid;grid-template-columns:.9fr 1.1fr;gap:64px;align-items:center}
.nx-imp figure{margin:0;position:relative}
.nx-imp img{width:100%;height:auto;display:block;border-bottom:6px solid var(--nero)}
.nx-imp figcaption,.nx-leg{font-size:13px;color:#A99A9C;margin-top:8px}
.nx-imp h3{font-size:clamp(38px,4.6vw,62px);font-weight:700;text-transform:uppercase;line-height:1.02}
.nx-imp h3 em{font-style:normal;color:#FF5A6E}
.nx-imp .intro{color:#E3D5D6}
.nx-lista{list-style:none;margin:30px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:0 28px}
.nx-lista li{padding:16px 0;border-top:1px solid rgba(255,255,255,.18)}
.nx-lista b{display:block;font-family:var(--disp);font-size:23px;font-weight:700;text-transform:uppercase;letter-spacing:.4px}
.nx-lista span{display:block;color:#CDBFC0;font-size:16px;margin-top:2px}
.nx-fecho{margin-top:28px;font-size:20px;font-weight:600;color:#fff;border-left:5px solid var(--nero);padding-left:16px}
.ficha{grid-template-columns:minmax(0,460px) 1fr}
.nx-gal .palco-g{position:relative;background:#F3F4F5;border-bottom:6px solid var(--nero);aspect-ratio:5/4;overflow:hidden}
.nx-gal .palco-g img,.nx-gal .palco-g video{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;border:0}
.nx-gal .palco-g img.cobre{object-fit:cover}
.nx-thumbs{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-top:10px}
.nx-thumbs button{all:unset;box-sizing:border-box;cursor:pointer;aspect-ratio:1;background:#F3F4F5 center/cover no-repeat;border:2px solid var(--linha);position:relative}
.nx-thumbs button[aria-pressed="true"]{border-color:var(--nero)}
.nx-thumbs button:focus-visible{outline:3px solid var(--azul);outline-offset:2px}
.nx-thumbs .play::after{content:"";position:absolute;left:50%;top:50%;transform:translate(-35%,-50%);border-left:16px solid #fff;border-top:10px solid transparent;border-bottom:10px solid transparent;filter:drop-shadow(0 0 4px rgba(0,0,0,.7))}
.nx-selos{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px;padding:0;list-style:none}
.nx-selos li{background:#FFF0F2;color:#8E1022;font-weight:600;font-size:15px;padding:6px 12px;border-radius:3px}
.setor{padding:0;display:flex;flex-direction:column}
.setor img{width:100%;aspect-ratio:4/3;object-fit:cover;display:block}
.setor h3,.setor p{padding:0 22px}.setor h3{margin-top:20px}.setor p{padding-bottom:24px}
.nx-uso{display:grid;grid-template-columns:minmax(0,.62fr) minmax(0,1.38fr);gap:40px;margin-top:40px;align-items:stretch}
.nx-uso figure{margin:0;position:relative;background:#000}
.nx-uso figure{aspect-ratio:4/5;overflow:hidden}
.nx-uso figure video{width:100%;height:100%;object-fit:cover;display:block}
.nx-uso figure figcaption{position:absolute;left:0;top:0;background:rgba(0,0,0,.66);color:#fff;font-size:13px;padding:6px 12px}
.nx-uso .usar{margin-top:0;grid-template-columns:1fr 1fr}
.nx-uso .usar button{min-height:0}
.nx-uso .usar button:nth-child(2n){border-right:0}
.nx-uso .usar button:nth-child(-n+2){border-top:0}
.nx-uso .usar button{border-top:1px solid var(--linha)}
.nx-faq{max-width:900px}
.nx-faq details{border-bottom:1px solid var(--linha);background:var(--branco)}
.nx-faq details:first-of-type{border-top:3px solid var(--nero)}
.nx-faq summary{cursor:pointer;list-style:none;padding:22px 56px 22px 24px;font-family:var(--disp);font-size:26px;font-weight:600;position:relative}
.nx-faq summary::-webkit-details-marker{display:none}
.nx-faq summary::after{content:"+";position:absolute;right:24px;top:50%;transform:translateY(-50%);font-size:32px;color:var(--nero);font-family:var(--txt);font-weight:400}
.nx-faq details[open] summary::after{content:"\\2212"}
.nx-faq summary:focus-visible{outline:3px solid var(--azul);outline-offset:-3px}
.nx-faq p{padding:0 24px 24px;color:var(--cinza);font-size:18px;line-height:1.55;margin:0}
.nx-redes{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:36px}
.nx-redes button{all:unset;box-sizing:border-box;cursor:pointer;display:block;color:#fff;background:var(--aco);padding:26px 26px 76px;border-top:5px solid var(--nero);min-height:200px;position:relative}
.nx-redes button:hover{background:var(--aco-2)}
.nx-redes button:focus-visible{outline:3px solid var(--azul);outline-offset:3px}
.nx-redes i{position:absolute;left:26px;bottom:22px;width:44px;height:44px;border-radius:50%;background:var(--nero)}
.nx-redes i::after{content:"";position:absolute;left:50%;top:50%;transform:translate(-35%,-50%);border-left:14px solid #fff;border-top:9px solid transparent;border-bottom:9px solid transparent}
.nx-modal{position:fixed;inset:0;z-index:90;background:rgba(8,12,16,.88);display:flex;align-items:center;justify-content:center;padding:16px}
.nx-modal[hidden]{display:none}
.nx-modal .cx{position:relative;width:min(420px,100%);height:min(780px,calc(100vh - 32px));background:#fff;display:flex;flex-direction:column}
.nx-modal iframe{flex:1;width:100%;border:0;background:#fff}
.nx-modal .rod{padding:10px 14px;font-size:14px;color:var(--cinza);background:#fff;border-top:1px solid var(--linha)}
.nx-modal .rod a{color:var(--tinta);font-weight:600}
.nx-modal .fx{position:absolute;right:0;top:-46px;background:#fff;color:var(--tinta);border:0;font:600 15px var(--txt);padding:9px 16px;cursor:pointer;border-radius:3px}
@media (max-width:640px){.nx-modal .fx{top:8px;right:8px;z-index:2;box-shadow:0 2px 10px rgba(0,0,0,.4)}}
.nx-redes small{display:block;font-size:14px;letter-spacing:1px;text-transform:uppercase;color:#FF8E9C;font-weight:600}
.nx-redes b{display:block;font-family:var(--disp);font-size:27px;font-weight:700;text-transform:uppercase;margin-top:8px;line-height:1.1}
.nx-redes span{display:block;margin-top:14px;font-size:15px;color:#C3CDD6}
.nx-pans{margin-top:26px;padding-top:22px;border-top:1px solid rgba(255,255,255,.4);font-size:17px;color:#FFE9EC}
.nx-pans a{color:#fff;font-weight:600}
.nx-fab{position:fixed;right:18px;bottom:18px;z-index:40;display:flex;align-items:center;gap:10px;background:#1FAF5A;color:#fff;text-decoration:none;font-weight:600;font-size:16px;padding:13px 20px;border-radius:40px;box-shadow:0 6px 22px rgba(0,0,0,.35)}
.nx-fab:hover{background:#17964B}
.nx-fab svg{width:22px;height:22px;flex:none}
@media (max-width:980px){
  .nx-num .wrap{grid-template-columns:repeat(2,minmax(0,1fr));padding:0}
  .nx-num div{border-bottom:1px solid rgba(255,255,255,.28)}
  .nx-num div:nth-child(2n){border-right:0}
  .nx-num div:last-child{grid-column:1/-1;border-bottom:0}
  .nx-imp .wrap,.nx-uso,.ficha{grid-template-columns:1fr;gap:36px}
  .nx-uso figure{max-width:420px}
  .ficha figure{max-width:none}
  .nx-redes{grid-template-columns:1fr}
  .nx-redes button{min-height:0}
}
@media (max-width:640px){
  .nx-lista{grid-template-columns:1fr}
  .nx-uso .usar{grid-template-columns:1fr}
  .nx-uso .usar button{border-right:0}
  .nx-uso .usar button:nth-child(2){border-top:1px solid var(--linha)}
  .nero-hero .wrap{padding-top:88px;padding-bottom:120px}
  .nx-fab span{display:none}.nx-fab{padding:14px}
  .nx-faq summary{font-size:22px}
}
</style>'''
sub('</style>', CSS)

a = s.index('<div class="nero-hero">')
b = s.index('</section>', a)
NOVO = '''<div class="nero-hero">
    <video id="nvid" muted loop playsinline preload="none" poster="assets/nero/poster-1600.webp" aria-label="Simulação ilustrativa: veículo em chamas em uma garagem"></video>
    <script>(function(){var v=document.getElementById('nvid'),m=window.matchMedia&&matchMedia('(max-width:700px)').matches,n=m?'garagem-720':'garagem-1600';v.poster='assets/nero/'+(m?'poster-720.webp':'poster-1600.webp');v.dataset.hq='assets/nero/'+n+'.mp4';v.src='assets/nero/'+n+'-low.mp4';})();</script>
    <div class="wrap">
      <span class="selo">NERO Manta Antichamas · Distribuidor exclusivo em SC</span>
      <h2>O fogo começa em uma vaga. <em>Sua garagem está pronta?</em></h2>
      <p>A manta antichamas NERO cobre o veículo inteiro e ajuda a conter as chamas enquanto a resposta chega. Para carros elétricos, híbridos e a combustão.</p>
      <div class="acoes">
        <a class="bt bt-nero" href="''' + WA + '''" target="_blank" rel="noopener">Pedir proposta agora</a>
        <a class="bt bt-linha" href="#nero-ficha">Conhecer o equipamento</a>
      </div>
    </div>
    <button class="video-ctl" id="vctl" type="button" aria-pressed="false">Pausar vídeo</button>
    <p class="nota">Simulação ilustrativa da campanha NERO. Não é registro de ocorrência real.</p>
  </div>

  <div class="nx-num" aria-label="Dados da manta NERO">
    <div class="wrap">
      <div><b>6 × 8 m</b><span>Cobre o veículo inteiro</span></div>
      <div><b>48 m²</b><span>De manta antichamas</span></div>
      <div><b>22 kg</b><span>Duas pessoas posicionam</span></div>
      <div><b>Uso único</b><span>Reposição após o uso</span></div>
      <div><b>Pronta entrega</b><span>Em bolsa de parede, à vista</span></div>
    </div>
  </div>

  <div class="sec nx-imp">
    <div class="wrap">
      <figure>
        <img src="assets/nero/pos-incendio.webp" alt="Garagem de subsolo com veículo queimado ao lado de um ponto de recarga" width="900" height="900" loading="lazy">
        <figcaption>Imagem ilustrativa da campanha NERO.</figcaption>
      </figure>
      <div>
        <h3>O incêndio começa em uma vaga. <em>O prejuízo não para nela.</em></h3>
        <p class="intro">Em uma garagem, os carros ficam lado a lado. Sem contenção rápida, o fogo de um veículo vira um problema do prédio inteiro.</p>
        <ul class="nx-lista">
          <li><b>Veículos vizinhos</b><span>Os carros das vagas ao lado são os primeiros atingidos.</span></li>
          <li><b>Estrutura</b><span>Lajes, colunas e vigas expostas ao calor.</span></li>
          <li><b>Instalações do prédio</b><span>Elétrica, hidráulica e sprinklers.</span></li>
          <li><b>Interdição</b><span>Área isolada, limpeza e laudos técnicos.</span></li>
          <li><b>Rotina parada</b><span>Garagem fechada e moradores ou clientes sem acesso.</span></li>
          <li><b>Responsabilidade</b><span>Discussões com seguradoras e questões jurídicas.</span></li>
        </ul>
        <p class="nx-fecho">A manta fica na parede, pronta, antes que qualquer um desses itens entre na conta.</p>
        <div class="acoes" style="margin-top:28px"><a class="bt bt-nero" href="''' + WA + '''" target="_blank" rel="noopener">Quero proteger minha garagem</a></div>
      </div>
    </div>
  </div>

  <div class="sec nero-corpo" id="nero-ficha">
    <div class="wrap ficha">
      <div class="nx-gal">
        <div class="palco-g" id="gal-palco">
          <video id="gal-v" muted loop playsinline preload="none" poster="assets/nero/bolsa-frente.webp" src="assets/nero/bolsa-giro.mp4" aria-label="Vídeo do produto: bolsa da manta NERO girando"></video>
          <img id="gal-i" alt="" hidden>
        </div>
        <div class="nx-thumbs" id="gal-t">
          <button type="button" class="play" aria-pressed="true" data-v="1" style="background-image:url(assets/nero/bolsa-frente.webp)" aria-label="Vídeo do produto"></button>
          <button type="button" aria-pressed="false" data-i="assets/nero/bolsa-frente.webp" data-a="Bolsa vermelha da manta NERO, vista de frente" style="background-image:url(assets/nero/bolsa-frente.webp)" aria-label="Foto: frente"></button>
          <button type="button" aria-pressed="false" data-i="assets/nero/bolsa-diagonal.webp" data-a="Bolsa da manta NERO, vista em diagonal" style="background-image:url(assets/nero/bolsa-diagonal.webp)" aria-label="Foto: diagonal"></button>
          <button type="button" aria-pressed="false" data-i="assets/nero/bolsa-aberta.webp" data-a="Bolsa da manta NERO aberta" style="background-image:url(assets/nero/bolsa-aberta.webp)" aria-label="Foto: bolsa aberta"></button>
          <button type="button" aria-pressed="false" data-i="assets/img/img-8.jpg" data-c="1" data-a="Bolsa da manta NERO instalada na parede, perto do ponto de recarga" style="background-image:url(assets/img/img-8.jpg)" aria-label="Foto: instalada na parede"></button>
        </div>
        <p class="nx-leg" style="color:var(--cinza)">Vídeo e fotos reais do produto. A manta fica em bolsa de parede, perto dos pontos de recarga.</p>
      </div>
      <div>
        <h3 style="font-size:44px;font-weight:700;text-transform:uppercase">Prevenção que protege seus bens e seu patrimônio</h3>
        <p style="margin-top:14px;color:var(--cinza)">Pronta entrega no Brasil. Produto ensaiado em laboratório, com relatório técnico. A bolsa vermelha deixa o equipamento à vista e fácil de identificar na hora em que cada segundo conta.</p>
        <ul class="nx-selos"><li>Elétricos, híbridos e a combustão</li><li>Ensaio IPT com relatório</li><li>Treinamento FOCO360</li></ul>
        <table class="spec">
          <tr><th scope="row">Dimensão</th><td>6 m × 8 m</td></tr>
          <tr><th scope="row">Área</th><td>48 m²</td></tr>
          <tr><th scope="row">Peso</th><td>22 kg</td></tr>
          <tr><th scope="row">Aplicação</th><td>Uso único</td></tr>
          <tr><th scope="row">Operação</th><td>2 pessoas</td></tr>
          <tr><th scope="row">Veículos</th><td>Elétricos, híbridos e a combustão</td></tr>
          <tr><th scope="row">Ensaio</th><td>Relatório IPT nº 1 160 363-203</td></tr>
        </table>
        <div class="aviso treino">
          <strong>Treinamento pela equipe FOCO360</strong>
          <p>O treinamento para o uso da manta é dado pela equipe FOCO360.</p>
        </div>
        <div class="docs">
          <h4>Documento</h4>
          <p>O tecido da manta passou por ensaio em laboratório. Abra o relatório:</p>
          <div class="acoes">
            <a class="bt bt-doc" href="assets/docs/NERO-relatorio-de-ensaio-1160363-203.pdf" target="_blank" rel="noopener">Relatório de ensaio nº 1 160 363-203 (PDF)</a>
            <a class="bt bt-nero" href="''' + WA + '''" target="_blank" rel="noopener">Pedir proposta</a>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="sec sec-clara" style="padding-top:88px">
    <div class="wrap">
      <h3 style="font-size:44px;font-weight:700;text-transform:uppercase">Reduza a exposição antes que o incidente se espalhe</h3>
      <p class="intro" style="max-width:62ch">Onde há veículos estacionados lado a lado, há risco de propagação. Veja onde a manta NERO entra no plano de emergência.</p>
      <div class="setores">
        <div class="setor"><img src="assets/nero/condominio.webp" alt="Veículo em chamas em garagem de condomínio" loading="lazy"><h3>Condomínios</h3><p>Adote planos de prevenção e resposta que reduzam a propagação do fogo, protejam moradores e áreas comuns e minimizem os danos ao patrimônio do condomínio.</p></div>
        <div class="setor"><img src="assets/nero/operadores.webp" alt="Duas pessoas cobrindo um veículo com a manta em um estacionamento" loading="lazy"><h3>Seguradoras</h3><p>Apoie planos de prevenção e resposta que limitam a propagação do fogo, os danos a veículos próximos e a exposição patrimonial.</p></div>
        <div class="setor"><img src="assets/nero/shopping.webp" alt="Veículo com fumaça em estacionamento de shopping" loading="lazy"><h3>Shoppings e estacionamentos</h3><p>Controle o foco do incêndio em áreas com alta concentração de veículos e preserve rotas, estruturas e operações adjacentes.</p></div>
        <div class="setor"><img src="assets/nero/poster-720.webp" alt="Chamas junto à roda de um veículo ao lado de um ponto de recarga" loading="lazy"><h3>Postos e eletropostos</h3><p>Tenha uma resposta dedicada para veículos elétricos, híbridos ou a combustão em áreas críticas de abastecimento e recarga.</p></div>
      </div>
      <p class="nx-leg" style="color:var(--cinza);margin-top:12px">Imagens ilustrativas da campanha NERO, não são registros de ocorrências reais.</p>
      <p style="margin-top:30px;font-weight:600">Proteção para ambientes com veículos:</p>
      <ul class="ambientes"><li>Condomínios</li><li>Estacionamentos</li><li>Eletropostos</li><li>Shopping centers</li><li>Empresas e indústrias</li><li>Frotas</li><li>Concessionárias</li><li>Oficinas</li><li>Hotéis</li><li>Hospitais</li><li>Aeroportos</li><li>Centros logísticos</li><li>Postos de combustíveis</li></ul>
    </div>
  </div>

  <div class="sec nero-corpo">
    <div class="wrap">
      <h3 style="font-size:44px;font-weight:700;text-transform:uppercase">Como utilizar</h3>
      <p class="intro" style="margin-top:10px">Resposta simples, em quatro passos. A equipe FOCO360 treina o seu time.</p>
      <div class="nx-uso">
        <figure>
          <video id="demo-v" muted loop playsinline controls preload="metadata" src="assets/video/video-6.mp4" aria-label="Demonstração: manta NERO cobrindo um veículo"></video>
          <figcaption>Demonstração da manta NERO cobrindo um veículo.</figcaption>
        </figure>
        <div class="usar" id="usar">
          <button type="button" aria-current="step"><span class="k">1</span><h3>Acione a emergência</h3><p>Isole a área e acione bombeiros ou brigadistas treinados.</p></button>
          <button type="button"><span class="k">2</span><h3>Abra e posicione</h3><p>Duas pessoas seguram as extremidades em lados opostos do veículo.</p></button>
          <button type="button"><span class="k">3</span><h3>Cubra da frente para trás</h3><p>Estenda a manta por completo e ajuste ao redor do veículo.</p></button>
          <button type="button"><span class="k">4</span><h3>Afaste-se e monitore</h3><p>Mantenha distância segura e siga o protocolo da equipe responsável.</p></button>
        </div>
      </div>
    </div>
  </div>

  <div class="sec sec-clara">
    <div class="wrap">
      <h3 style="font-size:44px;font-weight:700;text-transform:uppercase">Antes de decidir</h3>
      <p class="intro" style="margin-top:10px;margin-bottom:32px">As dúvidas mais comuns de síndicos, gestores e seguradoras.</p>
      <div class="nx-faq">
        <details open><summary>Quantas mantas a minha garagem precisa?</summary><p>Não existe um número único. Depende do número de vagas e pavimentos, de onde ficam os pontos de recarga, dos acessos e de quem atua no local. A equipe FOCO360 avalia o seu espaço e indica a quantidade e o ponto de instalação.</p></details>
        <details><summary>Para quais veículos a manta serve?</summary><p>Para veículos elétricos, híbridos e a combustão. Com 6 × 8 m e 48 m², a manta cobre o veículo inteiro.</p></details>
        <details><summary>A manta pode ser usada mais de uma vez?</summary><p>Não. A manta NERO é de uso único. Depois de uma ocorrência, ela deve ser reposta.</p></details>
        <details><summary>A manta substitui os Bombeiros ou os sistemas do prédio?</summary><p>Não. A manta é um recurso complementar, que entra no plano de emergência do local. Os sistemas de segurança e o atendimento dos Bombeiros continuam necessários. Em caso de fogo ou fumaça, afaste-se e ligue 193.</p></details>
        <details><summary>O que o relatório do IPT mostra?</summary><p>O Relatório de Ensaio IPT nº 1 160 363-203, de 23/02/2026, registra os resultados de ensaio de uma amostra do tecido em laboratório. Ele não é uma certificação do produto nem um teste de incêndio veicular em escala real. O relatório completo está disponível nesta página.</p></details>
        <details><summary>Quem treina a equipe do meu prédio?</summary><p>A equipe FOCO360. O treinamento de uso da manta é dado por nós.</p></details>
        <details><summary>Como comprar em Santa Catarina?</summary><p>A FOCO360 é a distribuidora autorizada e exclusiva da manta NERO em Santa Catarina, com pronta entrega e atendimento também a outras regiões. Fale com a FOCO360 ou com a Panspar, nossa representante exclusiva.</p></details>
      </div>
    </div>
  </div>

  <div class="sec nero-corpo">
    <div class="wrap">
      <h3 style="font-size:44px;font-weight:700;text-transform:uppercase">Veja em vídeo</h3>
      <p class="intro" style="margin-top:10px">Três vídeos curtos para entender o risco e conhecer o equipamento. Eles abrem aqui mesmo, sem sair do site.</p>
      <div class="nx-redes">
        <button type="button" data-reel="Dew8-QrgKVg"><small>Vídeo</small><b>Conheça o equipamento</b><span>A apresentação da manta, em detalhes.</span><i aria-hidden="true"></i></button>
        <button type="button" data-reel="De4djYHE3SR"><small>Vídeo</small><b>Ocorrência em Santa Catarina</b><span>O que observar depois de um incêndio veicular.</span><i aria-hidden="true"></i></button>
        <button type="button" data-reel="Df0Tup2k-Bh"><small>Vídeo</small><b>O que é fuga térmica</b><span>A animação que explica o risco das baterias.</span><i aria-hidden="true"></i></button>
      </div>
    </div>
  </div>

  <div class="sec sec-clara" id="nero-contato">
    <div class="wrap demo">
      <img src="assets/img/img-7.jpg" alt="Manta NERO estendida sobre um veículo em demonstração ao ar livre" width="900" height="750" loading="lazy">
      <div class="caixa-contato">
        <h3>Agende uma demonstração técnica</h3>
        <p>Descubra o ponto ideal de instalação, o protocolo de resposta e a quantidade recomendada para a sua estrutura.</p>
        <div class="acoes">
          <a class="bt bt-branco" href="''' + WA_DEMO + '''" target="_blank" rel="noopener">WhatsApp (47) 99911-0090</a>
          <a class="bt bt-linha-b" style="border:2px solid #fff" href="mailto:rosinei360@gmail.com?subject=Demonstra%C3%A7%C3%A3o%20t%C3%A9cnica%20NERO">rosinei360@gmail.com</a>
        </div>
        <p class="nx-pans">Ou fale com a Panspar, representante exclusiva da FOCO360: Rodrigo, <a href="https://wa.me/5547996095141" target="_blank" rel="noopener">(47) 99609-5141</a> · <a href="mailto:rodrigo@panspar.com.br">rodrigo@panspar.com.br</a></p>
      </div>
    </div>
  </div>

'''
s = s[:a] + NOVO + s[b:]

sub('</body>', '''<a class="nx-fab" href="''' + WA + '''" target="_blank" rel="noopener" aria-label="Pedir proposta da manta NERO pelo WhatsApp"><svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4 3h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H10l-5 4v-4H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/></svg><span>Proposta manta NERO</span></a>
<div class="nx-modal" id="nx-modal" hidden role="dialog" aria-modal="true" aria-label="Vídeo">
  <div class="cx">
    <button type="button" class="fx" id="nx-fx">Fechar ✕</button>
    <iframe id="nx-if" title="Vídeo" allow="autoplay; encrypted-media; picture-in-picture" allowfullscreen scrolling="no"></iframe>
    <p class="rod">O vídeo não carregou? <a id="nx-lk" href="#" target="_blank" rel="noopener">Abrir o vídeo em outra aba</a></p>
  </div>
</div>
<script>
(function(){
  var m=document.getElementById('nx-modal'),f=document.getElementById('nx-if'),lk=document.getElementById('nx-lk'),quem=null;
  function fecha(){m.hidden=true;f.removeAttribute('src');document.documentElement.style.overflow='';if(quem)quem.focus();}
  [].forEach.call(document.querySelectorAll('.nx-redes button'),function(b){b.addEventListener('click',function(){
    quem=b;var u='https://www.instagram.com/reel/'+b.dataset.reel+'/';
    f.src=u+'embed/';lk.href=u;m.hidden=false;document.documentElement.style.overflow='hidden';document.getElementById('nx-fx').focus();
  });});
  document.getElementById('nx-fx').addEventListener('click',fecha);
  m.addEventListener('click',function(e){if(e.target===m)fecha();});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!m.hidden)fecha();});
})();
(function(){
  var v=document.getElementById('gal-v'),im=document.getElementById('gal-i'),bs=[].slice.call(document.querySelectorAll('#gal-t button'));
  if(!v)return;
  var RM=window.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches,visivel=false,modoVideo=true;
  function toca(){if(modoVideo&&visivel&&!RM)v.play().catch(function(){});else v.pause();}
  bs.forEach(function(b){b.addEventListener('click',function(){
    bs.forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false');});
    if(b.dataset.v){modoVideo=true;im.hidden=true;v.hidden=false;if(RM)v.controls=true;}
    else{modoVideo=false;v.hidden=true;im.src=b.dataset.i;im.alt=b.dataset.a||'';im.className=b.dataset.c?'cobre':'';im.hidden=false;}
    toca();
  });});
  if(RM)v.controls=true;
  if('IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){visivel=e.isIntersecting;toca();});},{threshold:.3}).observe(document.getElementById('gal-palco'));}else{visivel=true;toca();}
  var d=document.getElementById('demo-v');
  if(d&&!RM&&'IntersectionObserver' in window){new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)d.play().catch(function(){});else d.pause();});},{threshold:.4}).observe(d);}
})();
</script>
</body>''')
open(p, 'w', encoding='utf-8').write(s)
print('nero ok', len(s))
