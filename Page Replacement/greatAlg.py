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

	def searchRef(self, ref, mem):
		for ref_M in mem.get_frame():
			if(ref == ref_M):
				return True
		return False

	def __seek_idx(self, frame, pages, i):
		ind = i
		count = 0
		j = 0
		for x in frame:
			aux = 0
			for y in xrange(i,len(pages)):
				#armazenar o indice da pagina que vai demorar a mais a ser referenciada novamente
				if x == pages[y].get_ref():
					if aux+j > count:
						count = aux+j
						ind = j
						break
				aux += 1
			j += 1			
		return ind
		
	def work(self, mem, pages):
		pag_F = 0
		i = 0
		for page in pages:
			print("tam1 = " + str(mem.get_lgt())+" - tam2 = " + str(len(mem.get_frame())))
			print(len(mem.get_frame()) == mem.get_lgt())
			if not self.searchRef(page.get_ref(), mem):
				if (len(mem.get_frame()) == mem.get_lgt()):
					idx = self.__seek_idx(mem.get_frame(), pages, i)
					del mem.get_frame()[idx]
				mem.add_p_frame(page.get_ref())
			i += 1
		return pag_F