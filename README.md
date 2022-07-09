# PROJETO-OFICINA

Esse foi meu primeiro projeto do Jovem Programador módulo 2.
O projeto consiste basicamente em:
- Um cadastro de usuários
- Permissão de acessos dependendo do nível do usuário
- Cadastro simples de clientes
- Cadastro de veículos

É utilizado o banco de dados Sqlite3.

Regra de negócio deste projeto:

O usuário pode se cadastrar livremente, porém com o simples cadastro do usuário ele apenas terá permissão para consultas,

para ter mais permissões elas deverão ser concedidas a ele pelo ROOT, as permissões possíveis são:
- Somente consulta
- Criar (permite cadastrar novos veículos e clientes)
- Editar (permite alterar veículos e clientes existentes)
- Excluir (permite excluir veículos e clientes)
- ROOT (permite setar permissões para os usuários)

Existe um superusuário que através dele poderá ser setado ao primeiro usuário cadastrado a permissão de ROOT e após isso esse primeiro usuário já pode setar as permissões aos demais usuários.

No cadastro de clientes existe uma verificação para saber se o CPF é válido, para efeito de testes também foi colocado um botão de gerar CPF que gera CPFs aleatórios válidos para facilitar os testes e os cadastros de clientes, lembrando que esse sistema é apenas um exercício didático e não tem nenhuma funcionalidade prática, apenas serve como uma forma de praticar o CRUD.

Ao entrar no sistema o usuário deve receber uma mensagem de boas vindas informando suas permissões.
De acordo com suas permissões será as opções que ele deve ter disponível na tela.

Caso seja apenas consulta ele verá as opções de buscar clientes e manutenção de clientes, sendo que não conseguirá fazer nenhuma alteração, apenas verificar os dados.

Se a permissão for criar, vai aparecer também a opção de cadastrar clientes e cadastrar veículos, e ele conseguirá fazer cadastros, porém não poderá alterar dados existentes, pois para isso é necessário a permissão de editar.

Se a permissão for editar, ele poderá apenas editar os registros e se for criar e editar vai poder criar e editar, mas não poderá excluir registros, pois para isso é necessário a permissão de excluir.

Se a permissão for excluir, então ele poderá também excluir registros, e se for criar, editar e excluir ele poderá fazer o CRUD completo, apenas não poderá setar permissões aos usuários, pois para isso é necessário a permissão de ROOT.

Caso o usuário tenha permissão de ROOT ele poderá setar as permissões para ele mesmo e os demais usuários, portanto 
se ele tiver a permissão de ROOT ele consegue fazer o que quiser no sistema.

Quanto a exclusão dos registros:

Caso tente excluir algum cliente que possui veículos cadastrados, o sistema deve informar uma mensagem de erro avisando que esse cliente não pode ser excluído pois possui veículos cadastrados para ele e que é necessário primeiro excluir o registro desses veículos para depois poder excluir o cliente.

Em resumo, esse simples exemplo de exercício serviu para praticar a construção de um programa com interface gráfica utilizando o PyQt5 e o Qt design e também um exercício para praticar o uso do banco de dados relacional Sqlite, pois era necessário haver uma relação entre os clientes e seus veículos.

Também esse sistema foi importante para exercitar a lógica de permissão, do que os usuários podem ou não podem fazer, dependendo de suas permissões.

Quem quiser ver como ficou basta baixar esse projeto, e instalar as dependências (basicamente pyqt5) e o Python na versão 3.x

Para poder setar as permissões deve utilizar inicialmente o superusuário ROOT e a senha manager.

Para executar o sistema utilize o arquivo main.py, que vai abrir a tela de login, onde você poderá se cadastrar e logo em seguida logar novamente com o superusuário ROOT para lhe dar as permissões que você quiser.
