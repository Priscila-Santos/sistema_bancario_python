import csv
from datetime import datetime

ARQUIVO_USUARIOS = 'usuarios.csv'
ARQUIVO_TRANSACOES = 'transacoes.csv'

def criar_arquivos():
    # Cria os arquivos iniciais se não existirem
    for arquivo, campos in [(ARQUIVO_USUARIOS, ['cpf', 'nome', 'conta', 'saldo']),
                            (ARQUIVO_TRANSACOES, ['conta', 'tipo', 'valor', 'data'])]:
        try:
            with open(arquivo, 'x', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(campos)
        except FileExistsError:
            pass

def cadastrar_usuario(nome, cpf, numero_conta):
    with open(ARQUIVO_USUARIOS, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([cpf, nome, numero_conta, 0.0])

def buscar_usuario(conta):
    with open(ARQUIVO_USUARIOS, 'r') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            if linha['conta'] == conta:
                return linha
    return None

def atualizar_saldo(conta, novo_saldo):
    linhas = []
    with open(ARQUIVO_USUARIOS, 'r') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            if linha['conta'] == conta:
                linha['saldo'] = str(novo_saldo)
            linhas.append(linha)
    with open(ARQUIVO_USUARIOS, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['cpf', 'nome', 'conta', 'saldo'])
        writer.writeheader()
        writer.writerows(linhas)

def registrar_transacao(conta, tipo, valor):
    with open(ARQUIVO_TRANSACOES, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([conta, tipo, f"{valor:.2f}", datetime.now().strftime('%d/%m/%Y %H:%M:%S')])

def contar_saques(conta):
    hoje = datetime.now().strftime('%d/%m/%Y')
    contagem = 0
    with open(ARQUIVO_TRANSACOES, 'r') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            if linha['conta'] == conta and linha['tipo'] == 'saque' and hoje in linha['data']:
                contagem += 1
    return contagem

def depositar(conta, valor):
    if valor <= 0:
        print("⚠️ Depósitos devem ser maiores que zero.")
        return
    usuario = buscar_usuario(conta)
    saldo = float(usuario['saldo']) + valor
    atualizar_saldo(conta, saldo)
    registrar_transacao(conta, 'depósito', valor)
    print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso!")

def sacar(conta, valor):
    usuario = buscar_usuario(conta)
    saldo = float(usuario['saldo'])
    if contar_saques(conta) >= 3:
        print("⚠️ Limite de 3 saques diários atingido.")
        return
    if valor > 500:
        print("⚠️ Valor do saque excede o limite de R$ 500.00.")
        return
    if saldo < valor:
        print("⚠️ Saldo insuficiente.")
        return
    atualizar_saldo(conta, saldo - valor)
    registrar_transacao(conta, 'saque', valor)
    print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso!")

def extrato(conta):
    movimentos = []
    with open(ARQUIVO_TRANSACOES, 'r') as f:
        reader = csv.DictReader(f)
        for linha in reader:
            if linha['conta'] == conta:
                movimentos.append(linha)
    usuario = buscar_usuario(conta)
    print("\n📄 Extrato da Conta:")
    if not movimentos:
        print("Não foram realizadas movimentações.")
    else:
        for mov in movimentos:
            tipo = mov['tipo'].capitalize()
            valor = float(mov['valor'])
            print(f"{tipo}: R$ {valor:.2f} em {mov['data']}")
    print(f"\n💰 Saldo atual: R$ {float(usuario['saldo']):.2f}")

# Inicialização
criar_arquivos()

# Exemplos de uso
cadastrar_usuario("José Silva", "12345678903", "0002")

depositar("0002", 1500)
sacar("0002", 200)
sacar("0002", 600) # Deve falhar por limite diário
sacar("0002", 500)
sacar("0002", 1300)  # Deve falhar por limite 

extrato("0002")