import random

def sortearPalavra(listaPalavras):
    """
    Função para sortear uma lista com (palavra,dica e dificuldade) de listaPalavras.

    Args: 
        listaPalavras (list): recebe a lista de palavras para poder sortear.
    """
    numero = 0
    numero = random.randint(0, len(listaPalavras)-1)
    palavraSecreta = listaPalavras[numero]
    return palavraSecreta

def LerArquivo():
    """
        Função para ler o arquivo de palavras

        Returns: 
            dados (list): retorna toda a lista de palavras em uma lista de lista.
    """

    vl = " "
    dados = []
    arquivo = open ("listaPalavras.txt", "r", encoding="utf-8")

    while(vl!=""):
        vl = arquivo.readline()
        if(vl!=""):
            vl = vl.split("|") #separando os campos, nome, dica e dificuldade
            nome = vl[0]
            dica = vl[1]
            dificuldade = vl[2]
            dificuldade = dificuldade.split("\n")[0] #tira o \n no final da linha
            aux = [nome,dica,dificuldade]
            dados.append(aux)
    
    return dados

def esconderPalavra(palavra):
    """
    Função para esconder a palavra secreta.

    Args: 
        palavra (str): recebe a palavra secreta sorteada.

    Returns: 
        palavraEscondida (str): retorna a palavra secreta escondida.
    """
    palavraEscondida = ""
    tamanho = len(palavra)

    palavraEscondida = (tamanho * "_ ")

    return palavraEscondida

def calcularTentativas(palavra, dificuldade):
    """
    Função para Calcular o numero de tentativas baseado em tamanho palavra e dificuldade.

    Args: 
        palavra (str): recebe a palavra secreta sorteada.
        dificuldade (str): recebe a dificuldade estipulada para a palavra.
    Returns: 
        tentativas (int): Retorna o numero de tentativas.
        tentativasMinimas (int): Retorna o numero de Tentativas Minimas Necessarias
    """
    tentativas = 0
    #manda a palavra pra função fazer a lista de lestras (sem repetição)
    letras = listaDeLetras(palavra)

    #tentativas minimas
    tentativasMinimas = len(letras)    

    #adiciona tentativas de acordo com a dificuldade
    if(dificuldade == "Fácil"):
        tentativas = tentativasMinimas + 2
    elif(dificuldade == "Médio"):
        tentativas = tentativasMinimas + 4
    elif(dificuldade == "Difícil"):
        tentativas = tentativasMinimas + 6

    return tentativas, tentativasMinimas

def verificarLetra(palavra, palavraEscondida, acertos, chutes, resposta, pontos):
    """
    Função para verificar se o usuario acertou a letra da palavra.

    Args: 
        palavra (str): palavra q o usuario tem q acertar
        acertos (int): numero de letras acertadas
        chutes (list): lista de letras chutadas
        resposta (str): a resposta do usuario (chute de uma letra q tem na palavra)
    Returns: 
        novaPalavraEscondida (str): nova palavra escondida com as letras amostra
        acertos(int): atualização numero de letras acertadas
        chutes (list): atualização da lista de chutes
    """
    contador = 0
    tamanhoPalavra = len(palavra)
    novaPalavraEscondida = ""
    palavra = palavra.lower()
    acertou = 0
    while(contador<tamanhoPalavra):
        if(palavra[contador] == resposta):
            acertou = 1
            #nova palavra escondida
            novaPalavraEscondida += resposta + " " #adicionando a letra e o espaço entre a proxima
        else:
            novaPalavraEscondida += palavraEscondida[contador * 2] + " " # para gerar a palavra secreta se faz "_ " logo uma letra 'ocupa' 2 indices então fazemos * 2 para compensar
        contador += 1
    if(acertou == 1):
        pontos += 2000
        acertos += 1
    else:
        pontos -= 1500
    chutes.append(resposta)

    return novaPalavraEscondida, acertos, chutes, pontos

def palavraCompleta(palavraEscondida, palavra):
    """
    Função para Verificar se a Palavra foi concluida, todas as letras ja foram desvendadas.

    Args: 
        palavraEscondida (str): recebe a palavraSecreta.
        palavra (str): recebe a palavra sorteada.
    Returns: 
        palavraConcluida (int): retorna a palavra concluida (maneira boleana) se estiver completa retorna 1 senão retorna 0
    """
    contador = 0
    letraAcertada = 0
    palavraConcluida = 0
    #percorre a palavra escondida e verifica quantas letras foram acertadas
    while(contador < len(palavraEscondida)):
        if (palavraEscondida[contador] != " " and palavraEscondida[contador] != "_"):
            letraAcertada += 1   
        contador +=1
    #se for acertada a mesma quantidade de letras da palavra retorna 1 senão 0
    if(letraAcertada == len(palavra)):
        palavraConcluida = 1
    else:
        palavraConcluida = 0

    return palavraConcluida


def listaDeLetras(palavra):
    """
    Função para criar uma lista com as letras da palavra (sem repetição de letras).

    Args: 
        palavra (str): recebe a palavra secreta sorteada.
    Returns: 
        letras (list): Retorna a lista de letras da palavra.
    """
    palavra = palavra.lower()
    contador = 0
    letras = []
    tamanhoPalavra = len(palavra)

    while (contador < tamanhoPalavra):
        contador2 = 0
        existe = 0

        while contador2 < len(letras):
            if palavra[contador] == letras[contador2]:
                existe = 1
                #para loop ja q entrou a letra na lista
                break
            
            contador2 += 1
                
        if(existe == 0):
            letras.append(palavra[contador])

        contador += 1
    
    return letras

def historico(nome,tentativas,pontos,palavra,chutes,acertos,acertou,data):
    """
    Função para Calcular o numero de tentativas baseado em tamanho palavra e dificuldade.

    Args: 
        nome (str): nome do jogador.
        tentativas (int): numero de tentativas restantes.
        pontos (int): quantidade de pontos feitos.
        palavra (str): palavra sorteada.
        chutes (list): letras chutadas.
        acertos (int): quantidades de acertos.
        acertou (str): se acertou a palavra ao final do jogo ('sim!' ou 'não :(' ).
        data (datatime): data e hora em que a pessoa jogou.
        
    Returns: não retorna algo diretamente, a função executada cria um arquivo.txt como forma de historico
    """
    arquivo = open("historico.txt", "a", encoding="utf-8")
    arquivo.write("==================================================================================================================\n")
    arquivo.write(f"  - Jogador: {nome}\n")
    arquivo.write(f"  - Tentativas Restantes: {tentativas}\n")
    arquivo.write(f"  - Pontuação Final: {pontos}\n")
    arquivo.write(f"  - Palavra Secreta: {palavra}\n")
    arquivo.write(f"  - Letras Chutadas: {chutes}\n")
    arquivo.write(f"  - Quantidade de Acertos: {acertos}\n")
    arquivo.write(f"  - Acertou a Palavra?: {acertou}\n")
    arquivo.write(f"  - Data da Partida: {data}\n")
    arquivo.write("==================================================================================================================\n\n")   
    arquivo.close()
