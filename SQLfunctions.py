import mysql.connector


class Table:
    def __init__(self, table_name):
        self.name = table_name
        self.columns = []  # string names of the columns // nomes das colunas em string


# This module provides a class to manage MySQL database connections and execute SQL queries.
# Este modulo se trata de uma classe para gerenciar conexões com banco de dados MySQL e executar consultas SQL.
class Connection:
    def __init__(self, host, port, user, password, database):
        self.host = host
        # address from the host
        # Endereço do host
        self.port = port
        # port to connect to the database
        # Porta para conectar ao banco de dados
        self.user = user
        # user name to connect to the database
        # Nome do usuário para conectar ao banco de dados
        self.password = password
        # password to connect to the database
        # Senha para conectar ao banco de dados
        self.database = database
        # database name
        # Nome do banco de dados

    # connect to the database and return the connection object
    # conectar ao banco de dados e retornar o objeto de conexão
    def connect(self):
        try:
            # Linking the connection to the database
            # estabelecendo a conexão com o banco de dados
            self.conn = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return self.conn
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    # instancia um objeto da classe Table com o nome da tabela e retorna as colunas dela
    # instance an object of the class Table with the name of the table and return its columns
    def table(self, table_name):
        cursor = self.conn.cursor()
        try:
            cursor.execute(
                f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '{self.database}' AND TABLE_NAME = '{table_name}';")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        result = cursor.fetchall()
        print(result)
        table = Table(table_name)
        table.columns = [column[0] for column in result]
        cursor.close()
        return table
    # close the connection to the database
    # fechar a conexão com o banco de dados

    def close(self):
        if self.conn.is_connected():
            self.conn.close()


# sql queries that u can use to return a especific command in a string
# consultas SQL que você pode usar para retornar um comando específico em uma string


class Query_to:
    def __init__(self, table_name):
        self.name = table_name

    def insert(self, columns, values):

        return f"INSERT INTO {self.name} ({",".join(columns)}) VALUES ({",".join(values)});"
