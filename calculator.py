def divi(a, b):
    return a / b

def multi(a, b):
   
   return a * b

def sub(a, b): 
    return a - b

def soma (a, b):
    return a + b 

print("Escolha o valor de A: ")
a = int(input())
print("Escolha o valor de B: ")
b = int(input())

print("Escolha uma operação: ")
entrada = input()

if (entrada == "soma"): 
    print("seu resultado é: ", soma(a, b))

elif(entrada == "sub"):
    print("seu resultado é: ", sub(a, b))

elif(entrada == "multi"):
   
   print("seu resultado é: ", multi(a, b))

elif(entrada == "divi"):
    print("seu resultado é: ", divi(a, b))