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
