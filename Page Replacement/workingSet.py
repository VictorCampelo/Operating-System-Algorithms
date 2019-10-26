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
		cndt1 = False
		cndt2 = False
		ifAllBitR1 = 0
		r1 = 0
		for x in mem.get_frame():
			if x.get_bit_R() == 0:
				cndt1 = True
				if (i-x.get_last_use()) > mem.get_lim():
					#remover essa pagina
					if count < i-x.get_last_use():
						count = i-x.get_last_use()
						ind = j
						cndt2 = True
				else:
					if not cndt2:#se não encontrar nenhuma candidato para remover
						if count < i-x.get_last_use():
							count = i-x.get_last_use()
							ind2 = j
			j += 1
			#se todos os bits r forem 1, procurar pelo mais velho
			if ifAllBitR1 < i-x.get_last_use():
				ifAllBitR1 = i-x.get_last_use()
				r1 = j	
		if cndt1:
			if cndt2:
				return ind
			else:
				return ind2			
		else:
			return r1

	def clearBitR(self, mem):
		for page in mem.get_frame():
			page.set_bit_R(0)		
		
	def work(self, mem, pages):
		pag_F = 0
		vt = 0
		for page in pages:
			if not self.searchRef(page, mem, vt):
				pag_F += 1
				if int(len(mem.get_frame())) == int(mem.get_lgt()):
					#percorrer lista para encontrar o melhor elemento para remover
					idx = self.__seek_idx(mem, pages, vt)
					del mem.get_frame()[idx]
				page.set_bit_R(1)
				page.set_last_use(vt)
				mem.add_p_frame(page)
			vt += 1
			if (vt)%4 == 0:
				self.clearBitR(mem)
		return pag_F