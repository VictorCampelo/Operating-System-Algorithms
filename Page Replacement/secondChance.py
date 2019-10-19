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

	def searchRef(self, ref, mem):
		for ref_M in mem.get_frame():
			if(ref == ref_M):
				return True
		return False

	def clearBitR(self, pages):
		for page in pages:
			page.set_bit_R(0)

	def work(self, mem, pages):
        # Inicializa os valores de miss
		pag_F = 0
        #Quando a pagina referenciada nao esta na memoria
		# Percorre a lista de paginas referenciadas
		loop = 0
		for page in pages:
			loop+=1
			if not self.searchRef(page.get_ref(), mem):
				pag_F += 1 # incrementa o numero de paginas faltantes
                # Se todos os quadros estiverem ocupados remove a pagina mais antiga
				if len(mem.get_frame()) == mem.get_lgt():
					mem.get_frame().pop(0)
                # Adiciona a nova pagina
				mem.add_p_frame(page.get_ref())
            # inspecionar o bit de referência da página mais antiga
			elif page.get_bit_R() == 1:
        	#remove e adiona no final com R = 0
				mem.get_frame().remove(page.get_ref())
				page.set_bit_R(0)
				mem.add_p_frame(page.get_ref())
			else:
				mem.get_frame().remove(page.get_ref())
				page.set_bit_R(1)
			#zerar todos os bits R			
			if (loop%4 == 0):
				self.clearBitR(pages)
		# Retorna o numero de paginas nao encontradas na memoria RAM
		return pag_F


