#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class Lotery:
	""" this class is representing the process"""
	def __init__(self):
		self.ret__M = 0
		self.res__M = 0
		self.esp__M = 0
#retorno = step(process executou) - step(process exc = 0)
	def work(self, process):
		step = 0
		tam = 0
		state = True
		value = 0.0
		while state:
			end = 1;
			lst = []
			for x in range(0, len(process), 1):
				if process[x].exc <= 0:
					if end == len(process):
						state = False
						break
					else:
						end = end + 1
						continue
				else:
					lst.append(x)		
			if state == False:
				break;
			i = random.randint(0, (len(lst)-1))
			if process[lst[i]].start_exc < 0 :
				process[lst[i]].set_start_exc(step+1)
			if (process[lst[i]].exc == 1):
				process[lst[i]].dec_exc(1)
				step += 1
			else:
				process[lst[i]].dec_exc(2)
				step += 2
			if process[lst[i]].exc == 0:
				print("processo: "+str(process[lst[i]].idt)+" Finalizou em "+str(step))
				value += ((step+1) - (process[lst[i]].arr+1))
		return value		




