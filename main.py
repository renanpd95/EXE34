
import os
km = float(input("Qual a quantidade de km percorrido? "))
dias = int(input("Qual a quantidade de dias alugados? "))
os.system('clear')
result1 = km * 0.15
result2 = dias * 60
soma = result1+result2

print ("O valor a ser pago pelo aluguel do carro é: R$",soma)