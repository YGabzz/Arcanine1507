import ChatBot as cb

nomeMaquina = "Christofer Nolan"
cb.saudacoes(nomeMaquina)
while True:
    texto = cb.recebeTexto()
    resposta = cb.buscaResposta(nomeMaquina, texto)
    if cb.exibeResposta(resposta, nomeMaquina) == "fim":
        break