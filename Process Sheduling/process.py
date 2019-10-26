#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Process:
	""" this class is representing the process"""
	def __init__(self, idt, arr, exc):
		self.idt = idt
		self.arr = arr
		self.exc = exc
		self.ret = 0
		self.res = 0
		self.esp = 0
		self.prt = -1
		self.start_exc = -1
		self.queue = 0

	def idt(self):
		return self.idt

	def arr(self):
		return self.arr

	def exc(self):
		return self.exc

	def ret(self):
		return self.ret

	def res(self):
		return self.res			

	def esp(self):
		return self.esp

	def queue(self):
		return self.queue			

	def set_pos_queue(self, value):
		self.queue += value

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