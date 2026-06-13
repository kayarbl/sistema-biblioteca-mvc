from config.conexao import ConexaoDB
from psycopg2 import sql

class UsuarioModel:
    def __init__(self):
        self.db = ConexaoDB()

    def inserir(self, nome, email, telefone):
        query = sql.SQL("""
            INSERT INTO {tabela} 
            (nome, email, telefone)
            VALUES (%s, %s, %s)
        """).format(
            tabela=sql.Identifier("usuarios")
        )

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            cursor.execute(query, (nome, email, telefone))
            conn.commit()

            cursor.close()
            conn.close()

        except Exception as erro:
            print("Erro ao inserir usuário:", erro)

    def listar(self):
        query = sql.SQL("""
            SELECT 
                id, nome, email, telefone, data_cadastro
            FROM {tabela}
            ORDER BY nome
        """).format(
            tabela=sql.Identifier("usuarios")
        )

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            cursor.execute(query)
            dados = cursor.fetchall()

            cursor.close()
            conn.close()
            return dados

        except Exception as erro:
            print("Erro ao listar usuários:", erro)
            return []
