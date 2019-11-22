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

def results_to_tsv(dict_abstracts, output_file, list_events):
	""" write the result into a tsv (tab-separated values) 
	    ARGUMENTS : dict_abstracts -> the dictonnary with our results
			output_file -> the file used to store the results
			list_events -> the events used
	"""
	output_file.write("title \t doi \t event \t aopwikiID \t type \t localisation \t presence score \n")
	for abstract in dict_abstracts:
		if 'score' in abstract:
			abst_title = abstract['title']
			abst_doi = abstract['doi']
			for event in abstract['score'].keys():
				for ev in list_events:
					if ev['name']==event:
						info_abst = abst_title +'\t' + abst_doi + '\t' + event + '\t' + str(ev['type']) + "\t" + str(ev['id']) + "\t"
				info_abst = info_abst + str(abstract['score'][event]['localisation']) +"\t" + str(abstract['score'][event]['multiscore']) + "\n"
				output_file.write(info_abst)
	return


