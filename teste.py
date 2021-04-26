for i in range(len(fibonnaci)):
    if num1 > fibonnaci[-1]:
        fibonnaci.append(fibonnaci[-1] + fibonnaci[-2])
print(fibonnaci)
