# Definição das Cores (Apenas fonte)
amarelo = "\033[33m"
vermelho = "\033[31m"
verde = "\033[32m"
azul = "\033[96m"
reset = "\033[0m"

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


def menu(palavraSecreta, dica, tentativas, chutes, acertos):
    """
    Função para exibir o menu do jogo com arte ASCII.
    """
    # Variável para controlar o espaçamento interno do menu
    espaco = 85
    print(fr"{amarelo} ____________________________________________________________________________________________________________________________ {reset}")
    print(fr"{amarelo}/                                                                                                                            \ {reset}")
    print(fr"{amarelo}|                                                                                                                            | {reset}")
    print(fr"{amarelo}|                         ,---.      ,--.,--.          ,--.        ,--.                                                   | {reset}")
    print(fr"{amarelo}|                        /  O  \  ,-|  |`--',--.  ,--.`--',--,--, |  ,---.  ,---.      ,---.                                 | {reset}")
    print(fr"{amarelo}|                       |  .-.  |' .-. |,--. \  `'  / ,--.|      \|  .-.  || .-. :    | .-. |                                | {reset}")
    print(fr"{amarelo}|                       |  | |  |\ `-' ||  |  \    /  |  ||  ||  ||  | |  |\   --.    ' '-' '                                | {reset}")
    print(fr"{amarelo}|            ,------.    `--' `--' `---' `--'   `--'   `--'`--''--'`--' `--' `----'     `---'     ,--.                         | {reset}")
    print(fr"{amarelo}|            |  .--. ' ,---. ,--.--. ,---.  ,---. ,--,--,  ,--,--. ,---.  ,---. ,--,--,---.     ,-|  | ,---.                  | {reset}")
    print(fr"{amarelo}|            |  '--' || .-. :|  .--'(  .-' | .-. ||      \\' ,-.  || .-. || .-. :|        |    ' .-. || .-. :                 | {reset}")
    print(fr"{amarelo}|            |  | --' \   --.|  |   .-'  `)' '-' '|  ||  |\ '-'  |' '-' '\\   --.|  |  |  |    \ `-' |\   --.                 | {reset}")
    print(fr"{amarelo}|            `--'      `----'`--'   `----'  `---' `--''--' `--`--'.`-  /  `----'`--`--`--'     `---'  `----'                 | {reset}")
    print(fr"{amarelo}|                                                                `---'                                                       | {reset}")
    print(fr"{amarelo}|{vermelho}    ,---. ,--------. ,---.  ,------. ,------.  ,------.,--.   ,--.    ,--.   ,--.,---.  ,--.   ,--.   ,------.,--.   ,--.  {amarelo} | {reset}")
    print(fr"{amarelo}|{vermelho}   '  .-''--.  .--'/  O  \ |  .--. '|  .-.  \ |  .---'|  |   |  |     \  `.'  //  O  \ |  |   |  |   |  .---' \  `.'  /   {amarelo} | {reset}")
    print(fr"{amarelo}|{vermelho}   `.  `-.   |  |  |  .-.  ||  '--'.'|  |  \  :|  `--, |  |.'.|  |      \    /|  .-.  ||  |   |  |   |  `--,   '.    /     {amarelo} | {reset}")
    print(fr"{amarelo}|{vermelho}   .-'    |  |  |  |  | |  ||  |\  \ |  '--'  /|  `---.|  ,'.   |       \\  / |  | |  ||  '--.|  '--.|  `---.    |  |      {amarelo} | {reset}")
    print(fr"{amarelo}|{vermelho}   `-----'   `--'  `--' `--'`--' '--'`-------' `------''--'   '--'        `-'  `--' `--'`-----'`-----'`------'    `--'      {amarelo} | {reset}")
    print(fr"{amarelo}|                                                                                                                            |{reset}")
    print(fr"{amarelo}\____________________________________________________________________________________________________________________________/{reset}")
    print(fr"{amarelo}       |   |                                                                           |   | {reset}")
    print(fr"{amarelo}       |   |                                                                           |   | {reset}")
    print(fr"{amarelo}       |   |                                        {azul}personagem: {palavraSecreta:<{espaco - 36}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                                        {azul}dica: {dica:<{espaco - 30}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                                                                           |   | {reset}")
    print(fr"{amarelo}       |   |                                        {azul}tentativas: {str(tentativas):<{espaco - 36}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                                        {azul}letras chutadas: {str(chutes):<{espaco - 41}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                                        {azul}acertos: {str(acertos):<{espaco - 33}} {amarelo}|   | {reset}")
    print(fr"{amarelo}       |   |                                                                           |   | {reset}")
    print(fr"{amarelo}       |   |                                                                           |   | {reset}")
    
    # Grama
    print(fr"{verde}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ {reset}")
    print(fr"{verde}^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ {reset}")
