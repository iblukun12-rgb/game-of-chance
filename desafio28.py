#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys


import random

num = int(input('Digite um n�mero:'))
sorteio = random.randint(0, 5)
print(sorteio)
if num == sorteio:
    print('Parab�ns, o n�mero pensado pelo computador foi {}! Voc� venceu!'.format(sorteio))
else:
    print('Poxa n�o foi dessa vez, voc� Perdeu!')
