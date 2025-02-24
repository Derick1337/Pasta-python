Empresas=['ALB','MM','CZB']
Porcentagens=[10,8,5]
Usuário=[]
Saldo_de_um_Usuário=[]
while True:
    print('Escolha a opção:\n1-Cadastrar_empresa\n2-Cadastrar_Usuário\n3-Registrar_Compra_de_um_Usuário\n4-Mostrar_Saldo_de_um_Usuário\n5-Resgatar_Saldo_de_um_Usuário\n6-Excluir_Empresa\n0-Sair')
    try:
        NumOpção=int(input('Escolha a opção :'))
        if NumOpção == 1 :
            idEmpresa, Percentagem_Disponível=input('Empresa e Porcentagem Disponível:').split()
            idEmpresa=idEmpresa.upper()
            Percentagem_Disponível=int(Percentagem_Disponível)
            Empresas.append(idEmpresa)
            Porcentagens.append(Percentagem_Disponível)
        elif NumOpção == 2 :
            CadastrodeUsuário, valor=input('Cadastro de Usuário e Saldo Requerido:').split()
            CadastrodeUsuário=CadastrodeUsuário.upper()
            valor=int(valor)
            Usuário.append(CadastrodeUsuário)
            Saldo_de_um_Usuário.append(valor)
        elif NumOpção == 3:
            id_usuario = input('ID do usuário: ').upper()
            valor_compra = float(input('Valor da compra: '))
            id_empresa = input('ID da empresa: ').upper()

            if id_usuario in Usuário and id_empresa in Empresas:
                indice_empresa = Empresas.index(id_empresa)
                desconto = valor_compra * (Porcentagens[indice_empresa] / 100)
                indice_usuario = Usuário.index(id_usuario)
                Saldo_de_um_Usuário[indice_usuario] += desconto
                print('Compra registrada')
            else:
                print('Usuário ou empresa não cadastrados.')
        elif NumOpção == 4:
            id_usuario = input('ID do usuário: ').upper()
            if id_usuario in Usuário:
                indice_usuario = Usuário.index(id_usuario)
                saldo = Saldo_de_um_Usuário[indice_usuario]
                print('Saldo do usuário:', saldo)
            else:
                print('Usuário não cadastrado.')
        elif NumOpção == 5:
            idUsuário=input('idUsuário :')
            idUsuário= idUsuário.upper()
            if idUsuário in list(Usuário):
                índice=Usuário.index(idUsuário)
                Saldo_Mostra=Porcentagens[índice]
                subtração=int(input('Subtração :'))
                item=Saldo_de_um_Usuário[índice]
                Minuendo=item-subtração
                if Minuendo < Saldo_de_um_Usuário[índice]:
                        Saldo_de_um_Usuário[índice] = Minuendo
                elif Minuendo > Saldo_de_um_Usuário[índice]:
                    print('Error 404')
                else:
                    Saldo_de_um_Usuário[índice] = Minuendo
            elif idUsuário not in list(Usuário):
                print('Error')
        elif NumOpção == 6:
                idEmpresa = input('idEmpresa :')
                idEmpresa= idEmpresa.upper()
                if idEmpresa in Empresas:
                    Escolha= input('Deseja Mesmo excluir a empresa :')
                    Escolha=Escolha.upper()
                    if Escolha == 'SIM': 
                        índice=Empresas.index(idEmpresa)
                        Empresas.pop(índice)
                        Porcentagens.pop(índice)
                        print('ok')
                    else:
                        print('Que bom')
                elif idEmpresa not in list(Empresas):
                    print('Error') 
        elif NumOpção == 0:
            print('Thank You')
    except EOFError:
         break