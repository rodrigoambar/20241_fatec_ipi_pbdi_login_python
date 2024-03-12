import psycopg
print(psycopg)
class Usuario:
  def __init__(self, login, senha):
    self.login = login
    self.senha = senha

#verifica se o usuário recebido existe na base
def existe(usuario):
  #abrir uma conexão com o PostgreSQL
  #obter uma abstração do tipo "cursor"
  #executar um comando sql
  #verificar o resultado
  #devolver True ou False
  with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="20241_fatec_ipi_pbdi_login_python",
    user="postgres",
    password="123456"
  ) as conexao:
    with conexao.cursor() as cursor:
      cursor.execute(
        'SELECT * FROM tb_usuario WHERE login=%s AND senha=%s',
        (usuario.login, usuario.senha)
      )
      result = cursor.fetchone()
      
      #return #se result for igual a None, devolvo False, senão devolvo True
      #return True if result != None else False
      return result != None
def inserir_usuario(login_novo, senha_novo):
  with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="20241_fatec_ipi_pbdi_login_python",
    user="postgres",
    password="123456"
  ) as conexao:
    with conexao.cursor() as cursor:
      insert = "INSERT INTO tb_usuario(login, senha) VALUES(%s, %s)"
      values = (login_novo, senha_novo)
      cursor.execute(insert, values)

    conexao.commit

def menu():
  texto = '0-Sair\n1-Login\n2-Logoff\n3-Cadastrar de usuario\n'
  #usuario ainda não existe
  usuario = None
  op = int(input(texto))
  while op != 0:
    if op == 1:
      login = input('Digite o login: ')
      senha = input('Digite a senha: ')
      usuario = Usuario(login, senha)
      #expressão condicional 
      print('Usuario ok ' if existe(usuario) else 'Usuario nok')
    elif op == 2:
      usuario = None
      print('Logoff realizado com sucesso')
    elif op == 3:
      login_novo = input('Coloque o login do novo usuario: ')
      senha_novo = int(input('digite a senha do novo usuario: '))
      inserir_usuario(login_novo, senha_novo)
      if inserir_usuario == True:
        print("Usuario cadastrado com sucesso")

    else:
      print('Jovem não seja cabaço')
    op = int(input(texto))
menu()



# def teste():
#   print(existe(Usuario('admin', 'admin')))

# teste()