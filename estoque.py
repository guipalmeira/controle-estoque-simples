from db import conectar

def cadastrar_produto(nome, quantidade, valor, fornecedor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO produtos (nome, quantidade, valor, fornecedor)
        VALUES (?, ?, ?, ?)
    ''', (nome, quantidade, valor, fornecedor))
    conn.commit()
    conn.close()

def listar_produtos_por_fornecedor(fornecedor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT nome, quantidade, valor FROM produtos
        WHERE fornecedor = ?
    ''', (fornecedor,))
    produtos = cursor.fetchall()
    conn.close()
    return produtos

def remover_produto(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM produtos WHERE nome = ?', (nome,))
    conn.commit()
    conn.close()