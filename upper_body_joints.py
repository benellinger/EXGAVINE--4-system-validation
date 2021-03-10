# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:54:19 2020

@author: B.Ellinger

This script will determine joint coordinate systems (jcs) of three joints: 
    shoulder, elbow, wrist. In a next step we will apply rotational calculations 
    to those jcs. As a result we will obtain cardan angles. With these cardan angles 
    we will calculate joint angles. The definiton of the jcs's and the joint angles 
    will follow the recommendations of the ISB.
"""

"""
list of implementations
. handle data gaps --> gap filling
. make log file for gaps
. take care of strange data
"""

import pandas as pd
import numpy as np


class QTM:
    """
    This class imports exported data from QTM (*.tsv) and calculates joint angles 
    as output
    """
    def __init__(self, fID):
        self.fID = fID
        self.df = pd.read_csv(fID, skiprows=10, delimiter='\t')
        
    def generate_jcs(self, markerset1, markerset2):
        """based on markerset we compute direction vectors. 
        The order of input matters: first component will be subtracted from last.
        """
        marker_11 = self.df.loc[:,self.df.columns.str.match(markerset1[0])]
        marker_12 = self.df.loc[:,self.df.columns.str.match(markerset1[1])]  
        marker_21 = self.df.loc[:,self.df.columns.str.match(markerset2[0])]
        marker_22 = self.df.loc[:,self.df.columns.str.match(markerset2[1])]
        columns = marker_11.columns.to_list() + marker_12.columns.to_list() \
            + marker_21.columns.to_list() + marker_22.columns.to_list()
        if self.df[columns].isnull().sum().any():
            print('CAUTION. nan-Values found in \n %s' %self.fID)
        
        self.base_1 = marker_12.to_numpy() - marker_11.to_numpy()
        self.base_2 = marker_22.to_numpy() - marker_21.to_numpy()
        
        return self.base_1, self.base_2
    
    def joint_angle(self, movement='flexion'):
        """
        Parameters
        ----------
        components1 : list
            components of first marker. Must be 2D.
        components2 : list
            components of second marker. Must be 2D.
    
        Returns
        -------
        numpy.array, 1D 
        """
        if movement == 'abduction':
            vec1 = self.base_1[:, [1,2]]
            vec2 = self.base_2[:, [1,2]]
        elif movement == 'flexion':
            vec1 = self.base_1[:, [0,2]]
            vec2 = self.base_2[:, [0,2]]
        vec1, vec2 = vec1 / np.linalg.norm(vec1), vec2 / np.linalg.norm(vec2) 
        alphas = np.zeros((len(vec1),1))
        # compute joint angle frame by frame
        for i in range(len(vec1)):
            v1, v2 = vec1[i,:], vec2[i,:]
            alpha = np.arccos( np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))
            alphas[i] = np.rad2deg(alpha)
        return alphas


# file = 'data/qu/flexion_statisch_gestreckt_0001.tsv'
# test = QTM(file)
# test.generate_jcs(['T8', 'C7'], ['LEL', 'ACR'])
# import matplotlib.pyplot as plt
# plt.plot(test.joint_angle('flexion'))
# a=test.joint_angle('flexion')