#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import codecs
import winshell
import json



BaseFolder=os.environ['userprofile']+r"\Favorites\Cyber\OSINT\_All"

def EscapeBizare(Text):
    Text = str(Text)
    Text = Text.replace("/","-")
    Text = Text.replace(":","-")
    Text = Text.replace("?","")
    Text = Text.replace("|","-")
    Text = Text.replace("*","")
    Text = Text.replace("<","")
    Text = Text.replace(">","")

    return Text

def Generate_Path(oneSection,one_ref,ref_num,url_num=""):
    GenericFolder=""

    if oneSection.startswith("Working with "):                              GenericFolder="Working with"
    elif oneSection.startswith("Downloading Videos from "):                 GenericFolder="Downloading Videos from"
    elif oneSection.endswith(" Research"):                                  GenericFolder="Research"
    elif oneSection.endswith(" Search"):                                    GenericFolder="Search"
    elif "Social Media" in oneSection:                                      GenericFolder="Social Media"
    elif any (s in oneSection for s in ["Feed","RSS","News"]):              GenericFolder="RSS_Feed_News"
    elif any (s in oneSection for s in ["Analysing","Analysis"]):           GenericFolder="Analysis"
    elif "Search Engines" in oneSection:                                    GenericFolder="Search Engines"
    elif "Tools" in oneSection:                                             GenericFolder="Tools"
    elif "E-mail" in oneSection:                                            GenericFolder="E-mail"

    if len(GenericFolder)>1:
        if GenericFolder in oneSection: oneSection.replace(GenericFolder,"")
        GenericFolder = GenericFolder+os.sep
    if len(url_num)>0:
        path=BaseFolder+os.sep+GenericFolder+oneSection+os.sep+str(ref_num)+" "+one_ref+" n"+str(url_num)+".url"
    else:
        path=BaseFolder+os.sep+GenericFolder+oneSection+os.sep+str(ref_num)+" "+one_ref+".url"
    return path

def CreateShorcut(Filename,target):
    # Creating flders, if they does exist
    os.makedirs(os.path.dirname(Filename), exist_ok=True)
    #Creating Shortcut
    desktop = winshell.desktop()
    shortcut = codecs.open(Filename, 'w')
    shortcut.write('[InternetShortcut]\n')
    shortcut.write('URL=%s' % target)
    shortcut.close()

def main():
    data = json.load(codecs.open("."+os.sep+"Data_Cleaned.json","r","utf-8"))
    Sec_num=0
    for oneSection in data.keys():
        Sec_num+=1
        print(str(Sec_num).rjust(3)+" - "+oneSection)

        ref_num=0
        ref_to_delete=[]
        for one_ref in data[oneSection].keys():
            ref_num +=1
            if len(data[oneSection][one_ref])==0:
                pass
            elif len(data[oneSection][one_ref])==1:
                path = Generate_Path(EscapeBizare(oneSection),EscapeBizare(one_ref),str(ref_num))
                print(path)
                CreateShorcut(path,str(data[oneSection][one_ref][0]))
            else:
                url_num=0
                for one_url in data[oneSection][one_ref]:
                    url_num+=1
                    path = Generate_Path(EscapeBizare(oneSection),EscapeBizare(one_ref),str(ref_num),str(url_num))
                    print(path)
                    CreateShorcut(path,str(one_url))

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