#!/usr/bin/env python
#-*- coding: utf-8 -*-



import json
import sys,os
import codecs
import requests,socket
import argparse
import datetime


ProxyFile = '..'+os.sep+'Proxy.json'

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

	parser.add_argument('-fi', '--file_in',			type=str, action="store", default="."+os.sep+"List.csv", help='File to open')
	parser.add_argument('-fo', '--file_out',		type=str, action="store", default="."+os.sep+"List_up.json", help='File to save')
	parser.add_argument('-sep', '--separator',		type=str, action="store", default=",", help='Separator')
	parser.add_argument('-uc',  '--urlcol',			type=int, action="store", default=-1, help='Column number for url')
	parser.add_argument('-to',  '--timeout',		type=int, action="store", default=20, help='session timeout')
	parser.add_argument('-ms',  '--minsize',		type=int, action="store", default=500, help='session timeout')
	parser.add_argument('-ncd', '--NoCheckDomain',	action="store_true", default='', help='Do not check domain resolution')
	options = parser.parse_args()
	
	
	One_session = requests.session()
	#We load Proxy if there is some Proxy.json...
	if os.path.exists(ProxyFile):
		One_session.proxies=json.load(codecs.open(ProxyFile,'r','utf-8'))
		One_session.verify = False

	print("Loading: "+str(options.file_in))
	fic_in = codecs.open(options.file_in,"r","utf-8")
	urls = fic_in.readlines()
	
	if len(urls)<1:
		print("Nothing to do, Strange")
		sys.exit(1)
	print("We get "+str(len(urls))+" urls to test.")

	Responding_urls=[]

	for one_url in urls:
		one_url = one_url.replace("\r","").replace("\n","").replace("\t","")
		
		if options.urlcol >-1 and options.separator in one_url:
			one_url = one_url.split(options.separator)[options.urlcol]
		
		if len(one_url)<5: continue
		print("\t Testing: "+str(one_url))
		Is_OK = True

		if options.NoCheckDomain:
			try:
				Domain = one_url.split("/")[2]
				socket.settimeout(options.timeout)
				print(str(Domain)+" > "+socket.gethostbyname(Domain))
			except Exception as inst:
				Is_OK = False
				print("\t\t [-] DNS Dead")

		if Is_OK:
			# try to get URL
			try:
				resp = One_session.get(one_url, timeout=options.timeout)
			except Exception as inst:
				Is_OK = False
				print("\t\t [-] URL Dead")

		if resp.status_code in [200,201]:
			pass
		else:
			Is_OK = False
			print("\t\t [-] HTTP_Code = "+str(resp.status_code))

		if len(resp.text)<options.minsize:
			Is_OK = False
			print("\t\t [-] TooShort = "+str(len(resp.text))+" < Minsize("+str(options.minsize)+")")

		if not Is_OK: continue

		print("\t\t [+] HTTP_Code = "+str(resp.status_code))

		URL={}
		URL["link"]=one_url
		URL["Valid"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		URL["HTTP_Code"]=resp.status_code
		URL["Length"]=len(resp.text)

		Responding_urls.append(URL)

	#Our loop is Over, Let's save them to JSON
	print("Saving JSON: "+str(options.file_out))
	fic = codecs.open(options.file_out,"w","utf-8")
	fic.write(json.dumps(Responding_urls,indent=4))
	fic.close()

	
	print("Saving CSV: "+str(options.file_out))
	fic = codecs.open(options.file_out.replace(".json",".csv"),"w","utf-8")
	fic.write("link"+options.separator+"Valid"+options.separator+"HTTP_Code"+options.separator+"Length"+options.separator+"\r\n")
	for one in Responding_urls:
		fic.write(str(one["link"])+options.separator)
		fic.write(str(one["Valid"])+options.separator)
		fic.write(str(one["HTTP_Code"])+options.separator)
		fic.write(str(one["Length"])+options.separator+"\r\n")
	fic.close()



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