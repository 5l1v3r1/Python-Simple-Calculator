#!/usr/bin/env python
# -*- coding:utf-8 -*-

simplecalculator_ico = """
#########################################################
#     PYTHON - SIMPLE CALCULATOR - GH0ST S0FTWARE       #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

print simplecalculator_ico

islem_numarasi_ico = """
(1) Toplama
(2) Çıkartma
(3) Çarpma
(4) Bölme
"""

print islem_numarasi_ico

star = "**********************************************";

print star	

islem_numarasi = input("Yapılcak işlem numarasını giriniz : ")

print star

def toplama():
	print star
	sayi_toplama = input("Toplama işlemi için ilk sayıyı giriniz : ")
	sayi_toplama = input("Toplama işlemi için ikici sayıyı giriniz : ")
	print star
	print "Sonuç : " , sayi_toplama, " + ", sayi_toplama, "=", sayi_toplama + sayi_toplama
	print star

def cikarma():
	print star
	sayi_cikartma = input("Çıkartma işlemi için ilk sayıyı giriniz : ")
	sayi_cikartma = input("Çıkartma işlemi için  sayıyı giriniz : ")
	print star	
	print "Sonuç : " , sayi_cikartma, " - ", sayi_cikartma, "=", sayi_cikartma - sayi_cikartma
	print star

def carpma():
	print star
	sayi_carpma = input("Çarpma işlemi için ilk sayıyı giriniz : ")
	sayi_carpma = input("Çarpma işlemi için ikinci sayıyı giriniz : ")
	print star	
	print "Sonuç = " , sayi_carpma, " X ", sayi_carpma, "=", sayi_carpma * sayi_carpma
	print star

def bolme():
	print star
	sayi_bolme = input("Bölme işlemi için ikinci sayıyı giriniz : ")
	sayi_bolme = input("Bölme işlemi için ikinci sayıyı giriniz : ")
	print star        
	print "Sonuç = " , sayi_bolme, " / ", sayi_bolme, "=", sayi_bolme / sayi_bolme
	print star

if islem_numarasi == 1:
	toplama()
 
elif islem_numarasi == 2:
	cikartma()
 
elif islem_numarasi == 3:
	carpma()
	
elif islem_numarasi == 4:
	bolme()

else:
	if islem_numarasi != 1 and 2 and 3 and 4:  
		print star
		hata_mesaji = "Gerçersiz işlem numarsı girdiniz. Tekrar deneyin.";
		print hata_mesaji
		print star
