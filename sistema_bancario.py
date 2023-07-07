menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

Selecione uma opção: """

saldo = 0
extrato = ""
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

while True:

    opcao = int(input(f"Seja bem vindo ao Banco 123! {menu}"))
    

    if opcao == 1:
        print("Operação Deposito")
        deposito = float(input("Digite o valor que deseja depositar: "))

        while deposito <= 0:
            deposito = float(input("[ERRO] Valor inválido, selecione um valor postitivo: "))

        saldo += deposito
        extrato += f"Depósito de R$ {deposito:.2f}\n"
        print(f"O depósito de R$ {deposito:.2f} foi realizado com sucesso!")
    
    elif opcao == 2:

        validacao = True
        while validacao == True:
            print("Operação Saque")
            saque = float(input("Digite o valor que deseja sacar: "))
            
            if saque <= 0:
                print("[ERRO] Você inseriu um valor negativo ou igual a 0, tente novamente.")
                validacao = False
                

            elif saque > LIMITE:
                print("[ERRO] Você excedeu o limite de R$ 500.00, tente novamente.")
                validacao = False
                

            elif saque > saldo:
                print("[ERRO] Você não tem saldo suficiente, tente novamente.")
                validacao = False
                
            
            elif numero_saques >= LIMITE_SAQUES:
                print("[ERRO] Você excedeu o limite diário de saques.")
                validacao = False
                
            else:
                saldo -= saque
                numero_saques += 1
                extrato += f"Saque de R$ {saque:.2f}\n"
                print(f"O saque de R$ {saque:.2f} foi realizado com sucesso!")
                validacao = False

    elif opcao == 3:
        print(f"""
Operação Extrato:
{extrato}

Saldo:
R$ {saldo:.2f}
        """)

    elif opcao == 0:
        print("Obrigado por utilizar os nossos serviços!")
        break

    else:
        opcao = int(input(f"[ERRO] Opção inválida! {menu}"))