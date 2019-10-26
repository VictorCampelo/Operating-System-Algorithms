#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class RoundRobin:
	""" this class is representing the process"""
	def __init__(self):
		self.ret__M = 0
		self.res__M = 0
		self.esp__M = 0
#retorno = step(process executou) - step(process exc = 0)
	def work(self, process):
		state = True
		value = 0.0
		process.sort(key=lambda x: (x.arr,x.idt), reverse=False)
		'''for x in xrange(0,len(process)):
			for y in xrange(x,len(process)):
				if (process[x].arr == process[y].arr):
					if(process[x].idt > process[y].idt):
						aux = []
						aux = process[x]
						process[x] = process[y]
						process[y] = aux'''
		for x in xrange(0,len(process)):
			process[x].set_pos_queue(x)				
		loop = 0
		end = 1
		step = 0
		while state:
			#o que ta no 0 executa e recebe o valor final
			#todos os outros diminui o valor na pos_queue
			if process[loop].exc <= 0:
				loop += 1 #vai pro proximo processo
				end += 1 #aumenta o numero de processos finalizados
				if end == len(process):
					break
				continue
			else:
				if process[loop].start_exc < 0:
					process[loop].set_start_exc(step+1)
				if process[loop].exc == 1:
					process[loop].dec_exc(1)
					step += 1
				else:	
					process[loop].dec_exc(2)
					step += 2
				if process[loop].exc == 0:
					value += ((step+1) - (process[loop].arr+1))	
				for x in xrange(0,len(process)):
					if x == loop:
						continue
					process[x].set_pos_queue(-1) #diminui a posição da fila de todos os outros
				process[loop].set_pos_queue(len(process)-1) #final da fila
				if (loop == (len(process)-1)): #chegou no final da fila = reinicia
					loop = 0
				end = 1
				loop += 1
		return value		