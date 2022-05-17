#!/usr/bin/env python
#-*- coding: utf-8 -*-

import json
import sys,os
import codecs
import requests
import datetime



def CheckAlive(
        FileIn="Data.json",     # JSON ToCheck
        FileSave="",            # Set a name to save originalfile ()
        CheckDomain=True,
        CheckWget=False):
    
    data = json.load(codecs.open("."+os.sep+FileIn,"r","utf-8"))
    One_session = requests.session()
    #We load Proxy if there is some Proxy.json...
    if os.path.exists('..'+os.sep+'Proxy.json'):
        One_session.proxies=json.load(codecs.open('Proxy.json','r','utf-8'))
        One_session.verify = False

    Sec_num=0
    for oneSection in data.keys():
        Sec_num+=1
        print(str(Sec_num).rjust(3)+" - "+oneSection)

        ref_num=0
        ref_to_delete=[]
        for one_ref in data[oneSection].keys():
            ref_num +=1
            
            for one_url in data[oneSection][one_ref]:
                Is_OK = True
                
                if CheckDomain:
                    if Is_OK:
                        # Retreiving Domain's IP address
                        try:
                            Domain = one_url.split("/")[2]
                            # print(str(Domain)+" > "+socket.gethostbyname(Domain))
                        except Exception as inst:
                            Is_OK = False
                
                if CheckWget:
                    if Is_OK:
                        # try to get URL
                        try:
                            resp = One_session.get(one_url)
                        except Exception as inst:
                            Is_OK = False
                
                if Is_OK :
                    print("\t"+str(ref_num).rjust(2)+" . OK . "+one_ref+" - "+str(one_url))
                else:
                    print("\t"+str(ref_num).rjust(2)+" . HS . "+one_ref+" - "+str(one_url))
                    data[oneSection][one_ref].pop(data[oneSection][one_ref].index(one_url))
            
            if len(data[oneSection][one_ref])<1:
                ref_to_delete.append(one_ref)
        
        for one_ref in ref_to_delete:
            data[oneSection].pop(one_ref)

    json.dump(data, codecs.open("."+os.sep+"Data_temp.json","w","utf-8"),indent=4)

    if len(FileSave)>1:
        FileSave = FileSave.replace("<DATE>",datetime.datetime.now().strftime("%Y-%m-%d"))
        os.rename("."+os.sep+FileIn,"."+os.sep+FileSave)

    try:
        os.remove("."+os.sep+FileIn)
    except Exception as inst:
        pass
    #Finally we our temp file to original file place
    os.rename("."+os.sep+"Data_temp.json","."+os.sep+FileIn)

    return "."+os.sep+FileIn

if __name__ == "__main__":
	newfile = CheckAlive("Data.json","Data_old_<DATE>.json")
	try:
		pass
	except Exception as inst:
		print('='*60)
		print(str(type(inst)))
		print('-'*60)
		print(str(inst))
		print('='*60)