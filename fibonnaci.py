#Exercício: Uma grande empresa de jogos está querendo tornar seus games mais desafiadores. Por isso ela contratou vc para
# desenvolver um algoritmo que será aplicado futuramente em diversos outros games: o algoritmo da sorte fibonnaci.
#A ideia dessa empresa, é claro, é fazer com que seja mais difícil os jogadores terem sucesso  nas ações que realizam nos games.
#Por isso o seu algoritmo deverá funcionar da seguinte forma: o usuário deve digitar um valor numérico inteiro e o algoritmo
#deverá verificar se esse valor encontra-se na sequência de Fibonnaci. Caso o número esteja na sequência, o algoritmo deve exibir
# a mensagem "Ação bem sucedida!" e, caso não esteja, deve exibir a mensagem "A ação falho...".

num1 = int(input("Digite um valor inteiro "))

fibonnaci = [0, 1]
i = num1

while num1 > fibonnaci[-1]:
    fibonnaci.append(fibonnaci[-1] + fibonnaci[-2])
    ultimo_fibonnaci = fibonnaci[-1]
if num1 == ultimo_fibonnaci:
    print("Ação bem sucedida!")
if num1 < ultimo_fibonnaci:
    if num1 != ultimo_fibonnaci:
        print("A ação falhou...")
