
from flask import Flask, render_template
app = Flask(__name__)

from evento import Evento, Palestrantes, Categorias , Inicio

evento = Evento()
palestrante = Palestrantes()
categoria = Categorias()
inicio = Inicio()

dados_c_inicio = """Festival ASM 2025 Tecnologia, Saúde e Desenvolvimento em um só
              lugar Prepare-se para uma experiência única de conhecimento,
              conexão e inovação! Vem aí o ASM Festival, um evento que une
              mentes criativas, especialistas visionários e apaixonados por
              tecnologia, saúde e desenvolvimento humano. Durante três dias
              intensos, o ASM será palco de palestras inspiradoras, painéis
              interativos e workshops práticos, com nomes de peso das áreas mais
              transformadoras do nosso tempo. Desde avanços em inteligência
              artificial e biotecnologia até soluções para o bem-estar físico e
              mental, o festival promete abrir caminhos para o futuro. O que te
              espera: Talks com especialistas nacionais e internacionais
              Tendências em inovação digital e saúde conectada Experiências
              imersivas e networking com propósito Ambiente colaborativo para
              quem quer transformar o mundo Seja você um profissional da área,
              um estudante ou apenas alguém curioso por mudanças que realmente
              importam, o ASM Festival é o seu lugar."""

dados_c_Anome="Arthur Monsores"
dados_c_Hnome="Hans Wahrlich"
dados_c_Mnome="Helena Mussei"

dados_c_Acargo="Especialista Em Tecnologia Mecanica"
dados_c_Mcargo="Consultora na area da saude"
dados_c_Hcargo="Pesquisador em Inteligencia Artificial"

dados_c_Adescriçao = """Com uma mente inquieta e apaixonada por inovação, Arthur Monsores
              construiu sua carreira explorando os limites entre a engenharia
              mecânica tradicional e as novas tecnologias da indústria 4.0.
              Especialista em tecnologia mecânica, Arthur combina conhecimento
              técnico com visão estratégica para criar soluções inteligentes,
              eficientes e sustentáveis para os desafios da manufatura moderna.
              Graduado em Engenharia Mecânica e com especializações em automação
              industrial e design de sistemas mecânicos, Arthur atua há mais de
              10 anos no setor, liderando projetos que envolvem desde a
              implementação de linhas automatizadas até o desenvolvimento de
              protótipos de alta precisão para setores como aeroespacial,
              automotivo e de energia renovável."""

dados_c_Mdescriçao = """Com um olhar atento às necessidades humanas e uma abordagem
                baseada em evidências, Helena Mussei atua como consultora na
                área da saúde, conectando pessoas, instituições e soluções em
                prol de um cuidado mais eficiente, acolhedor e sustentável. Sua
                missão é clara: transformar o sistema de saúde por meio do
                conhecimento, da empatia e da inovação. Formada em Enfermagem,
                com MBA em Gestão em Saúde e especializações em políticas
                públicas e qualidade assistencial, Helena acumula mais de 12
                anos de experiência em hospitais, clínicas e projetos
                governamentais. Ao longo de sua trajetória, desenvolveu e
                implementou protocolos clínicos, treinou equipes
                multidisciplinares e colaborou com instituições na
                reestruturação de processos para melhorar a experiência do
                paciente e os resultados em saúde
"""

dados_c_Hdescriçao = """Hans Wahrlich movido por uma pergunta central: "Como podemos
                ensinar as máquinas a pensar de forma ética, eficiente e
                criativa?" Como pesquisador em Inteligência Artificial, ele
                dedica sua carreira a explorar os limites do aprendizado de
                máquina, processamento de linguagem natural e sistemas
                inteligentes aplicados à solução de problemas complexos. Formado
                em Ciência da Computação e com doutorado em Inteligência
                Artificial Aplicada, Hans combina sólida base técnica com uma
                visão crítica sobre o impacto social e ético das tecnologias
                emergentes. Seus estudos se concentram em redes neurais, modelos
                generativos e inteligência artificial explicável (XAI), com
                aplicações que vão desde a medicina de precisão até a automação
                de decisões em ambientes corporativos.
"""

dados_categoriaT="""Inovação que transforma o agora No espaço dedicado à tecnologia, o
            ASM Festival mergulha nas inovações que estão moldando o presente e
            o futuro. Inteligência artificial, realidade aumentada, blockchain,
            robótica, segurança digital — você vai se conectar com as mentes por
            trás das maiores transformações do nosso tempo. Descubra como a
            tecnologia pode impulsionar negócios, resolver problemas sociais e
            melhorar a vida das pessoas. Aqui, o futuro é agora.
"""
dados_categoriaS=""" Cuidar de pessoas é revolucionário A saúde está no centro do
            progresso. No ASM, reunimos especialistas, médicos, terapeutas,
            pesquisadores e startups para falar sobre bem-estar físico, mental e
            emocional. De tecnologias para a medicina personalizada a práticas
            integrativas, nosso foco é promover uma vida mais equilibrada e
            acessível para todos. Porque inovar também é cuidar.
"""
dados_categoriaD="""Pessoas, sociedade e propósito O verdadeiro desenvolvimento vai além
            da técnica: ele envolve crescimento humano, social e sustentável.
            Nesta trilha, o ASM Festival aborda temas como educação, liderança,
            empreendedorismo social, sustentabilidade, inclusão e impacto. É um
            espaço para quem acredita que transformar o mundo começa com
            transformar a si mesmo e o seu entorno. Desenvolver é evoluir com
            consciência.
"""
inicio_lista = [
    {"id":"lista" ,"descricao":dados_c_inicio}
]

palestrantes_lista= [
    {"id":"1","nome":dados_c_Anome, "cargo":dados_c_Acargo , "descricao":dados_c_Adescriçao},
    {"id":"2","nome":dados_c_Mnome, "cargo":dados_c_Mcargo , "descricao":dados_c_Mdescriçao},
    {"id":"3", "nome":dados_c_Hnome, "cargo":dados_c_Hcargo , "descricao":dados_c_Hdescriçao}
]
categorias_lista = [ 
    {"id":"tecnologia","descricao":dados_categoriaT},
    {"id":"saude", "descricao":dados_categoriaS},
    {"id":"desenvolvimento","descricao":dados_categoriaD}
    
]
@app.route ('/')
def home():
    return render_template('index.html',home=inicio_lista)

@app.route('/detalhes')
def detalhes():
    return render_template ('detalhes.html')

@app.route('/categorias')
def categorias():
    return render_template ('categorias.html',categorias=categorias_lista)

@app.route('/palestrantes')
def palestrantes():
    return render_template('palestrantes.html',palestrantes=palestrantes_lista)