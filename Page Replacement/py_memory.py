#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Page:
	""" this class is representing the process"""
	def __init__(self, ref):
		self.ref = ref
		self.bit_R = 0
		self.bit_M = 0
		self.n_ins = 0
		self.last_use = 0
	
	def get_last_use(self):
		return self.last_use

	def set_last_use(self, value):
		self.last_use = value

	def get_ref(self):
		return self.ref	

	def get_n_ins(self):
		return self.n_ins		

	def set_bit_R(self, value):
		self.bit_R = value	
	
	def get_bit_R(self):
		return self.bit_R

	def set_N_Ins(self, value):
		self.n_ins = value	

class Memory:
	""" this class is representing the process"""
	def __init__(self, lgt):
		self.lgt = lgt
		self.frame = []
		self.lim = (int(lgt)/2)+1

	def get_lim(self):
		return self.lim

	def get_lgt(self):
		return self.lgt

	def get_frame(self):
		return self.frame

	def add_p_frame(self, page):
		self.frame.append(page)