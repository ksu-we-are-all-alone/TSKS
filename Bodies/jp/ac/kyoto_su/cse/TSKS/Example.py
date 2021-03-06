#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from jp.ac.kyoto_su.cse.TSKS.Bodies.Dragon import DragonModel
from jp.ac.kyoto_su.cse.TSKS.Bodies.Wasp import WaspModel
from jp.ac.kyoto_su.cse.TSKS.Bodies.Bunny import BunnyModel
from jp.ac.kyoto_su.cse.TSKS.Bodies.Penguin import PenguinModel
from jp.ac.kyoto_su.cse.TSKS.Bodies.Oni import OniModel
from jp.ac.kyoto_su.cse.TSKS.Bodies.Baby import BabyModel
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


class Example(object):
	
	@classmethod
	def main(self):
		"""OpenGL立体データを読み込んで描画する。"""
		
		a_model = DragonModel()
		a_model.open()
		
		a_model = WaspModel()
		a_model.open()
	
		a_model = BunnyModel()
		a_model.open()
	
		a_model = PenguinModel()
		a_model.open()
	
		a_model = OniModel()
		a_model.open()
	
		a_model = BabyModel()
		a_model.open()
		
		glutMainLoop()
	
		return 0
