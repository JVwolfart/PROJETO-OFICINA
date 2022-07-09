import banco

cpf = input('Informe o seu cpf: ')
pessoa = banco.buscar_cliente_por_cpf(cpf)

if len(pessoa) == 0:
    print('Essa pessoa não existe no banco, informe os dados abaixo')
    nome = input('Nome: ')
    email = input('E-mail: ')
    banco.inserir_cliente(nome, cpf, email)
    print('Pessoa inserida com sucesso')

marca = input('Marca: ')
modelo = input('Modelo: ')
ano = int(input('Ano: '))
id = pessoa[0][0]
banco.inserir_carro(marca, modelo, ano, id)
print('Carro inserido com sucesso')