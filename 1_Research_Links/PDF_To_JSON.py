#!/usr/bin/env python
#-*- coding: utf-8 -*-



import fitz 
import json
import sys,os
import codecs


FileToParse = "."+os.sep+"OSINT_Handbook_2020.pdf"

def trim(text):
    if len(text)<3: return ""
    if len(text.replace(" ",""))<1: return ""
    try:
        while text[0]==" ":
            text = text[1:]
        while text[-1] == " ":
            text = text[:-1]
    except Exception as inst:
        print("++ "+str(text)+" ++")
        print("++ "+str(len(text))+" ++")
        raise inst
    return text

def IsNum(text):
    try:
        if int(text): pass
        return True
    except:
        return False



def GetNewSection():
    Section={}
    Section["Title"]=""
    Section["Elements"]={}
    return Section

def main():
    page_num = 1
    with fitz.open(FileToParse) as doc:
        text = []
        for page in doc:
            print("Page: "+str(page_num))
            if 17<page_num and page_num<510:
                text.extend(page.get_text_blocks())
            page_num+=1

    All_Section={}

    ActualSection=""
    ActualName=""
    ActualURL=""
    LastSection=""

    for oneblock in text:
        one_text = trim(str(oneblock[4].replace("\n","").replace("\r","")))
        

        
        if len(one_text)<4: # Must be a page num or empty block
            print("\t >> Junk")
            continue

        if one_text == "Tool  Link":
            print("\t >> Junk (elem start)")
            InElement = True
            continue
        
        if "Tool  Link" in one_text:
            one_text = trim(one_text.replace("Tool  Link",""))

        if "http" in one_text:
            ActualName = trim(one_text.split("http")[0])
            if one_text.count("http")==1:
                ActualURL  = ["http"+one_text.split("http")[1]]
            else:
                ActualURL=[]
                for num in range(1,one_text.count("http")):
                    ActualURL.append("http"+one_text.split("http")[num])
            
            if len(ActualName)<4:
                print("\t\t\tOups")
                ActualName = ActualSection
                ActualSection = LastSection
            if not ActualSection in All_Section.keys(): All_Section[ActualSection]={}

            print(" > "+ActualSection+" > "+ActualName+" > "+str(ActualURL))

            All_Section[ActualSection][ActualName]=ActualURL
        else:
            print ("-"+str(one_text)+"-")
            LastSection = ActualSection
            ActualSection = trim(one_text)

    # print(json.dumps(All_Section,indent=4))        
    json.dump(All_Section, codecs.open("."+os.sep+"Data.json","w","utf-8"),indent=4)


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