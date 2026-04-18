def menu():
    print(f"\n-----------------Progama de Leitura das pressões hidrodinâmicas-----------------\nDeseja iniciar o programa?\n1-Para iniciar\n2-Para fechar")
    inicio=int(input(f"\n--> Digite aqui o comando desejado: "))
    match inicio:
        case 1:
            return True
        case 2:
            print(f"\nFechando programa...")
            return False
        case _:
            print(f"\n!!!!Comando inválido!!!!\nRetornando ao início...")
            return menu()
rodando=menu()

while rodando:
    travou=False
    numh=0
    soma=0
    contvermelho=0
    contverde=0
    leituras=1
    print(f"--------------------------------------------------------------------------------")
    numh=int(input("\n~ Quantidade de leituras que serão realizadas no seu turno: "))
    for i in range(1,numh+1):
        upc=float(input("\n- Valor da pressão hidrodinâmica: "))
        if upc>150:
            upc=upc*(108/100)
        else:
            upc=upc*(96/100)
        if i==1:
            maior=upc
            menor=upc
        if 120<=upc<=180:
            zona=(f"\n--> {upc:.2f} UPC está na Zona Verde(Estável)")
            print(zona)
            print(f"--------------------------------------------------------------------------------")
            contverde+=1
            if upc>maior:
                maior=upc
            if upc<menor:
                menor=upc
        elif upc>250:
            zona=(f"\n--> {upc:.2f} UPC está na Zona Vermelha(Crítica)")
            print(zona)
            print(f"--------------------------------------------------------------------------------")
            if upc>maior:
                maior=upc
            if upc<menor:
                menor=upc
        else:
            zona=(f"\n--> {upc:.2f} UPC está na Zona Amarela(Oscilação)")
            print(zona)
            print(f"--------------------------------------------------------------------------------")
            if upc>maior:
                maior=upc
            if upc<menor:
                menor=upc
        
        if zona==(f"\n--> {upc:.2f} UPC está na Zona Vermelha(Crítica)"):
            contvermelho+=1
        else:
            contvermelho=0
        leituras+=1
        soma+=upc
        if contvermelho==2:
            print(f"\nInterrupção do escoamento por motivos de segurança")
            rodando=False
            travou=True
            break
        
        rodando=False
        porcentagem=(contverde/numh)*100
        porcentagem2=(leituras/numh)*100

    media=soma/numh
    print(f"------------------------------Relatório-----------------------------------------")
    print(f"\n-->A média das pressões ajustadas: {media:.2f}")
    print(f"\n-->A menor pressão registrada foi: {menor:.2f}")
    print(f"\n-->Porcentagem de leituras que ficaram na Zona Verde foi: {porcentagem:.2f}%")
    if travou:
        print(f"\n-->Porcentagem de leituras realizadas antes do travamendo do Escoamento foi: {porcentagem2}%")
