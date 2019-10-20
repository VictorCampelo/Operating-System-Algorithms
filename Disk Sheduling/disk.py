#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Disk:
	""" this class is representing the process"""
	def __init__(self, n_cl, s_cl):
		self.n_cl = n_cl
		self.s_cl = s_cl

	def get_n_cl(self):
		return self.n_cl

	def get_s_cl(self):
		return self.s_cl	

	def set_n_cl(self, value):
		self.n_cl = value

	def set_s_cl(self, value):
		self.s_cl = value	