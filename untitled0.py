# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 23:01:29 2021

@author: b.ellinger
"""

import matplotlib.pyplot as plt
import numpy as np

# rot * vec = vec1obj

Xs = [1,1,4]
Ys = [0,2,3]
theta = np.deg2rad(180) #degrees
rot = np.array([[np.cos(theta), np.sin(theta)],[np.sin(theta)*-1, np.cos(theta)]])

obj = np.array([[1,1,4], [0,2,3]])
obj_ = np.matmul(rot, obj)
plt.plot(obj[0], obj[1], '*-')
plt.plot(obj_[0], obj_[1], 'o-', c='red')
plt.plot(0,0, 'x')
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.hlines(0,-4,4, linestyles='dashed')
plt.vlines(0,-4,4, linestyles='dashed')