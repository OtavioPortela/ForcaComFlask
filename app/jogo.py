from random import choice, sample

def palavraJogo():
    palavras = ["Abacaxi", "Girassol", "Travesseiro",
                "Planeta", "Bicicleta", "Abóbora",
                "Telefone", "Cachoeira", "Espelho",
                "Chocolate"]
    valor = choice(range(len(palavras)))
    return palavras[valor]

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


