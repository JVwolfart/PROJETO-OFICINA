import sqlite3
from sqlite3.dbapi2 import Cursor

def conectar():
    banco = sqlite3.connect('bdados.db')
    return banco.cursor()

def criar_cliente():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS clientes(nome TEXT, cpf TEXT, email TEXT)')
    banco.commit()
    banco.close()

def inserir_cliente(nome, cpf, email):
    criar_cliente()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"INSERT INTO clientes VALUES( '{nome}', '{cpf}', '{email}')")
    banco.commit()
    banco.close()

def buscar_cliente_por_cpf(cpf):
    criar_cliente()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT rowid, * FROM clientes WHERE cpf='{cpf}'")
    return cur.fetchall()
    banco.commit()

def buscar_cliente_por_id(id):
    criar_cliente()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT rowid, * FROM clientes WHERE rowid={id}")
    return cur.fetchall()
    banco.commit()

def buscar_cliente_por_nome(nome):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT rowid, * FROM clientes WHERE nome='{nome}'")
    return cur.fetchall()
    banco.commit()

def buscar_todos_clientes():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT rowid, * FROM clientes ORDER BY nome ASC")
    return cur.fetchall()
    banco.commit()
    

def deletar_cliente_cpf(cpf):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"DELETE  FROM clientes WHERE cpf='{cpf}'")
    banco.commit()
    banco.close()

def alterar_clientes(nome, email, id_cliente):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"UPDATE clientes SET nome='{nome}', email='{email}' WHERE rowid={id_cliente}")
    banco.commit()
    banco.close()

def criar_usuario():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS usuarios(nome TEXT, senha TEXT, criar BOOLEAN, editar BOOLEAN, excluir BOOLEAN, root BOOLEAN)')
    banco.commit()
    banco.close()

def buscar_usuario(nome):
    criar_usuario()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT rowid, * FROM usuarios WHERE nome='{nome}'")
    return cur.fetchall()
    banco.commit()

def novo_usuario(nome, senha, criar, editar, excluir, root=False):
    criar_usuario()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"INSERT INTO usuarios VALUES('{nome}','{senha}', {criar}, {editar}, {excluir}, {root})")
    banco.commit()
    banco.close()

def alterar_permissoes(nome, criar, editar, excluir, root):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"UPDATE usuarios SET criar={criar}, editar={editar}, excluir={excluir}, root={root} WHERE nome='{nome}'")
    banco.commit()
    banco.close()

def buscar_todos_usuarios():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT * FROM usuarios")
    return cur.fetchall()
    banco.commit()

def busca_permissoes(nome):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT criar, editar, excluir, root FROM usuarios WHERE nome='{nome}'")
    permissoes = cur.fetchone()
    autorizacoes = []
    for k, c in enumerate(permissoes):
        if k == 0 and c == 1:
            autorizacoes.append('Criar')
        if k == 1 and c == 1:
            autorizacoes.append('Editar')
        if k == 2 and c == 1:
            autorizacoes.append('Excluir')
        if k == 3 and c == 1:
            autorizacoes.append('Root')
    if len(autorizacoes) == 0:
        autorizacoes.append('Apenas consulta, caso queira outras permissões solicite ao administrador')
    return autorizacoes
    #banco.commit()

def criar_servicos():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS servicos(descricao TEXT, valor REAL)')
    banco.commit()
    banco.close()

def inserir_servico(desc, val):
    criar_servicos()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"INSERT INTO servicos VALUES( '{desc}', {val})")
    banco.commit()
    banco.close()

def buscar_servico_por_descricao(desc):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT * FROM servicos WHERE descricao='{desc}'")
    return cur.fetchall()
    banco.commit()

def buscar_servico_por_valor(val):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT * FROM servicos WHERE valor={val}")
    return cur.fetchall()
    banco.commit()

def buscar_todos_servicos():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT * FROM servicos")
    return cur.fetchall()
    banco.commit()
    

'''def deletar_cliente_cpf(cpf):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"DELETE  FROM clientes WHERE cpf='{cpf}'")
    banco.commit()
    banco.close()

def alterar_clientes(nome, cpf, telefone, categoria, email):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"UPDATE clientes SET nome='{nome}', telefone='{telefone}', categoria='{categoria}', email='{email}' WHERE cpf='{cpf}'")
    banco.commit()
    banco.close()'''

def criar_carros():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS carros(marca TEXT, modelo TEXT, ano INTERGER, cliente_id INTERGER NOT NULL, FOREIGN KEY(cliente_id) REFERENCES clientes(id))')
    banco.commit()
    banco.close()

def inserir_carro(marca, modelo, ano, pessoa_id):
    criar_carros()
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"INSERT INTO carros VALUES( '{marca}', '{modelo}', {ano}, {pessoa_id})")
    banco.commit()
    banco.close()

def buscar_carro_por_marca(marca):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT * FROM carros WHERE marca='{marca}'")
    return cur.fetchall()
    banco.commit()

def buscar_carro_por_modelo(modelo):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT * FROM carros WHERE modelo='{modelo}'")
    return cur.fetchall()
    banco.commit()

def buscar_carro_por_ano(ano):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT * FROM carros WHERE ano={ano}")
    return cur.fetchall()
    banco.commit()

def buscar_carro_por_cliente(id_pessoa):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT rowid, * FROM carros WHERE cliente_id={id_pessoa}")
    return cur.fetchall()
    banco.commit()


def buscar_todos_carros():
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"SELECT * FROM carros ORDER BY ano ASC")
    return cur.fetchall()
    banco.commit()

def altera_veiculo_id(marca, modelo, ano, id_veiculo):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"UPDATE carros SET marca='{marca}', modelo='{modelo}', ano={ano} WHERE rowid={id_veiculo}")
    banco.commit()
    banco.close()

def excluir_veiculo(id_veiculo):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"DELETE FROM carros WHERE rowid={id_veiculo}")
    banco.commit()
    banco.close()

def excluir_cliente(id_cliente):
    banco = sqlite3.connect('bdados.db')
    cur = banco.cursor()
    cur.execute(f"DELETE FROM clientes WHERE rowid={id_cliente}")
    banco.commit()
    banco.close()
