author: Florence Jornod - INSERM 
contact: florence.jornod@inserm.fr

------- WHAT IS AOPHELPFINDER? -------------

AOPhelpfinder 2 is an new version of AOPhelpfinder (Jean-Charles Carvaillo: https://github.com/jecarvaill/aop-helpFinder) based on text mining and parsing process on abstract. It links Key events, Molecular initiating event and adverse outcome and chemical throw abstract from pubmed. 
AOPhelpfinder 2 was implemented for Human Biomonintoring in Europe (HBM4EU) Work Package 13.1.
HBM4EU has received funding from the European Union’s H2020 research and innovation programme under grant agreement No 733032.

------- LICENCE ---------------------------

all rights reserved

------- STRUCTURE OF THE FOLDER------------

aophelpfinder/ 
		-> script/ 
			-> aophelpfinder.py (the main program to use aophelpfinder)
			-> compute_output.py (the script we use to create a tsv from the results from aophelpfinder)
			-> compute_scores.py (to compute the different scores we use to determined if an event is in an abstract)
			-> create_collection_event.py (to create a list of the events we test)
			-> extract_xml.py (to extract the abstracts we analyse. This file is an adapted version of Titipat Achakulvisut, Daniel E. Acuna (2015) "Pubmed Parser" http://github.com/titipata/pubmed_parser.  http://doi.org/10.5281/zenodo.159504)
			-> tm_module.py (the text Mining module developped by Jean-Charles Carvaillo)

		-> data/ 
			-> cyphenothrin.xml (an example of xml we use)
			-> aop_ke_mie_ao.tsv (an example of events file, you must have the same structure of file)
		-> readme.txt (this present file)

------- INSTALL ---------------------------


you need to install :
- python > 3.5
- lxml (we use 4.3.0)
- nltk
- nltk.tokenize
- nltk.data
- csv


------- HOW TO USE ------------------------

$ python3 aophelpfinder.py abstracts_file events_file

-> abstracts_file is a xml from pubmed with the abstracts you want to check (you will find an exemple, in data/)
-> events_file must be a csv with a first col the aopwiki_id, then the type of the event, then the 		name of the event. (you will find an exemple, in data/)

example
 :
florence:~/Documents/aophelpfinder/script$ python3 aophelpfinder.py ../data/cyphenothrin.xml ../data/aop_ke_mie_ao.tsv 

/!\ warning, the output erase the previous.

------- HOW TO CITE -----------------------

If you use our work, please cite : XXX




 






	



	
