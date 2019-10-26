#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from process import Process

class RoundRobin:
	""" this class is representing the process"""
	def __init__(self):
		self.ret__M = 0
		self.res__M = 0
		self.esp__M = 0
#retorno = step(process executou) - step(process exc = 0)
	def work(self, process):
		ret = 0.0
		res = 0.0
		esp = 0.0
		i = 0
		step = 0
		inc = 0
		process.sort(key=lambda x: (x.arr,x.idt), reverse=False)
		while len(process) > 0:
			if process[i].start_exc < 0:
				process[i].set_start_exc(step)
				res += (step - process[i].arr)
			if process[i].exc == 1:
				process[i].dec_exc(1)
				step += 1
				inc = 1
			else:	
				process[i].dec_exc(2)
				step += 2
				inc = 2
			if process[i].exc == 0:
				ret += (step - process[i].arr)
				del process[i]
				for x in process:
					if x.arr <= step:
						if x.arr_aux%2 == 0 :
							esp += inc
						else:
							if inc == 2:
								esp += inc - x.arr_aux
								x.arr_to_pair()
							else:
								esp += inc	
				continue	
			else:
				for x in xrange(1,len(process)):
					if process[x].arr <= step:
						if process[x].arr_aux%2 == 0 :
							esp += inc
						else:
							if inc == 2:
								esp += inc - process[x].arr_aux
								process[x].arr_to_pair()
							else:
								esp += inc				
				pc = Process(process[i].idt, process[i].arr, process[i].exc)
				pc.set_start_exc(process[i].start_exc)
				del process[i]
				process.append(pc)	
		return (ret, res, esp)		