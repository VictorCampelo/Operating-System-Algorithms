#!/usr/bin/env python
# -*- coding: utf-8 -*-
class DynPri:
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
		while state:
			end = 1;
			for x in range(0, len(process), 1):
				if process[x].exc <= 0:
					if end == len(process):
						state = False
						break
					else:
						end = end + 1
						continue
			if state == False:
				break;
			if (tam <= len(process)):
				aux = 0
				process.sort(key=lambda x: x.arr)
				for x in range(tam, len(process), 1):
					if process[x].arr == step:
						process[x].set_prt(len(process)+1)
						aux = aux + 1
				tam = tam + aux
			process.sort(key=lambda x: x.prt, reverse=True)
			i = 0
			for x in xrange(1,len(process)):
				if process[0].prt > process[x].prt:
					break
				else:
					if process[x].idt < process[i].idt:
						i = x
			print("passo: "+str(step))
			print("id: "+str(process[i].idt))
			print("chegada: "+str(process[i].arr))
			print("prioridade: "+str(process[i].prt))
			print("\n")
			if process[i].start_exc < 0 :
				process[i].set_start_exc(step+1)
			process[i].dec_prt()
			process[i].dec_exc(1)
			if process[i].exc == 0:
				print("processo: "+str(process[i].idt)+" Finalizou em "+str(step))
				process[i].set_ret((step+1) - (process[i].arr+1))
				process[i].set_prt(-1)
			#incrementa as prioridades dos outros
			for x in range(0, len(process), 1):
				#encontra os processos que ainda não receberam prioridades
				if (process[x].prt < 0 or x == i):
					continue	
				process[x].inc_prt()
			step = step + 1			








