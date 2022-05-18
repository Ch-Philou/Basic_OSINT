#!/usr/bin/env python
#-*- coding: utf-8 -*-

import readline
import sys,os
import codecs
import argparse


def main():
	print("Argument Reading")
	parser = argparse.ArgumentParser(
		# prog='Target_add',
		add_help = True,
		description = "-------------------------",
		epilog='''\
		 blabla\r\n
		 balbla\r\n
		 ''')

	parser.add_argument('-fi',  '--file_in',		type=str, action="store", default="."+os.sep+"CPE_List.csv",   help='File to save data to')
	parser.add_argument('-s',   '--separator',		type=str, action="store", default=',',							help='Separator in CSV')
	parser.add_argument('-cp',  '--cpe_part',		type=str, action="store", default='',							help='Search in part (o/a/h)')
	parser.add_argument('-cven','--cpe_vendor',		type=str, action="store", default='',							help='Search in vendor')
	parser.add_argument('-cpr', '--cpe_product',	type=str, action="store", default='',							help='Search in Product')
	parser.add_argument('-cver','--cpe_version',	type=str, action="store", default='',							help='Search in version')
	parser.add_argument('-cu',  '--cpe_update',		type=str, action="store", default='',							help='Search in update')
	parser.add_argument('-ce',  '--cpe_edition',	type=str, action="store", default='',							help='Search in edition')
	parser.add_argument('-cl',  '--cpe_lang',		type=str, action="store", default='',							help='Search in lang')
	parser.add_argument('-cswe','--cpe_sw_edi',		type=str, action="store", default='',							help='Search in sw_edition')
	parser.add_argument('-ctsw','--cpe_target_sw',	type=str, action="store", default='',							help='Search in Target_SW')
	parser.add_argument('-cthw','--cpe_target_hw',	type=str, action="store", default='',							help='Search in Target_HW')
	parser.add_argument('-co',  '--cpe_other',		type=str, action="store", default='',							help='Search in Other')
	parser.add_argument('-lf',							  action="store_true",						 		help='Use LF instead of CRLF for new line')
	options = parser.parse_args()

	CSV_File = options.file_in
	Separator = options.separator

	if not os.path.exists(CSV_File):
		print("File does not exist "+str(CSV_File))
		sys.exit(1)
	
	print("-"*40)
	print(" Reading CPE")
	print("-"*40)
	print("XML file (input)  is "+str(CSV_File))
	print("-"*40)
	fic_in = codecs.open(CSV_File,"r",encoding="UTF-8")
	cpe_offset = 2
	myline = fic_in.readline()
	while myline:
		datas = myline.split(Separator)
		store_the_line = False
		
		if len(options.cpe_part)>0:	
			if options.cpe_part.lower() == datas[cpe_offset].lower():				store_the_line=True
		
		if len(options.cpe_vendor)>0:
			if options.cpe_vendor.lower() in datas[cpe_offset+1].lower():	store_the_line=True
		
		if len(options.cpe_product)>0:
			if options.cpe_product.lower() in datas[cpe_offset+2].lower():	store_the_line=True
		
		if len(options.cpe_version)>0:
			if options.cpe_version.lower() in datas[cpe_offset+3].lower():	store_the_line=True

		if len(options.cpe_update)>0:
			if options.cpe_update.lower() in datas[cpe_offset+4].lower():	store_the_line=True

		if len(options.cpe_edition)>0:
			if options.cpe_edition.lower() in datas[cpe_offset+5].lower():	store_the_line=True

		if len(options.cpe_lang)>0:
			if options.cpe_lang.lower() in datas[cpe_offset+6].lower():	store_the_line=True

		if len(options.cpe_sw_edi)>0:
			if options.cpe_sw_edi.lower() in datas[cpe_offset+7].lower():	store_the_line=True

		if len(options.cpe_target_sw)>0:
			if options.cpe_target_sw.lower() in datas[cpe_offset+8].lower():	store_the_line=True

		if len(options.cpe_target_hw)>0:
			if options.cpe_target_hw.lower() in datas[cpe_offset+9].lower():	store_the_line=True

		if len(options.cpe_other)>0:
			if options.cpe_other.lower() in datas[cpe_offset+10].lower():	store_the_line=True

		if store_the_line:
			print(myline.replace("\r","").replace("\n",""))

		myline = fic_in.readline()

	fic_in.close()    
	print("Done...")
	print("See you soon.")

if __name__ == "__main__":
	main()
	try:
		pass
	except Exception as inst:
		print('='*60)
		print(str(type(inst)))
		print('-'*60)
		print(str(inst))
		print('='*60)