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
import sys
import re
import time
import os
import lxml
import extract_xml as exxml
import compute_scores as cscores
import compute_output as cout
import create_collection_event as ev

arg = sys.argv
abstracts_file = arg[1]
events_file = arg[2]
print(abstracts_file)
print(events_file)


dict_abstracts = exxml.get_abstracts_from_pubmedfile(abstracts_file)
list_events = ev.create_collection_event(events_file)


for abstract in dict_abstracts:
	score = cscores.compute_scores(abstract["abstract"],list_events)
	if score:
		abstract['score']=score

filename= os.path.splitext(abstracts_file)[0] + '-output.tsv'
print("DONE")

output_file = open(filename,"w")

cout.results_to_tsv(dict_abstracts, output_file, list_events)
