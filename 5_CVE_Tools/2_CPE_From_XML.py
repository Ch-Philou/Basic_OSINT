#!/usr/bin/env python
#-*- coding: utf-8 -*-

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

	parser.add_argument('-xi',  '--xml_in',		type=str, action="store", default='.'+os.sep+"official-cpe-dictionary_v2.3.xml",help='File to open')
	parser.add_argument('-fo',  '--file_out',	type=str, action="store", default="."+os.sep+"CPE_List.csv",   help='File to save data to')
	parser.add_argument('-s',   '--separator',	type=str, action="store", default=',',							help='Separator in CSV')
	parser.add_argument('-lf',							  action="store_true",						 		help='Use LF instead of CRLF for new line')
	options = parser.parse_args()
	
	if len(options.xml_in)<2:
		print("Well... we need at least a xml from NIST")
		print("You can get one fresh like this:")
		
		from platform import system
		if system() == 'Windows':
			print("Powershell:")
			print("> Invoke-WebRequest https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip -OutFile official-cpe-dictionary_v2.3.xml.zip")
			print("> Expand-Archive .\official-cpe-dictionary_v2.3.xml.zip -DestinationPath .")
			
		elif system() in ['Linux', 'Darwin'] :
			print("Bash:")
			print("# wget https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip -OutFile official-cpe-dictionary_v2.3.xml.zip")
			print("# unzip .\official-cpe-dictionary_v2.3.xml.zip -d .")
		
		sys.exit(1)
	
	XML_File = options.xml_in
	CSV_Out = options.file_out

	if not os.path.exists(XML_File):
		print("File does not exist "+str(XML_File))
		sys.exit(1)
	
	print("-"*40)
	print(" Reading CPE file")
	print("-"*40)
	print("XML file (input)  is "+str(XML_File))
	print("CSV file (output) is "+str(CSV_Out))
	print("-"*40)
	print("Go")


	fic_in = codecs.open(XML_File,"r",encoding="UTF-8")
	fic_out= codecs.open(CSV_Out,"w",encoding="UTF-8")
	#Headings
	fic_out.write("Full CPE"+options.separator)
	fic_out.write("CPE Version"+options.separator)
	fic_out.write("Part"+options.separator)
	fic_out.write("Vendor"+options.separator)
	fic_out.write("Product"+options.separator)
	fic_out.write("Version"+options.separator)
	fic_out.write("Update"+options.separator)
	fic_out.write("Edition"+options.separator)
	fic_out.write("Language"+options.separator)
	fic_out.write("SW_Edition"+options.separator)
	fic_out.write("Target_SW"+options.separator)
	fic_out.write("Target_HW"+options.separator)
	fic_out.write("Other"+options.separator)

	if options.lf:
		fic_out.write("\n")
	else:
		fic_out.write("\r\n")

	myline = fic_in.readline()
	while myline:
		if "<cpe-23:cpe23-item name=" in myline:
			OneCPE = myline[myline.find('"')+1:-4]
			print("\r"+OneCPE+" "*(170-len(OneCPE)),end="")
			fic_out.write(OneCPE+options.separator+OneCPE.replace(":",options.separator)[4:])
			if options.lf:
				fic_out.write("\n")
			else:
				fic_out.write("\r\n")
		myline = fic_in.readline()
	fic_in.close()  
	fic_out.close()  
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