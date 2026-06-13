from config.conexao import ConexaoDB
from psycopg2 import sql

class LivroModel:
    def __init__(self):
        self.db = ConexaoDB()

    def inserir(self, titulo, autor, ano, qtd_total, qtd_disp):
        query = sql.SQL("""
            INSERT INTO {tabela}
            (titulo, autor, ano_publicacao, quantidade_total, quantidade_disponivel)
            VALUES (%s, %s, %s, %s, %s)
        """).format(
            tabela=sql.Identifier("livros")
        )

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(query, (titulo, autor, ano, qtd_total, qtd_disp))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as erro:
            print("Erro ao inserir livro:", erro)

    def listar(self):
        query = sql.SQL("""
            SELECT 
                id, titulo, autor, ano_publicacao,
                quantidade_total, quantidade_disponivel
            FROM {tabela}
            ORDER BY titulo
        """).format(
            tabela=sql.Identifier("livros")
        )

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()#executa o comando 
            cursor.execute(query) 
            dados = cursor.fetchall() #pega todos os registros retomados pela query
            cursor.close()
            conn.close()
            return dados  # retorna lista de tuplas
        except Exception as erro:
            print("Erro ao listar livros:", erro)
            return [] #retorna lista vazia e garante que o programa continue rodando

    def buscar_por_id(self, livro_id):
        query = sql.SQL("""
            SELECT 
                id, titulo, autor, ano_publicacao,
                quantidade_total, quantidade_disponivel
            FROM {tabela}
            WHERE id = %s
        """).format(
            tabela=sql.Identifier("livros")
        )

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(query, (livro_id,))
            linha = cursor.fetchone()
            cursor.close()
            conn.close()
            return linha  # retorna tupla ou None
        except Exception as erro:
            print("Erro ao buscar livro:", erro)
            return None

    def atualizar(self, livro_id, titulo, autor, ano, qtd_total, qtd_disp):
        query = sql.SQL("""
            UPDATE {tabela}
            SET titulo = %s,
                autor = %s,
                ano_publicacao = %s,
                quantidade_total = %s,
                quantidade_disponivel = %s
            WHERE id = %s
        """).format(
            tabela=sql.Identifier("livros")
        )

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(query, (titulo, autor, ano, qtd_total, qtd_disp, livro_id))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as erro:
            print("Erro ao atualizar livro:", erro)

    def excluir(self, livro_id):
        query = sql.SQL("""
            DELETE FROM {tabela}
            WHERE id = %s
        """).format(
            tabela=sql.Identifier("livros")
        )

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(query, (livro_id,))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as erro:
            print("Erro ao excluir livro:", erro)

    def alterar_disponivel(self, livro_id, nova_qtd):
        query = """
            UPDATE livros
            SET quantidade_disponivel = %s
            WHERE id = %s
        """
        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(query, (nova_qtd, livro_id))
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as erro:
            print("Erro ao atualizar quantidade disponível:", erro)
