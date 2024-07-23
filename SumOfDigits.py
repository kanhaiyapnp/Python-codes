# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 11:41:26 2021

@author: Kanhaiya
"""
def SUM_DIG(n):
    product = 1
    while ( n!=0):
        
         rem = n%10
         product = product*rem
         n=n//10
    return product         

         
def main():
    n= int(input())
    print(SUM_DIG(n))
    
if __name__=='__main__':
    main()