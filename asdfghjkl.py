# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:42:07 2021

@author: User
"""
class MrAgnewsClass():
    spines = 9
    
    def __init__ (self, aardvark):
        self.aardvark = aardvark
        
    def soap(self):
        print("i am " + self.aardvark + ", i have " + str(self.spines) + " spines." )
        
      
arthur = MrAgnewsClass("arthur")
sue  = MrAgnewsClass("arthur2")

if input() == "hello":
    arthur.soap()
    