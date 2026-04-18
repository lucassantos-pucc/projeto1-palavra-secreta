import menus

inicio = 0
jogar = ""

while(inicio == 0):
    menus.recepcao()
    jogar = input()

    if(jogar == "sim"):
        #menus.menu()
        print("vamos jogarrrrr")
        inicio = 1
    elif(jogar == "nao"):
        print("obrigado pela atencao! ate a proxima :)")
        inicio = 1
    else:
        print("por favor! insira da forma correspondente: sim / nao")