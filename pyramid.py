# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def pyramid(s):
    d = {}
    for char in s:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
            
    sorted_d = sorted(d.items(), key=lambda x: x[1])        
    
    for k in range(len(sorted_d)):
        if k+1 != sorted_d[k][1]:
            return False
    return True
    
    
if __name__ == '__main__':
    ip = input()
    if pyramid(ip):
        print('True')
    else:
        print('False')
    