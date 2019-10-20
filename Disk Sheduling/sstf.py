#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

'''
Segunda Chance - Uma modificação simples para o FIFO que evita o
problema de jogar fora uma página intensamente usada é inspecionar o bit
de referência da página mais antiga. Considere que o bit R de todas as
páginas é zerada a cada 4(quatro) referências à memória.
'''
class Fcfs:
	def work(self, disk, seq):
		count = 0
		aux = 0
		i = 0
		pos = 0
		while len(seq) > 0:
			for cl in seq:
				if disk.get_s_cl() < cl:
					
				else:
					pass	
		return count		