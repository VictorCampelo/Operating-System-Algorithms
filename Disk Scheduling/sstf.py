#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Sstf:
	def work(self, disk, seq):
		count = 0
		while len(seq) > 0:
			aux = max(seq)
			i = 0
			pos = 0
			for cl in seq:
				if disk.get_s_cl() < cl:
					if cl - disk.get_s_cl() < aux:
						aux = cl - disk.get_s_cl()
						pos = i
				else:
					if disk.get_s_cl() - cl < aux:
						aux = disk.get_s_cl() - cl 
						pos = i
				i += 1
			if disk.get_s_cl() < seq[pos]:
				count += seq[pos] - disk.get_s_cl()
				disk.set_s_cl(seq[pos])
				del seq[pos]
			else:
				count += disk.get_s_cl() - seq[pos]
				disk.set_s_cl(seq[pos])
				del seq[pos]				
		return count		