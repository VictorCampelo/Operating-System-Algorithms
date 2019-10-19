#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

class WorkingSet:

	def searchRef(self, page, mem, vt):
		for pag in mem.get_frame():
			if(pag.get_ref() == page.get_ref()):
				pag.set_bit_R(1)
				pag.set_last_use(vt)
				return True
		return False

	def __seek_idx(self, mem, pages, i):
		ind = 0
		ind2 = 0
		count = 0
		j = 0
		cndt = False
		for x in mem.get_frame():
			aux = 0
			if x.get_bit_R() == 1:
				x.set_last_use(i)
			else:
				if (i-x.get_last_use()) > mem.get_lim():
					#remover essa pagina
					ind = j
					cndt = True
					print("idade: "+str(i-x.get_last_use()))
					print("escolhido ref: "+str(ind))
					
				else:
					if not cndt:#se não encontrar nenhuma candidato para remover
						aux = x.get_last_use()-i
						if count < aux:
							count = aux
							ind2 = j
			j += 1
		if cndt:
			return ind
		else:
			return ind2

	def clearBitR(self, mem):
		for page in mem.get_frame():
			page.set_bit_R(0)		
		
	def work(self, mem, pages):
		pag_F = 0
		vt = 0
		for page in pages:
			if not self.searchRef(page, mem, vt):
				pag_F += 1
				a = ()
				for x in mem.get_frame():
					a += (x.get_ref(), x.get_last_use())
				print(a)	
				if int(len(mem.get_frame())) == int(mem.get_lgt()):
					#percorrer lista para encontrar o melhor elemento para remover
					idx = self.__seek_idx(mem, pages, vt)
					del mem.get_frame()[idx]
				else:
					page.set_bit_R(1)
					page.set_last_use(vt)
				mem.add_p_frame(page)
			vt += 1
			if vt%4 == 0:
				self.clearBitR(mem)
		return pag_F