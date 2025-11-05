# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 11:23:07 2025

@author: Dela Eka Putri R
"""

def tampilkan_hasil(angka):
    def cek_prima(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    if cek_prima(angka):
        print(f"{angka} adalah bilangan prima.")
    else:
        print(f"{angka} bukan bilangan prima.")

bilangan = int(input("Masukkan bilangan: "))
tampilkan_hasil(bilangan)
