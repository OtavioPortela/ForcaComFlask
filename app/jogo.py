from random import choice, sample

def palavraJogo():
    palavras_e_dicas = [
    ["JavaScript", "Uma linguagem de programação amplamente usada em desenvolvimento web."],
    ["Python", "Uma linguagem de programação conhecida por sua legibilidade e versatilidade."],
    ["HTML", "A linguagem de marcação fundamental para criar páginas da web."],
    ["CSS", "Utilizado para estilizar páginas da web e torná-las visualmente atraentes."],
    ["Framework", "Uma estrutura de desenvolvimento que acelera a criação de aplicativos."],
    ["API", "Interface de programação de aplicativos usada para conectar diferentes sistemas."],
    ["Linux", "Um sistema operacional de código aberto."],
    ["Java", "Uma linguagem de programação usada para desenvolvimento de aplicativos móveis e empresariais."],
    ["Arduino", "Uma plataforma de prototipagem eletrônica."],
    ["Cybersegurança", "O campo de proteção contra ameaças cibernéticas."],
    ["Big Data", "Lida com grandes volumes de dados e análises."],
    ["Cloud Computing", "O uso de servidores remotos para armazenamento e processamento de dados."],
    ["Machine Learning", "Um subcampo da inteligência artificial onde os sistemas aprendem com dados."],
    ["HTML5", "A versão mais recente do HTML, que suporta recursos avançados."],
    ["CSS3", "A versão mais recente do CSS, que oferece animações e transições."],
    ["Ruby", "Uma linguagem de programação usada em desenvolvimento web."],
    ["SQL", "Linguagem de consulta estruturada para gerenciar bancos de dados."],
    ["DevOps", "Uma cultura que integra desenvolvimento e operações de TI."],
    ["Firewall", "Um dispositivo de segurança que protege redes contra ameaças."],
    ["Git", "Um sistema de controle de versão amplamente usado por desenvolvedores."],
    ["IoT", "A Internet das Coisas, que conecta dispositivos à internet."],
    ["Scrum", "Um método ágil de gerenciamento de projetos."],
    ["Algoritmo", "Uma série de etapas para resolver um problema ou executar uma tarefa."],
    ]
    valor = choice(range(len(palavras_e_dicas)))
    conjunto = palavras_e_dicas[valor]
    palavra = conjunto[0]
    dica = conjunto[1]
    return palavra, dica

def letrasForca(palavra):
    if len(palavra) <= 5: #se a palavra tiver menos de 5 letras
        numeroLetras = sample(range(len(palavra)), 1)
        return numeroLetras 
    elif 5 < len(palavra) <= 10:
        numeroLetras = sample(range(len(palavra)), 3)
        return numeroLetras
    else:
        numeroLetras = sample(range(len(palavra)), 4)
        return numeroLetras

def criarEspacos(lista, palavra):
    espacos = [' _ '] * len(palavra) #criar espacos vazios para ser colocado a palavra
    for i in lista: #prencher espaçõs vazios com as letras
        espacos[i] = palavra[i]
         
    return espacos


