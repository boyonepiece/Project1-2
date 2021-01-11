# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:58:59 2021

@author: Kahn Potter
"""

from __future__ import print_function
from huffman import HuffmanCoding
from buildSA import buildSA
import timeit

start = timeit.default_timer()

def rotations(t):
    tt = t*2
    return [ tt[i:i+len(t)] for i in range(0, len(t))]
    
def bwm(t):
    return sorted(rotations(t))

def bwt(t):
    return ''.join(map(lambda x: x[-1], bwm(t)))


def f1(s):
    return sorted([s[i-1:] for i in range(len(s),0,-1)])

def f2(s):
    l = len(s)
    return [l - len(t) for t in f1(s)]

def bwt1(s):
    return ''.join(s[i-1] for i in f2(s))


def bwt2(s):
    return ''.join(s[i-1] for i in buildSA(s, len(s)).build())

        
def move2front_encode(strng, symboltable, f_out, f_fre):
    frequency = {}
    #print(strng)
    for char in strng:
        indx = symboltable.index(char)
        if not indx in frequency:
            frequency[indx] = 0
        frequency[indx] += 1
        symboltable = [symboltable.pop(indx)] + symboltable
        
    #print(frequency)
    for character in frequency:
        f_out.write(str(character)+ ' ')
        f_fre.write(str(frequency.get(character))+' ') 

path1 = "test/500MB.txt"
path2 = 'bwt_mtf.txt'
path3 = 'frequency.txt'

f_in = open(path1,'r')
f_out = open(path2,'w+')
f_fre = open(path3,'w+')

  
T = f_in.read(3000)
#print(T+'$')
while T != '':
    SYMBOLTABLE = sorted(list(set(T)))
    #print(SYMBOLTABLE)
    move2front_encode(bwt(T), SYMBOLTABLE, f_out, f_fre)
    T = f_in.read(3000)
    
print('BWT-MTF completed!')

stop1 = timeit.default_timer()
print('Time BWT-MTF: ', stop1 - start)  


f_in.close()
f_out.close()   
f_fre.close()
    
h = HuffmanCoding(path2,path3)
  
output_path = h.compress()



stop = timeit.default_timer()

print('Time: ', stop - start)  
