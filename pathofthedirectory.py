# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:18:34 2021

@author: Quentin
"""
import os

# path of the given file
print(os.path.dirname(os.path.abspath("my_file.txt")))

# current working directory
print(os.path.abspath(os.getcwd()))