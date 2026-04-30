def menu():
    print("\n" +"-" * 70)
    print("SEUC-4 — Sistema de Escoamento de Unidades de Carga")
    print("Refinaria Delta-9") 
    print("=" * 70)
    print("\nDeseja iniciar o programa?")
    print("  1 - Iniciar novo turno")
    print("  2 - Encerrar sistema")
    print("  3 - Sobre os desenvolvedores")
    print("-" * 70)

    inicio = int(input("--> Digite o comando desejado: "))
    match inicio:
        case 1:
            return True
        case 2:
            print(f"\nEncerrando o SEUC-4. Até o próximo turno!")
            return False
        case 3:
            print(f"\nJúlia Andrade Guarnieri\nLarissa Souza Quito Sampaio\nPedro Henrique Sanches Agatti Godoy\nThomas Krause Arena")
            retornar = input(f"\nDigite qualquer coisa pra retornar ao menu:    ")
            match retornar:
                case _:
                    return menu()
        case _:
            print(f"\n!!!!Comando inválido!!!!\nRetornando ao menu...")
            return menu()


def iniciar_turno():
    print("\n" + "-" * 70)
    numh=int(input("\n~ Quantidade de leituras que serão realizadas no seu turno: "))

    if numh <= 0 :
        print("\n !!! Número de leitura deve ser maior que zero !!!")
        return
    
    soma= 0
    travou= False
    contvermelho=0
    contverde=0
    leituras=0
    menor = None
    maior = None

    print("\n" + "-" * 70)
    print(f"  {'Nº':>5}  | {'Pressão Ajustada':>15} | {'Classificação'}")
    print("-" * 70)
    
    for i in range(1,numh + 1):
        upc_bruta = float(input(f"\n  Pressão hidrodinâmica (leitura {i}/{numh}): "))

        if upc_bruta > 150:
            upc= upc_bruta * 1.08
        else:
            upc=upc_bruta * 0.96

        if i == 1:
            maior = upc
            menor = upc
        
        if upc > maior:
            maior=upc

        if upc < menor:
            menor=upc
        
        if 120 <= upc <= 180:
            zona = "VERDE"
            print(f"  Leitura {i:>3} | {upc:>8.2f} UPC | Zona VERDE  (Estável)")
        elif 180 < upc <=250:        
            zona = "AMARELA"
            print(f"  Leitura {i:>3} | {upc:>8.2f} UPC | Zona AMARELA  (Oscilação)")
        elif upc > 250:
            zona = "VERMELHA"
            print(f"  Leitura {i:>3} | {upc:>8.2f} UPC | Zona VERMELHA (Crítica)")
        else:
            zona = "ABAIXO DO LIMITE"
            print(f"  Leitura {i:>3} | {upc:>8.2f} UPC | Zona: ABAIXO DO LIMITE")

        if zona == "VERDE":
            contverde += 1

        if zona == "VERMELHA":
            contvermelho += 1
        else:
            contvermelho = 0  
        
        leituras += 1
        soma += upc      

        if contvermelho == 2:
            print("\n" + "!" * 70)
            print("  *** PROTOCOLO DE TRAVAMENTO ATIVADO ***")
            print("  Duas leituras consecutivas na Zona Vermelha detectadas.")
            print("  Escoamento interrompido imediatamente por segurança.")
            print("!" * 70)
            travou = True
            break
    
    if leituras > 0:
        media = soma / leituras
        pct_verde = (contverde / leituras) * 100
    else:
        media = 0
        pct_verde = 0
    
    pct_travamento = (leituras / numh) * 100        
    
    print("\n" + "=" * 70)
    print("RELATÓRIO DO TURNO — SEUC-4")
    print("=" * 70)
    print(f"  Leituras previstas          : {numh}")
    print(f"  Leituras realizadas         : {leituras}")
    print(f"  Média das pressões ajustadas: {media:.2f} UPC")
    print(f"  Menor pressão registrada    : {menor:.2f} UPC")
    print(f"  Maior pressão registrada    : {maior:.2f} UPC")
    print(f"  Leituras na Zona Verde      : {contverde} ({pct_verde:.2f}%)")
    
    if travou:
        print(f"\n [TRAVAMENTO] Percentual de leituras realizadas antes do travamento: {pct_travamento:.2f}%")
        print("  O turno foi encerrado devido ao protocolo de segurança.")
    else:
        print("\n  O turno foi concluído sem incidentes de segurança.")
    
    print("\n" + "=" * 70)

rodando = menu()

while rodando:
    iniciar_turno()
    rodando = menu()