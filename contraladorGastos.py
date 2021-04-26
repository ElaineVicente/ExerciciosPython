qt_transacoes = int(input("Digite a quantidade de transações realizadas "))
i = 1
valor_total = 0
media_total = 0

for i in range(qt_transacoes):
    valor_transacao = int(input("Digite o valor da transação "))
    # alimentos = [i]
    valor_total = valor_total + valor_transacao
media_total = valor_total/qt_transacoes
print("Média das transações é: ", media_total)
print("Valor total gasto = ", valor_total)


