import textwrap
def menu():
    menu = '''\n
    =======================MENU=======================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [c]\tCriar conta
    [nu]\tNovo Usuário
    [lc]\tListar contas
    [q]\tsair
    
    '''
    return input(textwrap.dedent(menu))

def depositar (saldo, valor, extrato, /): #chamada por posição ("/")
    if valor > 0: # deposito de valor postivo
        saldo+=valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n Depósito realizado com sucesso!!!")
    else:
        print('\n==Operação falhou! Valor informado inválido!')
        
    return saldo, extrato
    
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):#argumentos nomeados
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques
    
    if excedeu_saldo:
        print("Operação falhou! Saldo insuficiente...")
    elif excedeu_limite:
        print('Operação falhou!Limite insuficiente...')
    elif excedeu_saques:
        print('Operação falhou! Limite diário de saques excedido...')
        
    elif valor > 0:
        
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n Saque realizado com sucesso!")
    
    else:
        print("\n Valor informado inválido...")
    
def exibir_extrato (saldo, /, *, extrato):
    
    print("\n=======================EXTRATO=======================")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo: \t\tR$ {saldo:.2f}") #\t = tabulação
    print("========================================================")
    
def criar_usuario(usuarios):
    
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("Já existe usuário com esse CPF...")
        return
    
    nome=input("Nome completo: ")
    data_nascimento= input("Data nascimento (DD/MM/AAAA): ")
    endereco = input("Endereco completo: ")
    
    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco":endereco})
    print("Usuário cadastrado com sucesso!!")
    
def filtrar_usuarios(cpf, usuarios):
    
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] #compressão de listas
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta,usuarios):
    cpf = input("CPF: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("\n====Conta criada com sucesso!====")
        return {'agencia': agencia, 'numero_conta':numero_conta, 'usuario':usuario}
    
    print("Usuario não encontrado, fluxo de criação de conta encerrada...")
    
def listar_contas(contas):
    for conta in contas:
        linha = f'''
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        '''
        print("="*100)
        print(textwrap.dedent(linha))
        
        
        
def main():
    
    LIMITE_SAQUES = 3 #constantes
    AGENCIA = "0001" #constantes
 
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato) #função retorna saldo e extrato

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato) #receber argumentos de forma posicional e nomeada

        elif opcao == "nu":
            criar_usuario(usuarios) #usuarios = litsta usuarios

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
main ()   