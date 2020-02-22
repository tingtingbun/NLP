#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 19:52:03 2020

the code is inspired by http://stevehanov.ca/blog/?id=114"""


class Trie:
    def __init__(self):
        self.word = None
        self.children = {}
    def insert(self, word):
        node = self
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Trie()
            node = node.children[letter]
        node.word = word



def task4(dictionary, raw):
	
    dic = Trie()
    
    for word in open(dictionary, 'rt').read().split():
        dic.insert(word)


    def helper(node, previous_letter, letter, word, double_prevRow,previous_row,step_out):
        cur_row = [previous_row[0]+1]
        
        for col in range(1,len(word)+1):
            if word[col -1]== letter:
                cost = 0
            else:
                cost = 1
            
            if word[col-1]==previous_letter and word[col-2]==letter:
                
                cur_row.append(min(cur_row[col-1]+1,previous_row[col]+1,previous_row[col-1]+cost,double_prevRow[col-2]+1))
            else:
                
                cur_row.append(min(cur_row[col-1]+1,previous_row[col]+1,previous_row[col-1]+cost))
            
        if node.word!= None:
            step_out.append(cur_row[-1])
            
        else:
            
            old_letter = letter
            for l in node.children:
                helper(node.children[l],old_letter,l,word,previous_row,cur_row,step_out)
        
    def search(word):

        cur_row = range(len(word)+1)
        step_out = []
        
        for l in dic.children:
            helper(dic.children[l],None,l,word,None,cur_row,step_out)

       
        return min(step_out)


    
    overall = []
    
    for word in open(raw,'rt').read().split():
        overall.append(search(word)) 
    return overall



