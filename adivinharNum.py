import random
numRandom = random.randint(0,200)
print("Digite um número")
getNum = int(input())

while (getNum != numRandom):
    
    if getNum < numRandom:
        print("Seu número é menor que o número gerado")
    else:
        print("Seu número é maior que o número gerado")
    getNum = int(input())

print("Esse é seu número: ", numRandom)