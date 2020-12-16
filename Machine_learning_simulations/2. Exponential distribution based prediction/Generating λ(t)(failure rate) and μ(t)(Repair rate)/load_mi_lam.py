# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 14:35:39 2020

@author: Freedom
"""

import numpy as np

a1 = np.load('Repair_rates15dt10080h.npy15.npy')
print(a1.shape)

a3 = np.load('Repair_rates15dt21600h.npy15.npy')
print(a3.shape)

a2 = np.load('Repair_rates15dt43200h.npy15.npy')
print(a3.shape)

a4 = np.load('Repair_rates30dt10080h.npy30.npy')
print(a4.shape)

a5 = np.load('Repair_rates30dt21600h.npy30.npy')
print(a5.shape)

a6 = np.load('Repair_rates30dt43200h.npy30.npy')
print(a6.shape)

a7 = np.load('Repair_rates60dt10080h.npy60.npy')
print(a7.shape)

a8 = np.load('Repair_rates60dt21600h.npy60.npy')
print(a8.shape)