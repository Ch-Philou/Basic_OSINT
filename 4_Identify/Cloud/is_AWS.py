#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import json
import argparse
import requests
import codecs
import datetime

import ipaddress

AWS_IP_Range ="https://ip-ranges.amazonaws.com/ip-ranges.json"
Proxy_JSON = ".."+os.sep+".."+os.sep+"Proxy.json"


def LoadData(Proxy_file):
	Localfile = "."+os.sep+"AWS_ip-ranges_<DATE>.json".replace("<DATE>",datetime.datetime.now().strftime("%Y-%m-%d"))
	if not os.path.exists(Localfile):
		print("AWS IP Listing retreiving")
		session = requests.Session()
		if os.path.exists(Proxy_file):
			print(" -> Loading proxy setting ("+str(Proxy_file)+")")
			proxies =  json.load(codecs.open(Proxy_file,'r','utf-8'))
			session.proxies=proxies
			session.verify=False
		else:
			print(" -> No proxy setting ("+str(Proxy_file)+")")
		
		req = session.get(AWS_IP_Range,timeout=30)
		print("AWS IP Listing saving")
		fic = codecs.open(Localfile,"w","utf-8")
		fic.write(req.text)
		fic.close()
		del req, session
	
	print("Loading local file " + str(Localfile))
	Data_AWS = json.load(codecs.open(Localfile,'r','utf-8'))

	return Data_AWS

def IsAWS(IP,Data):
	IP_adr = ipaddress.ip_address(IP)
	if IP_adr.version ==4:
		for i in range(len(Data["prefixes"])):
			if IP_adr in ipaddress.ip_network(Data["prefixes"][i]["ip_prefix"]): return True
	elif  IP_adr.version ==6:
		for i in range(len(Data["ipv6_prefixes"])):
			if IP_adr in ipaddress.ip_network(Data["ipv6_prefixes"][i]["ipv6_prefix"]): return True
	return False

def main(argv):
	print("Argument Reading")
	parser = argparse.ArgumentParser(
		# prog='Target_add',
		add_help = True,
		description = "-------------------------",
		epilog='''\
		 blabla\r\n
		 balbla\r\n
		 ''')

	parser.add_argument('-ip',  '--IP',			type=str, action="store", default='', help='an IP v4 ou v6 list')
	parser.add_argument('-f', '--file',			type=str, action="store", default='', help='File to open')
	parser.add_argument('-fc', '--FileCol',		type=int, action="store", default=0, help='column where IP/hostname is')
	options = parser.parse_args()

	data = LoadData(Proxy_JSON)
    
	if len(options.IP)>1: 	print(IsAWS(options.IP,data))
	if len(options.file)>1:
		if not os.path.exists(options.file):
			print("File does not exist")
		else:
			fic_to_read = codecs.open(options.file,"r","utf-8")
			lines= fic_to_read.readlines()
			fic_to_read.close()

			fic_to_save = codecs.open("."+os.sep+"Listing.txt","w","utf-8")
			for one_line in lines:
				IP = one_line.split(",")[options.FileCol]
				if IsAWS(IP,data):
					print("Found One: "+str(IP))
					fic_to_save.write(one_line)
				
			fic_to_save.close()


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