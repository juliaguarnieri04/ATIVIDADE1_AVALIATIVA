def barra_progresso_simples(mensagem):
    print(f"\n{mensagem}")
    for i in range(1, 11):
        barra = "█" * i + "-" * (10 - i)
        print(f"  [{barra}] {i*10}%", end="\r")
        for _ in range(5000000): 
            pass
    print("\n" + "-" * 70)

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
            barra_progresso_simples("Sincronizando com os sensores da Unidade Delta-9...")
            return True
        case 2:
            print(f"\nEncerrando o SEUC-4. Até o próximo turno!")
            return False
        case 3:
            print(f"\nJúlia Andrade Guarnieri\nLarissa Souza Quito Sampaio\nPedro Henrique Sanches Agatti Godoy")
            input(f"\nPressione qualquer tecla para retornar ao menu...")
            return menu()
        case _:
            print(f"\n!!!! Comando inválido !!!!\nRetornando ao menu...")
            return menu()

def iniciar_turno():
    print("\n" + "-" * 70)
    numh = int(input("\n~ Quantidade de leituras que serão realizadas no seu turno: "))

    if numh <= 0 :
        print("\n !!! Número de leitura deve ser maior que zero !!!")
        return
    
    soma = 0
    travou = False
    contvermelho = 0
    contverde = 0
    leituras = 0
    menor = None
    maior = None
    anterior = None
    contbaixa = 0

    print("\n" + "-" * 70)
    print(f"  {'Nº':>5}  | {'Pressão Ajustada':>15} | {'Classificação'}")
    print("-" * 70)
    
    for i in range(1, numh + 1):
        upc_bruta = float(input(f"\n  Pressão hidrodinâmica (leitura {i}/{numh}): "))

        if upc_bruta > 150:
            upc = upc_bruta * 1.08
        else:
            upc = upc_bruta * 0.96
        
        if i == 1:
            maior = upc
            menor = upc
        
        if upc > maior:
            maior = upc

        if upc < menor:
            menor = upc
        
        if 120 <= upc <= 180:
            zona = "VERDE"
            print(f"  Leitura {i:>3} | {upc:>8.2f} UPC | Zona VERDE  (Estável)")
        elif upc < 120 or (180 < upc <= 250):       
            zona = "AMARELA"
            print(f"  Leitura {i:>3} | {upc:>8.2f} UPC | Zona AMARELA  (Oscilação)")
        else:
            zona = "VERMELHA"
            print(f"  Leitura {i:>3} | {upc:>8.2f} UPC | Zona VERMELHA (Crítica)")
        
        if anterior != None:
            if upc > anterior:
                print("   ↑ Pressão subindo")
            elif upc < anterior:
                print("   ↓ Pressão caindo")
            else:
                print("   → Pressão estável")
        anterior = upc

        if zona == "VERDE":
            contverde += 1

        if zona == "VERMELHA":
            contvermelho += 1
        else:
            contvermelho = 0  
        
        if upc < 120:
            contbaixa += 1
        else:
            contbaixa = 0
        
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
        if contbaixa == 2:
            print("\n" + "!" * 70)
            print("  *** PROTOCOLO DE TRAVAMENTO ATIVADO ***")
            print("  Duas leituras consecutivas abaixo de 120 UPC detectadas.")
            print("  Risco de cristalização do fluido.")
            print("  Escoamento interrompido imediatamente por segurança.")
            print("!" * 70)
            travou = True
            break
    
    barra_progresso_simples("Compilando dados e gerando relatório final...")
    variacao = maior - menor
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

    pct_realizadas = (leituras / numh) * 100

    print(f"  Leituras previstas          : {numh}")
    print(f"  Leituras realizadas         : {leituras} ({pct_realizadas:.2f}%)")
    print(f"  Média das pressões ajustadas: {media:.2f} UPC")
    print(f"  Menor pressão registrada    : {menor:.2f} UPC")
    print(f"  Maior pressão registrada    : {maior:.2f} UPC")
    print(f"  Leituras na Zona Verde      : {contverde} ({pct_verde:.2f}%)")
    print(f"  Variação de pressão         : {variacao:.2f} UPC")

    if pct_verde >= 70:
        print("  Status geral                : Sistema estável")
    elif pct_verde >= 40:
        print("  Status geral                : Sistema em atenção")
    else:
        print("  Status geral                : Sistema crítico")

    if travou:
        risco = "ALTO"
    elif pct_verde < 50:
        risco = "MÉDIO"
    else:
        risco = "BAIXO"
    

    print(f"  Nível de risco final        : {risco}")


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
