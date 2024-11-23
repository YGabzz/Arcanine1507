def  saudacoes (nome):
    import random
    frases = ["Bom dia! Meu nome é " + nome + " Como vai você?", "Oi, qual a sua pergunta?", "Olá, tudo bem?", "Opa, tudo bom?"]
    print(frases[random.randint(0, 3)])

def recebeTexto():
    texto = "Cliente: " + input("Cliente: ")
    palavrasProibidas = ["Idiota", "Animal", "Bunda mole", "Aberração", "Bobão", "Bocó", "Tongo", "Burro"]
    for p in palavrasProibidas:
        if p in texto:
            print("Oxi, vai me xingar? Frustrado. VEM PRA CIMA ENTÃO, QUERO VER TU AGUENTAR")
            return recebeTexto()
        return texto
    
def buscaResposta(nome, texto):
    with open("BaseConhecimento.txt", "+a") as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if texto.replace("Cliente:", "") == "Tchau":
                    print(nome + "Volte sempre!")
                    return "fim"
                elif viu.strip() == texto.strip():
                    proximaLinha = conhecimento.readline
                    if "ChatBot: " in proximaLinha:
                        return proximaLinha
                    
            else: 
                print("Me desculpe, não sei a resposta. I don't know my friend")
                conhecimento.write("\n" + texto)
                respostaUser = input("O que esperava? \n")
                conhecimento.write("\n" + "ChatBot" + respostaUser)
                return "Recebi o conhecimento, Meu Nobre!"
            
def exibeResposta(resposta, nome):
    print(resposta.replace("ChatBot", nome))
    if resposta == "fim":
        return "fim"
    return "continua"



    