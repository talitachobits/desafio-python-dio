def menu():
  menu = """\n
     ================ MENU ================
     [1] Depositar
     [2] Sacar
     [3] Extrato 
     [4] Novo usuário     
     [5] Nova conta     
     [6] Listar contas
     [0] Sair 
   => """
  return input(menu)

def depositar(saldo, valor, extrato, /):  
  if valor > 0:
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    print("Déposito realizado com sucesso.")
  else:
    print("Operação não realizada! O valor informado não é válido.")
    
  return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):  
  if valor > saldo:
    print("Operação não realizada! Não há saldo suficiente.")    
  elif valor > limite:
    print("Operação não realizada! O valor a ser sacado excede o limite.")        
  elif numero_saques >= limite_saques:        
    print("Operação não realizada! Número máximo de saques foi excedido.")    
  elif valor > 0:
    saldo -= valor       
    extrato += f"Saque: R$ {valor:.2f}\n"       
    numero_saques += 1 
    print("Saque realizado com sucesso.") 
  else:         
    print("Operação não realizada! O valor informado é inválido.") 
    
  return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
  print("\n================ EXTRATO ================")      
  print("Sem movimentações na conta." if not extrato else extrato)      
  print(f"\nSaldo: R$ {saldo:.2f}")        
  print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com este CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, conta não criada!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Insira o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Insira o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("Sistema finalizado.")
            break

        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")

main()



  
