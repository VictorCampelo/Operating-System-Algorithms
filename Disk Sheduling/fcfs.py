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
		for cl in seq:
			if disk.get_s_cl() < cl:
				count += (cl - disk.get_s_cl())
				disk.set_s_cl(cl)
			else:
				count += (disk.get_s_cl() - cl)
				disk.set_s_cl(cl)
		return count		
	