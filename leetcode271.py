# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from typing import List

def encode(strs: List[str]) -> str:
    result = ""
    
    for word in strs:
        result += str(len(word)) + '#' + word
    
    return result

def decode(s: str)-> List[str]:
    result = []
    i = 0
    
    while i<len(s):
        j = i
        while s[j] != '#':
            j+=1
            
        length = int(s[i:j])
        
        word = s[j+1: j+1+length]
        result.append(word)
        
        i = j + 1 + length
        
    return result

encoded = encode(["Hello", "World"])
print(encoded)

decoded = decode(encoded)
print(decoded)
