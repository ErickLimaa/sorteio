import random
num1 = int(input("Digite um numeiro inteiro "))
sorteio = random.randint(0, 10)
if num1 == sorteio:
  print("Parabens, voce acertou")
else:
  print("Você errou!!! O valor certo é:", sorteio)
  
