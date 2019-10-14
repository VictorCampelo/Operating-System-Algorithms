#!/usr/bin/env python
# -*- coding: utf-8 -*-
''''
	• Tempo de retorno médio – Refere-se ao tempo transcorrido entre o momento da
entrada do processo no sistema e o seu término.
	• Tempo de resposta médio – Intervalo de tempo entre a chegada do processo e o início
de sua execução.
	• Tempo de espera médio – Soma dos períodos em que um processo estava no seu
estado pronto.
'''
import sys
from process import Process
from dynPri import *
from lotery import *
from roundRobin import *

def conv_to_matrix(data):
	process__Mtx = []
	tmp = []
	i = 0
	for x in data:
		x = x.replace("\n", "")
		x = x.split(" ")
		x = map(int, x)
		pcs = Process(i+1, x[0], x[1])
		process__Mtx.append(pcs)
		i = i + 1
	process__Mtx.sort(key=lambda x: x.arr)

	return process__Mtx	

def main():
	in__data = sys.stdin.readlines()

	
	pc = conv_to_matrix(in__data)
	dynPri = []
	lotery = []
	roundRobin = []
	dp = DynPri()
	dp.work(pc)
	mid = 0.0
	for x in pc:
		mid += x.ret
		print(x.ret)
	print(str(mid/len(pc)))


	pc1 = conv_to_matrix(in__data)
	lt = Lotery()
	lt.work(pc1)
	mid = 0.0 
	for x in pc1:
		mid += x.ret
		print(x.ret)
	print(str(mid/len(pc1)))	


	pc2 = conv_to_matrix(in__data)
	rdn = RoundRobin()
	rdn.work(pc2)
	mid = 0.0
	for x in pc2:
		mid += x.ret
		print(x.ret)
	print(str(mid/len(pc2)))	


if __name__ == '__main__':
    main()