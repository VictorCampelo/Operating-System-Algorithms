#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Process:
	""" this class is representing the process"""
	def __init__(self, idt, arr, exc):
		self.idt = idt
		self.arr = arr
		self.arr_aux = arr
		self.exc = exc
		self.prt = -1
		self.start_exc = -1

	def idt(self):
		return self.idt

	def arr(self):
		return self.arr

	def arr_aux(self):
		return self.arr_aux		

	def arr_to_pair(self):
		self.arr_aux += 1

	def exc(self):
		return self.exc

	def start_exc(self):
		return self.start_exc	

	def dec_exc(self, value):
		self.exc = self.exc - value	

	def prt(self):
		return self.prt	

	def set_prt(self, value):
		self.prt = value

	def set_ret(self, value):
		self.ret = value	

	def set_start_exc(self, value):
		self.start_exc = value	

	def dec_prt(self):
		self.prt = self.prt - 1

	def inc_prt(self):
		self.prt = self.prt + 1		