
# 📦 Sistema de Controle de Estoque (Versão Simples - Sem Banco de Dados)

Este é um sistema de controle de estoque simples, feito em Python, que permite cadastrar produtos, associá-los a fornecedores, visualizar o estoque, remover itens e acessar o sistema por meio de login e senha.

---

## 🚀 Funcionalidades

- ✅ Login com verificação de senha
- ✅ Cadastro de fornecedores e seus produtos
- ✅ Consulta de estoque por fornecedor
- ✅ Remoção de produtos do estoque
- ✅ Menu interativo com opções de navegação

---

## 🛠️ Como funciona

### 1. Login
Ao iniciar o programa, o usuário precisa digitar um login e uma senha. Os logins e senhas são pré-definidos em listas:

```python
logins = ['gui01', 'gui02']
senhas = [123, 1234]
```

Se o login e senha corresponderem, o acesso ao menu principal é liberado.

---

### 2. Menu Principal

O menu apresenta as opções:

```
1 - Cadastro de Fornecedores
2 - Produtos em Estoque
3 - Programando (ainda em desenvolvimento)
4 - Remover Produto
5 - Editar Informações (ainda em desenvolvimento)
0 - Sair
```

---

### 3. Cadastro de Produtos

Ao escolher a opção 1:

- O usuário deve informar o nome do fornecedor, nome do produto, quantidade e valor.
- Esses dados são salvos em dois dicionários:
  - `estoque`: guarda o nome do produto, quantidade e valor.
  - `fornecedores`: associa o produto ao nome do fornecedor.

---

### 4. Consulta de Estoque

Na opção 2:

- O usuário digita o nome do fornecedor.
- O sistema busca nos dicionários os produtos cadastrados por aquele fornecedor e exibe quantidade e valor.

---

### 5. Remoção de Produto

Na opção 3 (em seu código, o número está invertido):

- O usuário informa o nome do produto que deseja remover.
- O produto é excluído tanto do dicionário `estoque` quanto de `fornecedores`.

---

## ⚠️ Observações

- O sistema **não salva os dados** ao encerrar. Tudo é armazenado em memória usando `dicionários`, ou seja, os dados são perdidos ao fechar o programa.
- É uma versão básica, ideal para aprendizado de lógica e estrutura em Python.
- As opções "Programando" e "Editar Informações" ainda não estão implementadas.

---

## ✅ Requisitos

- Python 3.x

---

## ▶️ Como executar

1. Copie o código para um arquivo `.py` (ex: `sistema_estoque.py`).
2. Execute pelo terminal ou por um editor de código (VS Code, PyCharm etc):

```bash
python sistema_estoque.py
```

---

## 📚 Próximos Passos

- Adicionar banco de dados SQLite para persistência dos dados.
- Melhorar tratamento de erros.
- Implementar sistema de edição de produtos e usuários.
- Interface gráfica ou versão web futuramente.

---

## 🧑‍💻 Autor

Desenvolvido por Guilherme Palmeira, como parte de um projeto de aprendizado em Python.
