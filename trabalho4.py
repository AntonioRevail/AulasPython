# Essa função calcula o troco e a quantidades
# de bombons, dado o dinheiro que você tem
# e o preço do bombom.

def numero_bombons(dinheiro,preco):
  numero_bombons = int(dinheiro/preco)
  troco = dinheiro - (numero_bombons*preco)
  return(numero_bombons,troco)

dinheiro = input("digite seu dinheiro = ")
preco =input ("digite o preco do bombom = ")

print numero_bombons(dinheiro,preco)
