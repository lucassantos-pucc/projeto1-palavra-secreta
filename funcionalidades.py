import listaPalavras
import random

def sortearPalavra():
    """
    Função para sortear uma lista com (palavra,dica e dificuldade) de listaPalavras.
    """
    numero = 0
    numero = random.randint(0, 29)
    palavraSecreta = listaPalavras.palavras[numero]
    return palavraSecreta

def esconderPalavra(palavra):
    """
    Função para esconder a palavra secreta.

    Args: recebe a palavra secreta sorteada
    returns: retorna a palavra secreta escondida
    """
    palavraEscondida = ""
    tamanho = len(palavra)

    palavraEscondida = (tamanho * "_ ")

    return palavraEscondida

