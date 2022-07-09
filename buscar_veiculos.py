from PyQt5 import QtWidgets
import banco
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import funcoes
import datetime

data_atual = datetime.date.today()
ano_atual = data_atual.year

#FUNÇÕES PARA TELA LOGIN
def fazer_login():
    usuario = login.InputUsuario.text().upper()
    senha = login.InputSenha.text()
    usuario_banco = banco.buscar_usuario(usuario)
    #print(usuario_banco)
    if usuario == 'ROOT' and senha == 'manager':
        login.close()
        carrega_usuarios()
    elif len(usuario_banco) == 0:
        QMessageBox.about(login, 'ERRO', 'Usuário inexistente no banco')
    elif senha != usuario_banco[0][2]:
        QMessageBox.about(login, 'ERRO', 'Senha não confere')
    else:
        permi = banco.busca_permissoes(usuario)
        '''cad_contatos.BtnInserir.setVisible(usuario_banco[0][3])
        contato_manut.BtnAlterar.setVisible(usuario_banco[0][4])
        contato_manut.BtnExcluir.setVisible(usuario_banco[0][5])'''
        busca_veiculos.BtnPermissao.setVisible(usuario_banco[0][6])
        busca_veiculos.BtnCadCliente.setVisible(usuario_banco[0][3])
        busca_veiculos.BtnNVeiculos.setVisible(usuario_banco[0][3])
        manut_veiculos.BtnConfirmar.setVisible(usuario_banco[0][4])
        manut_veiculos.BtnExcluir.setVisible(usuario_banco[0][5])
        altera_clientes.BtnConfirmar.setVisible(usuario_banco[0][4])
        altera_clientes.BtnExcluir.setVisible(usuario_banco[0][5])


        login.close()
        busca_veiculos.lbl_ola.setText(f'Seja bem vindo usuário {usuario}')
        busca_veiculos.show()
        QMessageBox.about(busca_veiculos, 'BOAS VINDAS', f'Bem vindo usuário {usuario}, você possui as seguintes permissões: {permi}')

def abrir_cria_usuario():
    login.close()
    cad_usuario.CbCriar.setVisible(False)
    cad_usuario.CbEditar.setVisible(False)
    cad_usuario.CbExcluir.setVisible(False)
    cad_usuario.CbRoot.setVisible(False)
    cad_usuario.show()    


##############################

#FUNÇÕES PARA CRIAÇÃO DE USUÁRIOS

def abrir_tela_login():
    cad_usuario.close()
    login.show()

def criar_novo_usuario():
    usuario = cad_usuario.InputUsuario.text().upper().strip()
    senha = cad_usuario.InputSenha.text()
    confirma = cad_usuario.InputConfirmar.text()
    criar = cad_usuario.CbCriar.isChecked()
    editar = cad_usuario.CbEditar.isChecked()
    excluir = cad_usuario.CbExcluir.isChecked()
    usuario_banco = banco.buscar_usuario(usuario)
    if len(usuario) < 5 or len(senha) < 5:
        QMessageBox.about(cad_usuario, 'ERRO', 'usuário e senha devem ter pelo menos 5 caractéres')
    elif senha != confirma:
        QMessageBox.about(cad_usuario, 'ERRO', 'Senha e confirmação são diferentes')
    elif len(usuario_banco) != 0:
        QMessageBox.about(cad_usuario, 'ERRO', 'Usuário já existe no sistema')
    else:
        banco.novo_usuario(usuario, senha, criar, editar, excluir)
        QMessageBox.about(cad_usuario, 'USUÁRIO CRIADO', f'Usuário {usuario} criado com sucesso!')
        cad_usuario.InputUsuario.setText('')
        cad_usuario.InputSenha.setText('')
        cad_usuario.InputConfirmar.setText('')
        cad_usuario.CbCriar.setChecked(False)
        cad_usuario.CbEditar.setChecked(False)
        cad_usuario.CbExcluir.setChecked(False)

################################

#MANUTENÇÃO DE USUÁRIOS

def carrega_usuarios():
    usuarios = banco.buscar_todos_usuarios()
    #print(usuarios)
    row = 0
    tabela = manut_usuarios.TabelaUsuarios
    tabela.setRowCount(len(usuarios))
    tabela.setColumnWidth(0, 350)
    tabela.setColumnWidth(1, 100)
    tabela.setColumnWidth(2, 100)
    tabela.setColumnWidth(3, 100)
    tabela.setColumnWidth(4, 100)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in usuarios:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        if c[2] == 1:
            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'NÃO'))
        if c[3] == 1:
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'NÃO'))
        if c[4] == 1:
            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'NÃO'))
        if c[5] == 1:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'SIM'))
        else:
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'NÃO'))            
        '''tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[4]}'))
        tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[5]}'))'''
        row += 1
    manut_usuarios.show()

def pega_usuario():
    linha = manut_usuarios.TabelaUsuarios.currentRow()
    nome = manut_usuarios.TabelaUsuarios.item(linha, 0).text()
    criar = manut_usuarios.TabelaUsuarios.item(linha, 1).text()
    editar = manut_usuarios.TabelaUsuarios.item(linha, 2).text()
    excluir = manut_usuarios.TabelaUsuarios.item(linha, 3).text()
    root = manut_usuarios.TabelaUsuarios.item(linha, 4).text()
    permissoes.InputUsuario.setText(nome)
    if criar == 'SIM':
        permissoes.CbCriar.setChecked(True)
    else:
        permissoes.CbCriar.setChecked(False)
    
    if editar == 'SIM':
        permissoes.CbEditar.setChecked(True)
    else:
        permissoes.CbEditar.setChecked(False)

    if excluir == 'SIM':
        permissoes.CbExcluir.setChecked(True)
    else:
        permissoes.CbExcluir.setChecked(False)
    
    if root == 'SIM':
        permissoes.CbRoot.setChecked(True)
    else:
        permissoes.CbRoot.setChecked(False)
    
    permissoes.show()

def setar_permissoes():
    nome = permissoes.InputUsuario.text()
    criar = permissoes.CbCriar.isChecked()
    editar = permissoes.CbEditar.isChecked()
    excluir = permissoes.CbExcluir.isChecked()
    root = permissoes.CbRoot.isChecked()
    banco.alterar_permissoes(nome, criar, editar, excluir, root)
    QMessageBox.about(permissoes, 'PERMISSÕES ALTERADAS', f'Permissões do usuário {nome} alteradas com sucesso')
    carrega_usuarios()
    permissoes.close()


###########################

#FUNÇÕES PARA VEÍCULOS

def buscar_veiculo():
    cpf = busca_veiculos.InputCPF.text()
    if funcoes.valida_cpf(cpf):
        pessoa_banco = banco.buscar_cliente_por_cpf(cpf)

        if len(cpf) < 14:
            QMessageBox.about(busca_veiculos, 'ERRO', 'CPF deve ter 11 digitos')

        elif len(pessoa_banco) == 0:
            men = QMessageBox.question(busca_veiculos, 'PESSOA INEXISTENTE', 'ATENÇÃO, essa pessoa não existe, deseja cadastra-la?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
            if men == QMessageBox.Ok:
                cad_clientes.InputCPF.setText(cpf)
                cad_clientes.show()
            else:
                return
        else:
            carros = banco.buscar_carro_por_cliente(pessoa_banco[0][0])
            #print(carros)
            '''cliente = banco.buscar_cliente_por_id(carros[0][3])
            print(cliente)'''
            return carros
    else:
        QMessageBox.about(busca_veiculos, 'ERRO', 'CPF inválido')

def carrega_veiculos():
    cpf = busca_veiculos.InputCPF.text()
    veiculos = buscar_veiculo()
    if len(veiculos) == 0:
        men = QMessageBox.question(busca_veiculos, 'ATENÇÃO', 'Esse usuário não possui veículos cadastrados, deseja cadastrar?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            cliente = banco.buscar_cliente_por_cpf(cpf)
            #print(cliente)
            #cad_clientes.InputCPF.setText(cpf)
            cad_veiculos.InputNome.setText(cliente[0][1])
            cad_veiculos.InputID.setText(str(cliente[0][0]))
            cad_veiculos.InputMarca.setText('')
            cad_veiculos.InputModelo.setText('')
            cad_veiculos.InputAno.setText('')
            cad_veiculos.show()
        else:
            tabela = busca_veiculos.TabelaCarros
            tabela.setRowCount(0)
            return
    else:
        cliente = banco.buscar_cliente_por_id(veiculos[0][4])
        #print(usuarios)
        row = 0
        tabela = busca_veiculos.TabelaCarros
        tabela.setRowCount(len(veiculos))
        tabela.setColumnWidth(0, 350)
        tabela.setColumnWidth(1, 200)
        tabela.setColumnWidth(2, 200)
        tabela.setColumnWidth(3, 60)
        tabela.setColumnWidth(4, 50)
        #tabela.setColumnWidth(4, 200)
        tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        for c in veiculos:
            tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{cliente[0][1]}'))
            tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
            tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
            tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
            tabela.setItem(row, 4, QtWidgets.QTableWidgetItem(f'{c[0]}'))
            row += 1

def inserir_veiculos():
    global ano_atual
    id = cad_veiculos.InputID.text()
    marca = cad_veiculos.InputMarca.text().title()
    modelo = cad_veiculos.InputModelo.text().title()
    ano = cad_veiculos.InputAno.text()
    
    if marca == '' or modelo == '':
        QMessageBox.about(cad_veiculos, 'ERRO', f'Alguns dados não preenchidos, verifique e tente novamente')
    elif len(ano) < 4:
        QMessageBox.about(cad_veiculos, 'ERRO', f'Ano do veículo precisa ter 4 digitos')
    elif int(ano) > ano_atual or int(ano) < 1920:
        QMessageBox.about(cad_veiculos, 'ERRO', f'Ano do veículo não pode ser maior que o ano atual ou menor que 1920')
    else:
        ano = int(ano)
        banco.inserir_carro(marca, modelo, ano, id)
        men = QMessageBox.question(cad_veiculos, 'VEÍCULO INSERIDO', 'ATENÇÃO, veículo inserido com sucesso, deseja cadastrar outro veículo para esse cliente?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            cad_veiculos.InputMarca.setText('')
            cad_veiculos.InputModelo.setText('')
            cad_veiculos.InputAno.setText('')
        else:
            cad_veiculos.close()
            carrega_veiculos()

def cadastra_novo_veiculo():
    cpf = busca_veiculos.InputCPF.text()
    cliente = banco.buscar_cliente_por_cpf(cpf)
    if len(cliente) == 0:
        men = QMessageBox.question(busca_veiculos, 'PESSOA INEXISTENTE', 'ATENÇÃO, essa pessoa não existe, deseja cadastra-la?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            cad_clientes.InputCPF.setText(cpf)
            cad_clientes.show()
        else:
            return
    else:
        cad_veiculos.InputMarca.setText('')
        cad_veiculos.InputModelo.setText('')
        cad_veiculos.InputAno.setText('')
        #print(cliente)
        #cad_clientes.InputCPF.setText(cpf)
        cad_veiculos.InputNome.setText(cliente[0][1])
        cad_veiculos.InputID.setText(str(cliente[0][0]))
        cad_veiculos.show()

def pega_veiculo():
    linha = busca_veiculos.TabelaCarros.currentRow()
    nome = busca_veiculos.TabelaCarros.item(linha, 0).text()
    marca = busca_veiculos.TabelaCarros.item(linha, 1).text()
    modelo = busca_veiculos.TabelaCarros.item(linha, 2).text()
    ano = busca_veiculos.TabelaCarros.item(linha, 3).text()
    id_veiculo = busca_veiculos.TabelaCarros.item(linha, 4).text()
    cpf = busca_veiculos.InputCPF.text()
    manut_veiculos.InputNome.setText(nome)
    manut_veiculos.InputMarca.setText(marca)
    manut_veiculos.InputModelo.setText(modelo)
    manut_veiculos.InputAno.setText(ano)
    manut_veiculos.InputIDVeiculo.setText(id_veiculo)
    manut_veiculos.InputCPF.setText(cpf)
    manut_veiculos.show()
    #tela_clientes.close()
    #carrega_veiculos()

def altera_veiculo():
    global ano_atual
    id_veiculo = manut_veiculos.InputIDVeiculo.text()
    marca = manut_veiculos.InputMarca.text().title()
    modelo = manut_veiculos.InputModelo.text().title()
    ano = manut_veiculos.InputAno.text()
    if marca == '' or modelo == '':
        QMessageBox.about(manut_veiculos, 'ERRO', f'Alguns dados não preenchidos, verifique e tente novamente')
    elif len(ano) < 4:
        QMessageBox.about(manut_veiculos, 'ERRO', f'Ano do veículo precisa ter 4 digitos')
    elif int(ano) > ano_atual or int(ano) < 1920:
        QMessageBox.about(manut_veiculos, 'ERRO', f'Ano do veículo não pode ser maior que o ano atual ou menor que 1920')
    else:
        ano = int(ano)
        id_veiculo = int(id_veiculo)
        banco.altera_veiculo_id(marca, modelo, ano, id_veiculo)
        men = QMessageBox.about(manut_veiculos, 'VEÍCULO ALTERADO', f'ATENÇÃO, veículo {marca}, {modelo} alterado com sucesso')
        manut_veiculos.close()
        carrega_veiculos()

def excluir_veiculo():
    marca = manut_veiculos.InputMarca.text().title()
    modelo = manut_veiculos.InputModelo.text().title()
    id_veiculo = int(manut_veiculos.InputIDVeiculo.text())
    men = QMessageBox.question(manut_veiculos, 'EXCLUIR VEÍCULO', 'ATENÇÃO, esse veículo será excluído, deseja realmente eliminar esse registro?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
    if men == QMessageBox.Ok:
        banco.excluir_veiculo(id_veiculo)
        QMessageBox.about(manut_veiculos, 'VEÍCULO EXCLUÍDO', f'Veículo {marca}, {modelo} excluído com sucesso')
        manut_veiculos.close()
        carrega_veiculos()
    else:
        return

################   

#FUNÇÕES PARA CLIENTES

def inserir_cliente():
    nome = cad_clientes.InputNome.text().title().strip()
    cpf = cad_clientes.InputCPF.text()
    email = cad_clientes.InputEmail.text().lower().strip()
    if funcoes.valida_cpf(cpf):
        cliente_banco = banco.buscar_cliente_por_cpf(cpf)
        if len(cliente_banco) != 0:
            QMessageBox.about(cad_clientes, 'ERRO', f'CPF já existe')
        elif nome == '' or cpf == '' or email == '':
            QMessageBox.about(cad_clientes, 'ERRO', f'Alguns dados não preenchidos, verifique e tente novamente')
        elif len(cpf) < 14:
            QMessageBox.about(cad_clientes, 'ERRO', f'CPF precisa ter 11 digitos')
        else:
            banco.inserir_cliente(nome, cpf, email)
            QMessageBox.about(cad_clientes, 'CLIENTE INSERIDO', f'Cliente {nome} inserido com sucesso!')
            cad_clientes.InputNome.setText('')
            cad_clientes.InputCPF.setText('')
            cad_clientes.InputEmail.setText('')
    else:
        QMessageBox.about(cad_clientes, 'ERRO', f'CPF inválido')

def gera_cpf_valido():
    cpf_valido = funcoes.gera_cpf()
    cad_clientes.InputCPF.setText(cpf_valido)

def carrega_clientes():
    clientes = banco.buscar_todos_clientes()
    #print(usuarios)
    row = 0
    tabela = tela_clientes.TabelaClientes
    tabela.setRowCount(len(clientes))
    tabela.setColumnWidth(0, 30)
    tabela.setColumnWidth(1, 250)
    tabela.setColumnWidth(2, 200)
    tabela.setColumnWidth(3, 200)
    #tabela.setColumnWidth(4, 200)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in clientes:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        row += 1
    tela_clientes.show()

def abrir_manut_clientes():
    clientes = banco.buscar_todos_clientes()
    #print(usuarios)
    row = 0
    tabela = manut_clientes.TabelaClientes
    tabela.setRowCount(len(clientes))
    tabela.setColumnWidth(0, 30)
    tabela.setColumnWidth(1, 250)
    tabela.setColumnWidth(2, 200)
    tabela.setColumnWidth(3, 200)
    #tabela.setColumnWidth(4, 200)
    tabela.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
    tabela.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
    for c in clientes:
        tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(f'{c[0]}'))
        tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{c[1]}'))
        tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(f'{c[2]}'))
        tabela.setItem(row, 3, QtWidgets.QTableWidgetItem(f'{c[3]}'))
        row += 1
    manut_clientes.show() 
        
def pega_cpf():
    linha = tela_clientes.TabelaClientes.currentRow()
    cpf = tela_clientes.TabelaClientes.item(linha, 2).text()
    busca_veiculos.InputCPF.setText(cpf)
    tela_clientes.close()
    carrega_veiculos()

def pega_cliente():
    linha = manut_clientes.TabelaClientes.currentRow()
    id_cliente = manut_clientes.TabelaClientes.item(linha, 0).text()
    cpf = manut_clientes.TabelaClientes.item(linha, 2).text()
    nome = manut_clientes.TabelaClientes.item(linha, 1).text()
    email = manut_clientes.TabelaClientes.item(linha, 3).text()
    altera_clientes.InputNome.setText(nome)
    altera_clientes.InputCPF.setText(cpf)
    altera_clientes.InputID.setText(id_cliente)
    altera_clientes.InputEmail.setText(email)
    altera_clientes.show()

def altera_cliente():
    id_cliente = altera_clientes.InputID.text()
    nome = altera_clientes.InputNome.text().title()
    email = altera_clientes.InputEmail.text().lower()
    if nome == '' or email == '':
        QMessageBox.about(altera_clientes, 'ERRO', f'Alguns dados não preenchidos, verifique e tente novamente')
    else:
        id_cliente = int(id_cliente)
        banco.alterar_clientes(nome, email, id_cliente)
        QMessageBox.about(altera_clientes, 'CLIENTE ALTERADO', f'Os dados do cliente {nome} foram alterados com sucesso')
        altera_clientes.close()
        abrir_manut_clientes()

def excluir_cliente():
    id_cliente = altera_clientes.InputID.text()
    nome = altera_clientes.InputNome.text().title()
    carros_cliente = banco.buscar_carro_por_cliente(id_cliente)
    if len(carros_cliente) > 0:
        QMessageBox.about(altera_clientes, 'ERRO', f'O cliente {nome} não pode ser excluído pois possui carros cadastrados. para excluí-lo é necessário primeiro excluir todos os seus veículos')
    else:
        men = QMessageBox.question(altera_clientes, 'EXCLUIR CLIENTE', f'ATENÇÃO, o cliente {nome} será excluído, deseja realmente eliminar esse registro?', QMessageBox.Ok|QMessageBox.Cancel, QMessageBox.Ok)
        if men == QMessageBox.Ok:
            banco.excluir_cliente(id_cliente)
            QMessageBox.about(manut_veiculos, 'CLIENTE EXCLUÍDO', f'O cliente {nome} foi excluído com sucesso')
            altera_clientes.close()
            abrir_manut_clientes()
        else:
            return


#########################

#TELAS

qt = QtWidgets.QApplication(sys.argv)

busca_veiculos = uic.loadUi('buscar_veiculos_cpf.ui')
cad_clientes = uic.loadUi('cad_clientes.ui')
tela_clientes = uic.loadUi('tela_clientes.ui')
manut_clientes = uic.loadUi('tela_clientes.ui')
altera_clientes = uic.loadUi('manut_clientes.ui')
cad_veiculos = uic.loadUi('cad_veiculos.ui')
manut_veiculos = uic.loadUi('manut_veiculos.ui')
login = uic.loadUi('tela_login.ui')
cad_usuario = uic.loadUi('tela_cadastro.ui')
manut_usuarios = uic.loadUi('manutencao_usuarios.ui')
permissoes = uic.loadUi('permissoes_usuarios.ui')
busca_veiculos.BtnBuscar.clicked.connect(carrega_veiculos)
busca_veiculos.BtnBuscarCliente.clicked.connect(carrega_clientes)
busca_veiculos.BtnManutCliente.clicked.connect(abrir_manut_clientes)
busca_veiculos.BtnNVeiculos.clicked.connect(cadastra_novo_veiculo)
busca_veiculos.BtnCadCliente.clicked.connect(cad_clientes.show)
busca_veiculos.TabelaCarros.doubleClicked.connect(pega_veiculo)
busca_veiculos.BtnPermissao.clicked.connect(carrega_usuarios)
tela_clientes.TabelaClientes.doubleClicked.connect(pega_cpf)
manut_clientes.TabelaClientes.doubleClicked.connect(pega_cliente)
cad_clientes.BtnInserir.clicked.connect(inserir_cliente)
cad_clientes.BtnGeraCPF.clicked.connect(gera_cpf_valido)
cad_veiculos.BtnInserir.clicked.connect(inserir_veiculos)
manut_veiculos.BtnConfirmar.clicked.connect(altera_veiculo)
manut_veiculos.BtnCancelar.clicked.connect(manut_veiculos.close)
manut_veiculos.BtnExcluir.clicked.connect(excluir_veiculo)
altera_clientes.BtnConfirmar.clicked.connect(altera_cliente)
altera_clientes.BtnCancelar.clicked.connect(altera_clientes.close)
altera_clientes.BtnExcluir.clicked.connect(excluir_cliente)
##############

#USUÁRIOS



login.BtnEntrar.clicked.connect(fazer_login)
login.BtnCriar.clicked.connect(abrir_cria_usuario)
cad_usuario.BtnCadastrar.clicked.connect(criar_novo_usuario)
cad_usuario.BtnLogin.clicked.connect(abrir_tela_login)
manut_usuarios.BtnVoltar.clicked.connect(manut_usuarios.close)
manut_usuarios.TabelaUsuarios.doubleClicked.connect(pega_usuario)
permissoes.BtnCancelar.clicked.connect(permissoes.close)
permissoes.BtnSetar.clicked.connect(setar_permissoes)

##############

login.show()
qt.exec_()