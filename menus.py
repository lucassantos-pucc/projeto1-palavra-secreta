import os

# Definição das Cores (Apenas fonte)
amarelo = "\033[33m"
vermelho = "\033[31m"
verde = "\033[32m"
azul = "\033[96m"
reset = "\033[0m"
roxo = "\033[35m"    




def limparTela():
    os.system('cls' if os.name == 'nt' else 'clear')

def recepcao():
    """
    Função para exibir a recepção do jogo.
    """
    print(f"{amarelo}==========================================================================================={reset}")
    print(f"{vermelho}\t\t\tSEJA BEM-VINDO AO JOGO DA PALAVRA ESCONDIDA!{reset}")
    print(f"{amarelo}-------------------------------------------------------------------------------------------{reset}")
    print(f"\t\t   Neste jogo, você vai se divertir enquanto exercita a mente.")
    print(f"\tA cada rodada, as pistas ajudam a desenvolver o raciocínio lógico, a atenção e a criatividade.")
    print(f"\t  Ao tentar descobrir a palavra escondida, você melhora sua linguagem, amplia o vocabulário")
    print(f"\t\t\t e pratica a leitura de forma leve e natural.")
    print(f"\t\tBrincar de adivinhar palavras é uma forma simples e divertida de aprender.")
    print(f"\t    Cada desafio é uma oportunidade de pensar, imaginar e explorar novas possibilidades.")
    print(f"\n{azul}\t\t      O tema deste jogo é: {amarelo}Personagens do Jogo Stardew Valley{reset}")
    print(f"\t\t\t  Será que você consegue adivinhar o personagem?")
    print(f"\t\t\t\tGostaria de jogar? {verde}sim{reset}/{vermelho}nao{reset}")
    print(f"{amarelo}==========================================================================================={reset}")

def avisoEntradas():
    print(f"{amarelo}==========================================================================================={reset}")
    print(f"{vermelho}\t\t\t\t   ATENÇÃO!{reset}")
    print(f"{amarelo}-------------------------------------------------------------------------------------------{reset}")
    print(f"\t\t\tparece que ocorreu um erro !\n \t\t\tPor favor, insira os valores da forma correta.")
    print(f"\t\tDigite apenas o que foi solicitado para continuar o jogo.")
    print(f"{amarelo}==========================================================================================={reset}")


def avisoRegras():
    """
    Função para exibir aviso de como funcionara as entradas do jogo  e as suas regras para o jogador.
    """
    print(f"{amarelo}==========================================================================================={reset}")
    print(f"{vermelho}\t\t\t\t     AVISO IMPORTANTE!{reset}")
    print(f"{amarelo}-------------------------------------------------------------------------------------------{reset}")
    print(f"\tAntes de começar, fique atento: este jogo aceita apenas {vermelho}*uma letra por vez*.") 
    print(f"s{vermelho}Se você digitar mais de um caractere, a tentativa será contabilizada e considerada incorreta.")
    print(f"\n{azul}\t\t      TEMA: {amarelo}Personagens de Stardew Valley{reset}")
    print(f"\n\t\t\tCOMO FUNCIONA O JOGO?")
    print(f"\tO computador escolherá aleatoriamente um personagem de Stardew Valley, junto com uma dica.")
    print(f"\tAlgumas letras do nome do personagem podem já aparecer para te ajudar no início.")
    print(f"\tSeu objetivo é descobrir qual personagem está escondido, tentando uma letra por vez.")
    print(f"\n\t\t\tREGRAS DO DESAFIO:")
    print(f"\t- Letras corretas que fazem parte do nome do personagem somam pontos.")
    print(f"\t- Letras que não existem no nome fazem você perder pontos.")
    print(f"\t- O número de tentativas é limitado, então pense bem antes de escolher!")
    print(f"\t- O jogo termina se suas tentativas acabarem.")
    print(f"\t- Se você descobrir o personagem antes disso, você vence!")
    print(f"\n\t\t\tACOMPANHE SEU DESEMPENHO:")
    print(f"\tDurante o jogo, você poderá ver quantos acertos, erros e tentativas ainda restam.")
    print(f"\n\t\t\tREGISTRO DAS PARTIDAS:")
    print(f"\tAo final, seus resultados serão salvos, incluindo:")
    print(f"\tData, nome do jogador, pontuação, número de tentativas e o personagem descoberto.")
    print(f"\n\tPrepare-se para testar seus conhecimentos sobre Stardew Valley!")
    print(f"\tBoa sorte e divirta-se tentando descobrir o personagem escondido!")
    print(f"{amarelo}==========================================================================================={reset}")

def menu(palavraEscondida, dica, dificuldade, tentativas, tentativasMinimas, chutes, acertos, pontos):
    """
    Função para exibir o menu do jogo com arte ASCII.

    Args: 
        palavraEscondida (str): palavra escondida q o usuario vai adivinhar.
        dica (str): a dica da palavra escondida.
        dificuldade (str): nivel de dificuldade da palavra (facil, medio, dificil)
        tentativas (int): numero de tentativas maximas para acertar.
        chutes (str): letras chutadas.
        acertos (int): numero de acertps feitos.
    
    Returns:
        retorna o menu com os itens inseridos
    """
    # Variável para controlar o espaçamento interno do menu
    espaco = 85
    print(fr"{amarelo} ____________________________________________________________________________________________________________________________ {reset}")
    print(fr"{amarelo}/                                                                                                                            \ {reset}")
    print(fr"{amarelo}|                                                                                                                            | {reset}")
    print(fr"{amarelo}|                         ,---.     ,--.,--.          ,--.        ,--.                                                       | {reset}")
    print(fr"{amarelo}|                        /  O  \  ,-|  |`--',--.  ,--.`--',--,--, |  ,---.  ,---.      ,---.                                 | {reset}")
    print(fr"{amarelo}|                       |  .-.  |' .-. |,--. \  `'  / ,--.|      \|  .-.  || .-. :    | .-. |                                | {reset}")
    print(fr"{amarelo}|                       |  | |  |\ `-' ||  |  \    /  |  ||  ||  ||  | |  |\   --.    ' '-' '                                | {reset}")
    print(fr"{amarelo}|            ,------.    `--' `--' `---' `--'   `--'   `--'`--''--'`--' `--' `----'    `---'      ,--.                       | {reset}")
    print(fr"{amarelo}|            |  .--. ' ,---. ,--.--. ,---.  ,---. ,--,--,  ,--,--. ,---.  ,---. ,--,--,---.     ,-|  | ,---.                 | {reset}")
    print(fr"{amarelo}|            |  '--' || .-. :|  .--'(  .-' | .-. ||      \\' ,-.  || .-. || .-. :|        |    ' .-. || .-. :                | {reset}")
    print(fr"{amarelo}|            |  | --' \   --.|  |   .-'  `)' '-' '|  ||  |\  '-'  |' '-''\\  --. |  |  |  |    \ `-' |\   --.                | {reset}")
    print(fr"{amarelo}|            `--'      `----'`--'   `----'  `---' `--''--' `--`--' .`-  /  `----'`--`--`--'      `---'  `----'               | {reset}")
    print(fr"{amarelo}|                                                                  `---'                                                     | {reset}")
    print(fr"{amarelo}|{vermelho}    ,---. ,--------. ,---.  ,------. ,------.  ,------.,--.   ,--.    ,--.   ,--.,---.  ,--.   ,--.   ,------.,--.   ,--.  {amarelo} | {reset}")
    print(fr"{amarelo}|{vermelho}   '  .-''--.  .--'/   O  \ |  .--. '|  .-.  \ |  .---'|  |   |  |     \  `.'  //  O  \ |  |   |  |   |  .---' \  `.'  /   {amarelo} | {reset}")
    print(fr"{amarelo}|{vermelho}   `.  `-.   |  |  |  .-.  ||  '--'.'|  |  \  :|  `--, |  |.'.|  |      \     /|  .-.  ||  |   |  |   |  `--,   '.    /    {amarelo} | {reset}")
    print(fr"{amarelo}|{vermelho}   .-'    |  |  |  |  | |  ||  |\  \ |  '--'  /|  `---.|   ,'.   |       \   / |  | |  ||  '--.|  '--.|  `---.    |  |     {amarelo} | {reset}")
    print(fr"{amarelo}|{vermelho}   `-----'   `--'  `--' `--'`--' '--'`-------' `------''--'   '--'        `-'  `--' `--'`-----'`-----'`------'    `--'     {amarelo} | {reset}")
    print(fr"{amarelo}|                                                                                                                            |{reset}")
    print(fr"{amarelo}\____________________________________________________________________________________________________________________________/{reset}")
    print(fr"{amarelo}       |   |                                                                                                      |   | {reset}")
    print(fr"{amarelo}       |   |                                                                                                      |   | {reset}")
    print(fr"{amarelo}       |   |                               {azul}Personagem: {reset}{palavraEscondida.upper():<{espaco - 27}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                               {azul}Dica: {reset}{dica:<{espaco - 21}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                               {azul}Dificuldade: {reset}{dificuldade:<{espaco - 28}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                               {azul}Tentativas Minimas: {reset}{str(tentativasMinimas):<{espaco - 35}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                                                                                                      |   | {reset}")
    print(fr"{amarelo}       |   |                               {azul}Tentativas restantes: {reset}{str(tentativas):<{espaco - 37}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                               {azul}Letras chutadas: {reset}{str(chutes).upper():<{espaco - 32}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                               {azul}Acertos: {reset}{str(acertos):<{espaco - 24}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                               {azul}Pontos : {amarelo}{str(pontos):<{espaco - 24}} |   | {reset}")
    print(fr"{amarelo}       |   |                                                                                                      |   | {reset}")
    print(fr"{amarelo}       |   |                                                                                                      |   | {reset}")
    print(fr"{verde}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ {reset}")
    print(fr"{verde}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ {reset}")

def identificação():
    print(f"{amarelo}==========================================================================================={reset}")
    print(f"{azul}\t\t\t\t   IDENTIFICAÇÃO DO JOGADOR{reset}")
    print(f"{amarelo}-------------------------------------------------------------------------------------------{reset}")
    print(f"\tAntes de começar, digite seu nome para registrarmos sua partida.")
    print(f"\tIsso permitirá salvar sua pontuação e gerar um histórico no arquivo.txt.")
    print(f"{amarelo}==========================================================================================={reset}")

def vitoria(palavra, pontos, jogador):
    print(f"{amarelo}==========================================================================================={reset}")
    print(f"{verde}\t\t\t\t   PARABÉNS! {roxo}{jogador}{reset}")
    print(f"{amarelo}-------------------------------------------------------------------------------------------{reset}")
    print(f"\tVocê acertou! A palavra era: {azul}{palavra}{reset}")
    print(f"\tMandou muito bem!")
    print(f"\tSua pontuação foi de {verde}{pontos} {reset}")
    print(f"\n\tPara ver o histórico das suas partidas,")
    print(f"\tabra o arquivo.txt e confira seus resultados.")
    print(f"{amarelo}==========================================================================================={reset}")

def derrota(palavra, pontos, jogador):
    print(f"{amarelo}==========================================================================================={reset}")
    print(f"{vermelho}\t\t\t\t   QUE PENA {roxo}{jogador}{reset}")
    print(f"{amarelo}-------------------------------------------------------------------------------------------{reset}")
    print(f"\tA palavra era: {azul}{palavra}{reset}")
    print(f"\tMais sorte da próxima vez!")
    print(f"\tSua pontuação foi de {vermelho} {pontos} {reset}")
    print(f"\n\tSe quiser ver o histórico de partidas,")
    print(f"\tabra o arquivo.txt para verificar suas respostas.")
    print(f"{amarelo}==========================================================================================={reset}")

def despedida():
    """
    Função simples se despedindo do jogador.
    """
    print(f"{amarelo}==========================================================================================={reset}")
    print(f"{verde}\t\t      Obrigado pela sua atenção!{reset}")
    print(f"{azul}\t\t      Até a próxima, agricultor! :){reset}")
    print(f"{amarelo}==========================================================================================={reset}")