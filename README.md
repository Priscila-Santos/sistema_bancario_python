# 💸 Sistema Bancário em Python

Este projeto é um sistema bancário simples desenvolvido em Python que permite realizar **depósitos**, **saques** e visualizar o **extrato bancário**, armazenando todas as informações em arquivos `.csv` como banco de dados simulado.

## 🧾 Funcionalidades e Regras de Negócio

- Cadastro de usuários (nome completo, CPF, número da conta)
- Depósitos (valores positivos)
- Saques (até 3 por dia com limite de R$ 500 por saque)
- Extrato completo da conta (saques, depósitos e saldo atual)
- Validação de saldo insuficiente
- Armazenamento persistente em arquivos `.csv`
- Mensagens informativas e formato monetário brasileiro `R$ xxx.xx`

## 📁 Estrutura de Arquivos

- `usuarios.csv`: contém informações dos usuários, como CPF, nome, conta e saldo atual.
- `transacoes.csv`: registra todas as operações financeiras (depósitos e saques) com data e hora.

## ⚙️ Como Executar

1. **Clone o repositório** (ou copie os arquivos manualmente):

   ```bash
   git clone https://github.com/seu-usuario/sistema_bancario_python_v1.git
   cd sistema_bancario_v1
   ```

2. **Execute o script** no terminal:

   ```bash
   python sistema_bancario.py
   ```

3. **Teste as operações** adicionando chamadas de funções ao final do arquivo `sistema_bancario.py`, como:

```python
  cadastrar_usuario("José Silva", "12345678903", "0002")

  depositar("0002", 1500)
  sacar("0002", 200)
  sacar("0002", 600) # Deve falhar por limite diário
  sacar("0002", 500)
  sacar("0002", 1300)  # Deve falhar por limite do saldo

  extrato("0002")
```

## 🛠 Requisitos

- Python 3.x instalado
- Editor de texto ou IDE (como VS Code ou PyCharm)
- Permissão para leitura/escrita de arquivos no diretório do projeto

## 🧪 Testes Interativos

Você pode interagir com o sistema diretamente via terminal, adicionando menus ou criando uma interface gráfica com bibliotecas como `Tkinter`.

## 🤝 Contribuições

Sinta-se à vontade para contribuir com melhorias no código, como:
- Implementação de autenticação com senha
- Relatórios gráficos
- Exportação de extrato em PDF
- Interface web com Flask ou Django

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## Feito com ☕ e 🧠 por Priscila Santos
