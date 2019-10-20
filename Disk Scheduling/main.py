#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from copy import deepcopy
from disk import *
from fcfs import *
from sstf import *
from elevator import *

def main():
	n_cl= int(sys.stdin.readline()) #cria a memoria com seu tamanho
	s_cl = int(sys.stdin.readline())
	seq = map(int, sys.stdin.readlines())

	dks1 = Disk(n_cl, s_cl)
	dks2 = Disk(n_cl, s_cl)
	dks3 = Disk(n_cl, s_cl)
	
	s1 = deepcopy(seq)
	s2 = deepcopy(seq)
	s3 = deepcopy(seq)

	fcfs = Fcfs()
	n1 = fcfs.work(dks1, s1)
	print(n1)

	sstf = Sstf()
	n2 = sstf.work(dks2, s2)
	print(n2)

	elv = Elevator()
	n2 = elv.work(dks3, s3)
	print(n2)

if __name__ == '__main__':
    main()