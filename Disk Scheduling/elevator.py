#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Elevator:
	def work(self, disk, seq):
		bit = 0#0=sobe 1 = desce
		count = 0
		while len(seq) > 0:
			if bit == 0:
				aux = max(seq)
				i = 0
				pos = 0
				test = False
				for cl in seq:
					if disk.get_s_cl() < cl:
						if cl - disk.get_s_cl() < aux:
							aux = cl - disk.get_s_cl()
							pos = i
							test = True
					i += 1
				if test: 	
					if disk.get_s_cl() < seq[pos]:
						count += seq[pos] - disk.get_s_cl()
						disk.set_s_cl(seq[pos])
						del seq[pos]
				else:
					bit = 1		
			else:
				aux = max(seq)
				i = 0
				pos = 0
				for cl in seq:
					if disk.get_s_cl() - cl < aux:
						aux = disk.get_s_cl() - cl 
						pos = i
					i += 1
				count += disk.get_s_cl() - seq[pos]
				disk.set_s_cl(seq[pos])
				del seq[pos]				
		return count		