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
		value = 0.0
		while len(process) > 0:
			for x in range(0, len(process), 1):
				if process[x].arr == step:
					process[x].set_prt(len(process)+1)
			#ordena por prioridades	da mais alta para a menor
			process.sort(key=lambda x: x.prt, reverse=True)
			i = 0
			for x in range(1,(len(process)-1),1):
				if process[0].prt > process[x].prt:
					break
				else: #pega o que tiver menor indice
					if process[x].idt < process[i].idt:
						i = x
						break
			print("passo: "+str(step))
			print("id: "+str(process[i].idt))
			print("chegada: "+str(process[i].arr))
			print("prioridade: "+str(process[i].prt))
			if process[i].start_exc == -1:
				process[i].set_start_exc(step)
			process[i].dec_prt()
			process[i].dec_exc(1)
			print("nova prioridade: "+str(process[i].prt))
			if process[i].exc == 0:
				print("processo: "+str(process[i].idt)+" Finalizou em "+str(step))
				value += (step - process[i].arr)+1
				print("Valeu: "+str((step - process[i].arr)+1))
				del process[i]
				for x in range(0, len(process), 1):
				#encontra os processos que ainda não receberam prioridades
					if (process[x].prt > 0):
						process[x].inc_prt()
						print("incrementou o: "+str(process[x].idt))	
				step += 1
				print("\n")
				continue
			#incrementa as prioridades dos outros
			for x in range(0, len(process), 1):
				#encontra os processos que ainda não receberam prioridades
				if (process[x].prt > 0 and x != i):
					process[x].inc_prt()
					print("incrementou o: "+str(process[x].idt))	
			step += 1
			print("\n")	
		return value			