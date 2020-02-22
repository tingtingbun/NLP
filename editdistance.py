#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:36:53 2020

@author: tingtinggu
"""

class EditDistance():
	
    def __init__(self):
        '''sdf'''
		
    def calculateLevenshteinDistance(self, str1, str2):
        d = []
        for n in range(len(str1)+1):
            d_n = []
            for m in range(len(str2)+1):
                d_n.append(0)
            d.append(d_n)
        for n in range(len(str1)+1):
            d[n][0]=n 
        for m in range(len(str2)+1):
            d[0][m]=m
        for n_ in range(1,len(str1)+1):
            for m_ in range(1,len(str2)+1):
                if str1[n_-1]==str2[m_-1]:
                    cost = 0 
                else:
                    cost = 1 
                d[n_][m_]= min(d[n_-1][m_]+1, d[n_][m_-1]+1, d[n_-1][m_-1]+cost)
        return d[len(str1)][len(str2)]
    
    def calculateOSADistance(self, str1, str2):
        d = []
        for n in range(len(str1)+1):
            d_n = []
            for m in range(len(str2)+1):
                d_n.append(0)
            d.append(d_n)
        for n in range(len(str1)+1):
            d[n][0]=n 
        for m in range(len(str2)+1):
            d[0][m]=m
        for n_ in range(1,len(str1)+1):
            for m_ in range(1,len(str2)+1):
                if str1[n_-1]==str2[m_-1]:
                    cost = 0 
                else:
                    cost = 1 
                d[n_][m_]= min(d[n_-1][m_]+1, d[n_][m_-1]+1, d[n_-1][m_-1]+cost)
                
                if str1[n_-1] == str2[m_-2] and str1[n_-2]==str2[m_-1]:
                    d[n_][m_] = min(d[n_][m_],d[n_-2][m_-2]+1)
    

        return d[len(str1)][len(str2)]
    
    def calculateDLDistance(self, str1, str2):
        dic = {}
        d = []
    
        for al in set(list(str1)+list(str2)):
            dic[al] = 0 
    
        for n in range(len(str1)+2):
            d_n = []
            for m in range(len(str2)+2):
                d_n.append(0)
        
            d.append(d_n)

        d[0][0] = len(str1)+len(str2)
        for n in range(len(str1)+2):
            d[n][1]=n
            d[n][0]=len(str1)+len(str2)
        
    
        for m in range(len(str2)+2):
            d[1][m]=m
            d[0][m]=len(str1)+len(str2)
    
    
        
    
    
        for n_ in range(1,len(str1)+1):
            db = 0 
            for m_ in range(1,len(str2)+1):
                n1 = dic[str2[m_-1]]
                m1 = db
                cost = 0 
                if str1[n_-1] == str2[m_-1]:
                    db = m_-1
                else: 
                    cost = 1
            
                d[n_][m_] = min(d[n_-1][m_]+1, d[n_][m_-1]+1, 
                             d[n_-1][m_-1]+cost,
                             d[n_-1][m_-1]+(n-n1-1)+(m-m1-1)+1)
            
           
            dic[str1[n_-1]] = n_
    
        return d[len(str1)][len(str2)] 
    


                    
