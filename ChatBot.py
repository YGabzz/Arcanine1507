def saudacoes_GUI(nome):
    import random
    frases = ["Bom dia, Meu nome é "+ nome +" Como vai voce?", "Olá", "Oi, qual sua pergunta?"]
    print(frases[random.randint(0,2)])

def recebeTexto():
    texto = "Cliente: " + input("Cliente: ")
    palavraProibidas = ["idiota", "burro", "bobão", "canalha"]
    for p in palavraProibidas:
        if p in texto:
            print("IXI RAPA, VEM ME OFENDER NÃO")
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
                    proximaLinha = conhecimento.readline()
                    if "Chatbot: " in proximaLinha:
                        return proximaLinha
            else:
                print("Me desculpe, nao sei oque falar")
                conhecimento.write("\n" + texto)
                respostaUser = input("O que esperava? \n")
                conhecimento.write("\n" + "Chatbot: " + respostaUser)
                return "Obrigado pelo comercimento"
            
def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("ChatBot", nome)


