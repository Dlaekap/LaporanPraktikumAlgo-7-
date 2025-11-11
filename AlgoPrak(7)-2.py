# -*- coding: utf-8 -*-
"""
Created on Tue Nov 11 20:48:30 2025

@author: Dela Eka Putri R
"""

def ordinal_suffix(number):
    if 11 <= number % 100 <= 13:
        suffix = 'th'
    elif number % 10 == 1:
        suffix = 'st'
    elif number % 10 == 2:
        suffix = 'nd'
    elif number % 10 == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
        
    return (number, suffix)

print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    input_angka = int(input("masukkan angka: "))
    
    if input_angka == 0:
        print(ordinal_suffix(0))
        break 
        
    hasil = ordinal_suffix(input_angka)
    print(hasil)
        
print("terima kasih telah menggunakan program saya")