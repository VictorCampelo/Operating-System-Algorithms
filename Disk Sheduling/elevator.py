#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

'''
Segunda Chance - Uma modificação simples para o FIFO que evita o
problema de jogar fora uma página intensamente usada é inspecionar o bit
de referência da página mais antiga. Considere que o bit R de todas as
páginas é zerada a cada 4(quatro) referências à memória.
'''
class GreatAlg:

	def searchRef(self, page, mem):
		for pag in mem.get_frame():
			if(pag.get_ref() == page.get_ref()):
				return True
		return False

	def __seek_idx(self, frame, pages, i):
		ind = 0
		count = 0
		j = 0
		for x in frame:
			aux = 0
			for y in range(i,len(pages)-1):
				if y == len(pages)-1:
					ind = j
					return idn				
				elif x.get_ref() == pages[y].get_ref():
					if aux > count:
						count = aux
						ind = j
						break		
				aux += 1
			j += 1			
		return ind
		
	def work(self, mem, pages):
		pag_F = 0
		i = 0
		for page in pages:
			#print("tam1 = " + str(mem.get_lgt())+" - tam2 = " + str(len(mem.get_frame())))
			#print(int(len(mem.get_frame())) == int(mem.get_lgt()))
			if not self.searchRef(page, mem):
				pag_F += 1
				if int(len(mem.get_frame())) == int(mem.get_lgt()):
					idx = self.__seek_idx(mem.get_frame(), pages, i)
					del mem.get_frame()[idx]
				mem.add_p_frame(page)
			i += 1
		return pag_F