#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import datetime

Dict_URL ="https://nvd.nist.gov/feeds/xml/cpe/dictionary/official-cpe-dictionary_v2.3.xml.zip"
Proxy_JSON = ".."+os.sep+"Proxy.json"


def LoadData(Proxy_file):
	Localfile = "."+os.sep+"Oofficial-cpe-dictionary_v2.3_<DATE>.xml.zip".replace("<DATE>",datetime.datetime.now().strftime("%Y-%m-%d"))
	if not os.path.exists(Localfile):
		print("NIST CPE dict retreiving")
		
		from platform import system
		if system() == 'Windows':
			print("Powershell:")
			print("> Invoke-WebRequest "+Dict_URL+" -OutFile "+Localfile)
			print("> Expand-Archive "+Localfile+" -DestinationPath .")
			
		elif system() in ['Linux', 'Darwin'] :
			print("Bash:")
			print("# wget "+Dict_URL+" -OutFile "+Localfile)
			print("# unzip "+Localfile+" -d .")
		
	
	print("Local file " + str(Localfile))

	return Localfile

def main(argv):
	
	data = LoadData(Proxy_JSON)


if __name__ == "__main__":
	main(sys.argv)
	try:
		pass
	except KeyboardInterrupt:
		sys.stdout.write('\nQuit by keyboard interrupt sequence !')
	except Exception as inst:
		sys.stdout.write('\n What did you do? ')
		sys.stdout.write('\n'+str(type(inst)))
		sys.stdout.write('\n'+str(inst))