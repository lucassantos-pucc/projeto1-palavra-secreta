import menus
import funcionalidades
import time
from datetime import datetime

roxo = "\033[35m"   
reset = "\033[0m"

numero = 0
inicioPrograma = 0
inicioJogo = 0
jogar = ""
listaSecreta = []
palavra = ""
tamanhopalavra = 0
dica = ""
tentativas = 0
tentativasMinimas = 0
chutes = []
acertos = 0
dificuldade = ""
palavraEscondida = ""
resposta = ""
letrapalavra = 0
palavraCompleta = 0
nomeJogador = ""
pontos = 0
dataFormatada = ""
acertouPalavra = ""


try:

    # while para logica de começar / terminar jogo
    while(inicioPrograma == 0):
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
            tamanhopalavra = len(palavra)
            
            #calculando quantidade de tentativas
            tentativas, tentativasMinimas = funcionalidades.calcularTentativas(palavra, dificuldade)
            
            #Esconder palavra
            palavraEscondida = funcionalidades.esconderPalavra(palavra)

            time.sleep(0.5)
            #pedindo nome do jogadior para registrar
            menus.identificação()
            nomeJogador = input("Como devo te chamar? ")

            menus.limparTela()
            time.sleep(0.5)
            #mostra as regras basicas para o usuario
            menus.avisoRegras()

            time.sleep(2)
            #input pra parar o programa até o usuario apertar Enter, (tempo para ele ler os avisos etc...)
            input(f"\t\tPreparado {roxo}{nomeJogador}{reset}? Pressione  ENTER para continuar")
            menus.limparTela()

            while(inicioJogo == 0):
                while (tentativas > 0):
                    #menu principal do jogo
                    menus.menu(palavraEscondida, dica, dificuldade, tentativas, tentativasMinimas, chutes, acertos, pontos)

                    #verificação de resposta
                    respostaAceita = 0
                    #só sai do loop se chutar uma letra q n foi chutada
                    while(respostaAceita == 0):
                        resposta = input("Faça seu chute:")
                        #verifica se a resposta ja foi chutada
                        resposta = resposta.lower()
                        contador = 0
                        letraRepetida = 0
                        while(contador< len(chutes)):
                            if(resposta == chutes[contador]):
                                print("Essa letra ja foi chutada!! tente outra Letra!")
                                letraRepetida = 1
                                break
                            else:
                                contador +=1
                        if(letraRepetida == 0):
                            respostaAceita = 1

                    #Saiu do loop, resposta foi aceita!

                    #verifica se acertou a resposta, e atualiza as variaveis
                    palavraEscondida, acertos, chutes, pontos = funcionalidades.verificarLetra(palavra, palavraEscondida, acertos, chutes, resposta, pontos)
                    
                    #verifica se a palavra esta completa
                    palavraCompleta = funcionalidades.palavraCompleta(palavraEscondida, palavra)
                    if(palavraCompleta == 1):
                        menus.limparTela()
                        menus.menu(palavraEscondida, dica, dificuldade, tentativas, tentativasMinimas, chutes, acertos, pontos)
                        inicioJogo = 1
                        break #sai do loop de tentativas
                    else:
                        menus.limparTela()
                        tentativas -= 1
                break
            #pegando data e hora
            data = datetime.now()
            dataFormatada = data.strftime("%d/%m/%Y %H:%M:%S")


            if(palavraCompleta == 1):
                acertouPalavra = "Sim!"
                time.sleep(1)
                menus.limparTela()
                menus.vitoria(palavra, pontos, nomeJogador)
            elif(palavraCompleta == 0):
                acertouPalavra = "Não :("
                time.sleep(1)
                menus.limparTela()
                menus.derrota(palavra, pontos, nomeJogador)
            
            funcionalidades.historico(nomeJogador,tentativas,pontos,palavra,chutes,acertos,acertouPalavra,dataFormatada)
            time.sleep(2)
            menus.despedida()
            
            inicioPrograma = 1
        elif(jogar == "nao"):
            menus.despedida()
            inicioPrograma = 1
        else:
            menus.avisoEntradas()
            time.sleep(2)
except:
    menus.avisoEntradas
    time.sleep(2)