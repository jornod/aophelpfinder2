# -*- coding: utf-8 -*-
# author: Florence Jornod - INSERM 
#contact: florence.jornod@inserm.fr

#------- WHAT IS AOPHELPFINDER? -------------

#AOPhelpfinder 2 is an new version of AOPhelpfinder (Jean-Charles Carvaillo: https://github.com/jecarvaill/aop-helpFinder) based on text mining and parsing process on abstract. It links Key events, Molecular initiating event and adverse outcome and chemical throw abstract from pubmed. 
#AOPhelpfinder 2 was implemented for Human Biomonintoring in Europe (HBM4EU) Work Package 13.1.
#HBM4EU has received funding from the European Union’s H2020 research and innovation programme under grant agreement No 733032.

#------- LICENCE ---------------------------

#all rights reserved
#-------------------------------------------

import datetime
import csv
import tm_module as tm
import pprint as pprint
import random


def create_collection_event(event_filename):
	"""Method to take from a file (event_filename) a list of event from the aopwiki website.
	The file must be a csv with a first col the aopwiki_id, then the type of the event, then the 		name of the event.
	ARGUMENT: event_filename -> the name of the file with the information about the event
    	RETURN: list_events -> a dictionnary with all the events. 
    	"""
	list_events = []
	list_id = []
	with open(event_filename,mode="r") as infile:
		reader = csv.reader(infile)
		for rows in reader:
			dict_event = {}
			dict_event["type"]=[]
			name = rows[2]
			t_event = rows[1]
			id_event = rows[0]

			if id_event not in list_id:
				dict_event["name"] = name
				dict_event["stemname"] = tm.clean_abstract(name, True)
				dict_event["type"].append(t_event)
				dict_event["id"] = id_event
				dict_event["udate"] = datetime.datetime.now()
				dict_event["indi"] = random.randint(1,4)

				list_events.append(dict_event)
			else:
				for event in list_events:
					if event["id"] == id_event:
						event["type"].append(t_event)
						break
			list_id.append(id_event)
	return list_events

