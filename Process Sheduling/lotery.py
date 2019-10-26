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
		inc = 0
		ret = 0.0
		res = 0.0
		esp = 0.0
		while len(process) > 0:
			end = 1;
			lst = []
			for x in range(0, len(process), 1):
				if process[x].arr <= step:
					lst.append(x)	
			i = random.randint(0, (len(lst)-1))
			#print("random: "+str(i))
			if process[lst[i]].start_exc < 0 :
				process[lst[i]].set_start_exc(step+1)
				res += (step - process[lst[i]].arr)
			if (process[lst[i]].exc == 1):
				process[lst[i]].dec_exc(1)
				step += 1
				inc = 1
			else:
				process[lst[i]].dec_exc(2)
				step += 2
				inc = 2
			if process[lst[i]].exc == 0:
				#print("processo: "+str(process[lst[i]].idt)+" Finalizou em "+str(step))
				ret += (step - process[lst[i]].arr)+1
				del process[lst[i]]
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
			else:	
				for x in xrange(0,len(process)):
					if x != lst[i]:
						if process[x].arr <= step:
							if process[x].arr_aux%2 == 0 :
								esp += inc
							else:
								if inc == 2:
									esp += inc - process[x].arr_aux
									process[x].arr_to_pair()
								else:
									esp += inc
		return (ret, res, esp)		




