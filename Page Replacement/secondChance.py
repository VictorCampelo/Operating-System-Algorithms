#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

'''
Segunda Chance - Uma modificação simples para o FIFO que evita o
problema de jogar fora uma página intensamente usada é inspecionar o bit
de referência da página mais antiga. Considere que o bit R de todas as
páginas é zerada a cada 4(quatro) referências à memória.
'''
class SecondChance:

	def searchRef(self, page, mem):
		for pag in mem.get_frame():
			if(page.get_ref() == pag.get_ref()):
				return True
		return False

	def clearBitR(self, mem):
		for page in mem.get_frame():
			page.set_bit_R(0)

	def seach_set_BitR(self, page, mem):
		for pag in mem.get_frame():
			if page.get_ref() == pag.get_ref():
				pag.set_bit_R(1)
				return True
		return False
				
	def work(self, mem, pages):
        # Inicializa os valores de miss
		pag_F = 0
        #Quando a pagina referenciada nao esta na memoria
		# Percorre a lista de paginas referenciadas
		loop = 0
		i = 0
		for page in pages:
			loop+=1
			if not self.searchRef(page, mem):
				pag_F += 1 
				if int(len(mem.get_frame())) == int(mem.get_lgt()):
					v = 0
					while v < len(mem.get_frame())-1:
						if mem.get_frame()[0].get_bit_R() == 1:
							p = mem.get_frame()[0]
							mem.get_frame()[0].set_bit_R(0) #tira do final
							del mem.get_frame()[0] #colocar o bit r = 0 
							mem.add_p_frame(p) #da a segunda chance
						v += 1
					mem.get_frame()[0].set_bit_R(0)	
					del mem.get_frame()[0] # o que sobrou como mais velho é removido
					page.set_bit_R(1)
					mem.add_p_frame(page) # adiciona a nova pagina no inicio
				else:
					page.set_bit_R(1)
					mem.add_p_frame(page)
            # inspecionar o bit de referência da página mais antiga
			else:
				self.seach_set_BitR(page, mem)
			if (loop%4 == 0):
				self.clearBitR(mem)
		# Retorna o numero de paginas nao encontradas na memoria RAM
		return pag_F


