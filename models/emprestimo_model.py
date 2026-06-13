from config.conexao import ConexaoDB
from psycopg2 import sql

class EmprestimoModel:
    def __init__(self):
        self.db = ConexaoDB()


    def inserir(self, usuario_id, livro_id, data_emp, data_prev):
        query = sql.SQL("""
            INSERT INTO {tabela}
            (usuario_id, livro_id, data_emprestimo, data_devolucao_prevista)
            VALUES (%s, %s, %s, %s)
        """).format(
            tabela=sql.Identifier("emprestimos")
        )

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()
            cursor.execute(query, (usuario_id, livro_id, data_emp, data_prev))
            conn.commit()
            cursor.close()
            conn.close()

        except Exception as erro:
            print("Erro ao registrar empréstimo:", erro)

    def listar(self):
        query = sql.SQL("""
            SELECT 
                e.id,
                u.nome AS usuario,
                l.titulo AS livro,
                e.data_emprestimo,
                e.data_devolucao_prevista,
                e.data_devolucao_real,
                e.status
            FROM {emprestimos} AS e
            JOIN {usuarios} AS u ON u.id = e.usuario_id
            JOIN {livros} AS l ON l.id = e.livro_id
            WHERE e.status = 'EMPRESTADO'
            ORDER BY e.id DESC
        """).format(
            emprestimos=sql.Identifier("emprestimos"),
            usuarios=sql.Identifier("usuarios"),
            livros=sql.Identifier("livros")
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
            print("Erro ao listar empréstimos:", erro)
            return []
        
    def devolver(self, emprestimo_id, data_devolucao):
        query = """
            UPDATE emprestimos
            SET data_devolucao_real = %s, status = 'DEVOLVIDO'
            WHERE id = %s
        """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            cursor.execute(query, (data_devolucao, emprestimo_id))

            conn.commit()

            cursor.close()
            conn.close()

        except Exception as erro:
            print("Erro ao devolver livro:", erro)

    def buscar_por_id(self, emprestimo_id):
        query = """
            SELECT *
            FROM emprestimos
            WHERE id = %s
        """

        try:
            conn = self.db.conectar()
            cursor = conn.cursor()

            cursor.execute(query, (emprestimo_id,))
            resultado = cursor.fetchone()

            cursor.close()
            conn.close()

            return resultado

        except Exception as erro:
            print("Erro ao buscar empréstimo:", erro)
            return None