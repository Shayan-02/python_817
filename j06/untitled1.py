# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13MLv7gF7JPRybjaKDvYwVMQUTnjrjsft
"""

import numpy

a = 10
a

b = a + 10
b

def zarb(n):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      print(i * j, end= "\t")
    print()
zarb(10)

def sums(a=20, b=10):
  return a + b
sums(b=30)

