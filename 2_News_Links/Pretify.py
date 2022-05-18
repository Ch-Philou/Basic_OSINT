#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import json
import codecs

Localfile = "."+os.sep+"NewsSource.json"

if os.path.exists(Localfile):
	data =  json.load(codecs.open(Localfile,'r','utf-8'))
	fic = codecs.open(Localfile,"w","utf-8")
	fic.write(json.dumps(data,indent=4))
	fic.close()
else:
	print("Nothing to Prettify")