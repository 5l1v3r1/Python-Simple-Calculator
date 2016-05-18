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
	sayi_toplama_1 = input("Toplama işlemi için ilk sayıyı giriniz : ")
	sayi_toplama_2 = input("Toplama işlemi için ikici sayıyı giriniz : ")
	print star
	print "Sonuç : " , sayi_toplama_1, " + ", sayi_toplama_2, "=", sayi_toplama_1 + sayi_toplama_2
	print star

def cikarma():
	print star
	sayi_cikartma_1 = input("Çıkartma işlemi için ilk sayıyı giriniz : ")
	sayi_cikartma_2 = input("Çıkartma işlemi için  sayıyı giriniz : ")
	print star	
	print "Sonuç : " , sayi_cikartma_1, " - ", sayi_cikartma_2, "=", sayi_cikartma_1 - sayi_cikartma_2
	print star

def carpma():
	print star
	sayi_carpma_1 = input("Çarpma işlemi için ilk sayıyı giriniz : ")
	sayi_carpma_2 = input("Çarpma işlemi için ikinci sayıyı giriniz : ")
	print star	
	print "Sonuç = " , sayi_carpma_1, " X ", sayi_carpma_2, "=", sayi_carpma_1 * sayi_carpma_2
	print star

def bolme():
	print star
	sayi_bolme_1 = input("Bölme işlemi için ikinci sayıyı giriniz : ")
	sayi_bolme_2 = input("Bölme işlemi için ikinci sayıyı giriniz : ")
	print star        
	print "Sonuç = " , sayi_bolme_1, " / ", sayi_bolme_2, "=", sayi_bolme_1 / sayi_bolme_1
	print star

if islem_numarasi == 1:
	toplama()
 
elif islem_numarasi == 2:
	cikarma()
 
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
