# Ajustes de conteudo aplicados depois do build.py (pedido de 20/11/2026):
# NERO como distribuicao exclusiva, secao NERO logo apos a abertura, treinamento pela equipe FOCO360.
import sys
p = sys.argv[1]
s = open(p, encoding='utf-8').read()
def sub(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:70])
    s = s.replace(a, b)

# titulo, descricao e dados para busca/compartilhamento
sub('FOCO360 | Gerenciamento de ferramentas, consultoria, treinamentos e representação',
    'FOCO360 | Consultoria, treinamentos e distribuição exclusiva da manta NERO', 2)
sub('presta serviços de gerenciamento de ferramentas, auditoria, consultoria em gestão de negócios, processos e recursos, treinamentos e representação comercial.',
    'presta serviços de gerenciamento de ferramentas, auditoria, consultoria e treinamentos, e é distribuidora autorizada e exclusiva da manta antichamas NERO em Santa Catarina.', 3)

# logo: texto alternativo sem "representação"
sub('alt="FOCO360 consultoria, treinamentos e representação"', 'alt="FOCO360"', 2)

# menu: Distribuição NERO em primeiro lugar
sub('      <a href="#representacoes">Representações</a>\n', '')
sub('      <a href="#sobre">Quem somos</a>', '      <a href="#distribuicao">Manta NERO</a>\n      <a href="#sobre">Quem somos</a>')

# abertura: mais curta, com a NERO no texto e no primeiro botao
sub('</style>', '.hero{min-height:84svh}\n.aviso.treino{border-left-color:var(--palha)}.aviso.treino strong{color:var(--palha)}\n</style>')
sub('<p>Gerenciamento de ferramentas, auditoria, consultoria, treinamentos e representação para a indústria. De Joinville, Santa Catarina.</p>',
    '<p>Gerenciamento de ferramentas, auditoria, consultoria, treinamentos e distribuição exclusiva da manta antichamas NERO. De Joinville, Santa Catarina, para todo o Brasil.</p>')
sub('      <a class="bt bt-palha" href="#servicos">Ver os serviços</a>',
    '      <a class="bt bt-nero" href="#distribuicao">Conhecer a manta NERO</a>\n      <a class="bt bt-palha" href="#servicos">Ver os serviços</a>')

# secao NERO: distribuidor exclusivo
sub('<section id="representacoes" aria-labelledby="rep-t">', '<section id="distribuicao" aria-labelledby="rep-t">')
sub('<h2 id="rep-t">Representações</h2>', '<h2 id="rep-t">Distribuidor exclusivo NERO</h2>')
sub('Além da consultoria, a FOCO360 representa produtos voltados à segurança das operações. Em Santa Catarina, somos representantes da manta antichamas NERO, com atendimento também a outras regiões.',
    'A FOCO360 é distribuidora autorizada e exclusiva da manta antichamas NERO em Santa Catarina, com atendimento também a outras regiões.')
sub('<span class="selo">NERO Manta Antichamas</span>', '<span class="selo">NERO Manta Antichamas · Distribuidor exclusivo em SC</span>')
sub('<td>2 profissionais</td>', '<td>2 pessoas</td>')
a = s.index('<div class="aviso">'); b = s.index('<div class="docs">')
s = s[:a] + '''<div class="aviso treino">
          <strong>Treinamento pela equipe FOCO360</strong>
          <p>O treinamento para o uso da manta é dado pela equipe FOCO360.</p>
        </div>
        ''' + s[b:]

# rodape
sub('FOCO360 consultoria, treinamentos e representação. Joinville, SC.', 'FOCO360 consultoria, treinamentos e distribuição exclusiva NERO. Joinville, SC.')

# secao NERO sobe para logo depois da abertura
a = s.index('<section id="distribuicao"'); b = s.index('</section>', a) + len('</section>\n\n')
bloco = s[a:b]; s = s[:a] + s[b:]
c = s.index('<section class="sec sec-branca" id="sobre">')
s = s[:c] + bloco + s[c:]
import re
resto = re.findall(r'.{50}epresenta.{30}', s.replace('Representa um', ''))
assert not resto, resto
open(p, 'w', encoding='utf-8').write(s)
print('ajustes ok', len(s))
