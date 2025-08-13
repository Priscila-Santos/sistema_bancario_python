# 💸 Sistema Bancário em Python — Orientado a Objetos

Este projeto é um sistema bancário simples e funcional desenvolvido em Python, com uma estrutura baseada em **classes e objetos**, seguindo princípios de **Programação Orientada a Objetos (POO)**. Ele permite realizar **depósitos**, **saques**, **transferências** e visualizar o **extrato bancário**, armazenando todas as informações em arquivos `.csv` como banco de dados simulado.

---

## 🧾 Funcionalidades e Regras de Negócio

- Cadastro de usuários (nome completo, CPF, número da conta)
- Autenticação por CPF e número da conta
- Depósitos (valores positivos)
- Saques:
  - Até **3 saques por dia**
  - Limite de **R$ 500 por saque**
- Transferência entre contas
- Extrato completo da conta (saques, depósitos, transferências e saldo atual)
- Validação de saldo insuficiente
- Armazenamento persistente em arquivos `.csv`
- Mensagens informativas e formato monetário brasileiro `R$ xxx.xx`

---

## 🧱 Estrutura Orientada a Objetos

O sistema utiliza duas classes principais:

- `Cliente`: representa o usuário, com CPF, nome e vínculo à conta
- `Conta`: representa a conta bancária, com número, saldo e operações como depósito, saque, extrato e transferência

---

## 📁 Estrutura de Arquivos

- `usuarios.csv`: contém informações dos usuários, como CPF, nome, conta e saldo atual
- `transacoes.csv`: registra todas as operações financeiras (depósitos, saques e transferências) com data e hora

---

## ⚙️ Como Executar

1. **Clone o repositório** (ou copie os arquivos manualmente):

   ```bash
   git clone https://github.com/seu-usuario/sistema_bancario_python_v2.git
   cd sistema_bancario
   ```

2. **Execute o script** no terminal:

   ```bash
   python sistema_bancario.py
   ```

3. **Interaja com o menu** para realizar operações bancárias diretamente pelo terminal.

---

## 🧪 Exemplos de Uso

```python
# Cadastro
cadastrar_usuario("José Silva", "12345678903", "0002")

# Operações
cliente = autenticar("12345678903", "0002")
cliente.conta.depositar(1500)
cliente.conta.sacar(200)
cliente.conta.sacar(600)  # Deve falhar por limite diário
cliente.conta.sacar(500)
cliente.conta.sacar(1300)  # Deve falhar por saldo insuficiente

# Transferência
cliente.conta.transferir("0003", 300)

# Extrato
cliente.conta.extrato()
```

---

## 🛠 Requisitos

- Python 3.x instalado
- Editor de texto ou IDE (como VS Code ou PyCharm)
- Permissão para leitura/escrita de arquivos no diretório do projeto

---

## 🧪 Testes Interativos

Você pode interagir com o sistema diretamente via terminal. Para expandir a experiência, considere:

- Criar uma interface gráfica com `Tkinter`
- Migrar para banco de dados real como `SQLite` ou `PostgreSQL`
- Criar uma API REST com `Flask` ou `FastAPI`

---

## 🤝 Contribuições

Sinta-se à vontade para contribuir com melhorias no código, como:

- Autenticação com senha
- Relatórios gráficos
- Exportação de extrato em PDF
- Interface web com Flask ou Django
- Testes automatizados com `pytest`

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Feito com ☕ e 🧠 por Priscila Santos

