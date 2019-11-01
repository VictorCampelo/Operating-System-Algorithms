#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from process import Process
from dynPri import *
from lotery import *
from roundRobin import *
from copy import deepcopy

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

	pc = deepcopy(conv_to_matrix(in__data))
	pc1 = deepcopy(pc)
	pc2 = deepcopy(pc)

	dp = DynPri()
	tam = len(pc)
	(ret, res, esp) = dp.work(pc)

	outPut_dp = "PRI {0} {1} {2}"
	outPut_dp = outPut_dp.format((ret/tam), (res/tam), (esp/tam))	

	lt = Lotery()
	tam = len(pc1)
	(ret, res, esp) = lt.work(pc1)
	
	outPut_lt = "LOT {0} {1} {2}"
	outPut_lt = outPut_lt.format((ret/tam), (res/tam), (esp/tam))	

	rdn = RoundRobin()
	tam = len(pc2)
	(ret, res, esp) = rdn.work(pc2)
	
	outPut_rdn = "RR {0} {1} {2}"
	outPut_rdn = outPut_rdn.format((ret/tam), (res/tam), (esp/tam))

	output = "{0}\n{1}\n{2}"

	#print(output.format(outPut_dp, outPut_lt, outPut_rdn))

	with open('out.txt', 'w+') as file_w:
		file_w.write(output.format(outPut_dp, outPut_lt, outPut_rdn))



if __name__ == '__main__':
    main()