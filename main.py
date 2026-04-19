import menus
import funcionalidades
import time

numero = 0
inicio = 0
jogar = ""
listaSecreta = []
palavra = ""
dica = ""
tentativas = 0
chutes = ""
acertos = 0
dificuldade = ""
palavraEscondida = ""
resposta = ""

# while para logica de começar / terminar jogo
while(inicio == 0):
    menus.limparTela()
    menus.recepcao()

    #input para saber se o jogador vai jogar ou não
    jogar = input()

    if(jogar == "sim"):
        menus.limparTela()
        listaSecreta = funcionalidades.sortearPalavra()

        #definindo palavra secreta, dica e dificuldade
        palavra = listaSecreta[0]
        dica = listaSecreta[1]
        dificuldade = listaSecreta[2]
        
        #Esconder palavra
        palavraEscondida = funcionalidades.esconderPalavra(palavra)

        #mostra as regras basicas para o usuario
        menus.avisoRegras()

        #input pra parar o programa até o usuario apertar Enter, (tempo para ele ler os avisos etc...)
        input("\tPreparado? Pressione  ENTER para continuar")

        #menu principal do jogo
        menus.menu(palavraEscondida, dica, dificuldade, tentativas, chutes, acertos)
        
        inicio = 1
    elif(jogar == "nao"):
        menus.despedida()
        inicio = 1
    else:
        menus.avisoEntradas()
        time.sleep(2)