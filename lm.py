#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Zimeng Qiu <zimengq@andrew.cmu.edu>

"""
F19 11-411/611 NLP Assignment 3 Task 1
N-gram Language Model Implementation Script
Kinjal Jain Feb 2020

This is a simple implementation of N-gram language model

Write your own implementation in this file!
"""

import argparse

from utils import *
from collections import Counter
import numpy as np


class LanguageModel(object):
    """
    Base class for all language models
    """
    def __init__(self, corpus, ngram, min_freq, uniform=False):
        self.ngram= ngram
        txt = self.preprocess_txt(corpus, min_freq)
        self.processed_txt = txt
        self.vocab = set(txt) ## all the unique word
        
        if uniform: 
            self.n_gram_model = Counter()
            for index in range(len(txt)-(ngram-1)):
                self.n_gram_model[tuple(txt[index:index+ngram])] += 1
            self.unique_ngram_vocab = len(self.n_gram_model)
    
        else:
        ## building n_gram model 
            self.n_gram_model = Counter()
            
        
            for index in range(len(txt)-(ngram-1)):
                self.n_gram_model[tuple(txt[index:index+ngram])] += 1
            self.actual_frequency = self.n_gram_model.copy()
        
            self.frequency_helper = Counter()
            for index in range(len(txt)-(ngram-1)):
                    self.frequency_helper[tuple(txt[index:index+ngram-1])] += 1
        
      
            self.unique_ngram_vocab = len(self.actual_frequency)
        
        
    def preprocess_txt(self,corpus,min_freq):
        frequency = Counter()
        words_list = [word for doc in corpus for word in doc]
        frequency.update(words_list)
        rare_words = [key for key in frequency.keys() if frequency[key] < min_freq]
        new_list = []
        for word in words_list:
            if word in rare_words:
                new_list.append('UNK')
            else:
                new_list.append(word)
        return new_list
    
    def preprocess_training(self, text):
        
        
        new_list = []
        for word in text:
            if word not in self.vocab:
                new_list.append('UNK')
            else:
                new_list.append(word)
        return new_list
    
    def calculate_uniform_probability(self, sentence):
        
        
        log_sum = 0
        
        sentence = self.preprocess_training(sentence)
        
        for i in range(len(sentence)-self.ngram+1):
            log_sum += np.log(1/self.unique_ngram_vocab)
    
        return log_sum
    
    
    def calculate_sentence_probability(self,sentence):
        
        log_sum = 0
        previous = []
        sentence = self.preprocess_training(sentence)
        
        for word in sentence:
            
            if len(previous) != self.ngram-1:
                previous.append(word)
            
            else:
                previous.append(word)
                numerator = self.actual_frequency[tuple(previous)]+0.00001
                denominator = self.frequency_helper[tuple(previous[0:self.ngram-1])]\
                                                            + 0.00001*self.unique_ngram_vocab
                
                
                log_sum += np.log(numerator/denominator) 
                del previous[0]

        return log_sum
        
                

    def most_common_words(self, k):
        """
        This function will only be called after the language model has been built
        Your return should be sorted in descending order of frequency
        Sort according to ascending alphabet order when multiple words have same frequency
        :return: list[tuple(token, freq)] of top k most common tokens
        """
        # Write your own implementation here

        raise NotImplemented


def calculate_perplexity(models, coefs, data):
    """
    Calculate perplexity with given model
    :param models: language models
    :param coefs: coefficients
    :param data: test data
    :return: perplexity
    """
       
    data = [ele for doc in data for ele in doc]
    sum_prob = coefs[0]*models[0].calculate_uniform_probability(data) + \
    coefs[1]*models[1].calculate_sentence_probability(data) +\
    coefs[2]*models[2].calculate_sentence_probability(data) +\
    coefs[3]*models[3].calculate_sentence_probability(data) 
    
  
    return np.exp(-sum_prob/(len(data)))
        
    # Write your own implementation here

    raise NotImplemented


# Do not modify this function!
def parse_args():
    """
    Parse input positional arguments from command line
    :return: args - parsed arguments
    """
    parser = argparse.ArgumentParser('N-gram Language Model')
    parser.add_argument('coef_unif', help='coefficient for the uniform model.', type=float)
    parser.add_argument('coef_uni', help='coefficient for the unigram model.', type=float)
    parser.add_argument('coef_bi', help='coefficient for the bigram model.', type=float)
    parser.add_argument('coef_tri', help='coefficient for the trigram model.', type=float)
    parser.add_argument('min_freq', type=int,
                        help='minimum frequency threshold for substitute '
                             'with UNK token, set to 1 for not use this threshold')
    parser.add_argument('testfile', help='test text file.')
    parser.add_argument('trainfile', help='training text file.', nargs='+')
    args = parser.parse_args()
    return args


# Main executable script provided for your convenience
# Not executed on autograder, so do what you want
if __name__ == '__main__':
    # parse arguments
    args = parse_args()

    # load and preprocess train and test data
    train = preprocess(load_dataset(args.trainfile))
    test = preprocess(read_file(args.testfile))

    # build language models
    uniform = LanguageModel(train, ngram=1, min_freq=args.min_freq, uniform=True)
    unigram = LanguageModel(train, ngram=1, min_freq=args.min_freq)
    bigram = LanguageModel(train, ngram=2, min_freq=args.min_freq)
    trigram = LanguageModel(train, ngram=3, min_freq=args.min_freq)

    # calculate perplexity on test file
    ppl = calculate_perplexity(
        models=[uniform, unigram, bigram, trigram],
        coefs=[args.coef_unif, args.coef_uni, args.coef_bi, args.coef_tri],
        data=test)

    print("Perplexity: {}".format(ppl))
   
    





