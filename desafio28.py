#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys


import random

num = int(input('Digite um número:'))
sorteio = random.randint(0, 5)
print(sorteio)
if num == sorteio:
    print('Parabéns, o número pensado pelo computador foi {}! Você venceu!'.format(sorteio))
else:
    print('Poxa não foi dessa vez, você Perdeu!')
