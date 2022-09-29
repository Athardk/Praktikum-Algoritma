# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:16:27 2022

@author: Athardk
"""

import math

t1 = float(input("masukkan garis lintang kota pertama = "))
g1 = float(input("masukkan garis bujur kota pertama ="))

t2 = float(input("masukkan garis lintang kota kedua ="))
g2 = float(input("masukkan garis bujur kota kedua ="))

dlat = t2 - t1
dlon = g2 - g1

a = math.sin(math.radians(dlat/2)) **2 - math.cos(math.radians(t1)) 
math.cos(math.radians(t2)) * math.sin(math.radians(dlon/2)) **2

c = 2 * math.asin(math.sqrt(a))
r = 6371.01

print("jarak antara dua titik adalah" ,c*r , "km")