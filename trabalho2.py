# -*- coding: utf-8 -*-
# função que calcula área de uma coroa circular ac
# dado os raios r1 e r2, onde r1 é maior que r2
def areadacoroa(r1,r2):
  return 3.14*r1**2 - 3.14*r2**2

a1 = input("digite r1: ")
a2 = input("digite r2: ")
ac = areadacoroa(a1,a2)

print("area da coroa e :",ac)
