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
import networkx as nx
import tm_module as tm

def compute_scores(abstract, events):
    ''' METHOD: compute the score of presence of the event in the abstract, return also the different position in the abstract.
	ARGUMENTS: abstract -> a string with the abstract 
		   events -> the list of the events
	RETURN: dico -> a dictionnary with the name if the event as key and the 2 scores
    '''
    len_abstract = len(abstract)
    sentences = abstract
    dico={}

    for event in events:
        score = 0
        if event["stemname"]!='':
            score, localisation = find_event(sentences,event["stemname"])
        if(score!=0):
             dico[str(event["name"])]={}
             dico[str(event["name"])]["multiscore"]=score
             dico[str(event["name"])]["localisation"]=localisation
    return(dico)

def find_event(sentences, event):
	''' METHOD: find a event in a list of sentences and compute the score
	    ARGUMENTS: sentences -> a string with the sentences (for example an abstract) 
		   event -> a string with one event
	    RETURN: score, localisation -> the score associated to the event and the abstract, and the localisation of the event (index of the list of sentences)
    '''
	event_split = list(set(event.split()))
	if not event_split:
		return
	score = 0
	localisation = 0
	for i in range(len(sentences)):
		best = presence_score(sentences,event_split,i)
		if (abs(1-best/len(event_split)) < abs(1-score)):
			score = best/len(event_split)
			localisation = i
	return score, localisation



def presence_score(sentence, event,i):
	''' METHOD: check if a event is in a sentence in a text (sentences)
	    ARGUMENTS: sentences -> a string with the sentences (for example an abstract) 
		       event -> a list of the words from one event
		       i -> the index of the sentence
	    RETURN: best -> the best score found
    '''
	best = 0
	cpt = 0
	index = {}
	words = sentence[i].split()
	for e in event:
		if e in words:
			cpt += 1
			index[e] = [pos+1 for pos, value in enumerate(words) if value == e]
	proportion = cpt/len(event)
	if 0.75 <= proportion and len(event) != 1:
		values = index.values()
		values = [sorted(value) for value in values]
		values = sorted(values, key = lambda k: k[-1])
		G = nx.Graph()
		for i in range(len(values) -1):
			for j in range(len(values[i])):
				for l in range(len(values[i + 1])):
					G.add_edge(values[i][j], values[i+1][l], weight = abs(values[i+1][l]-values[i][j]))
		shortest_paths = {}
		for start in values[0]:
			for end in values[-1]:
				shortest_path = nx.dijkstra_path(G, start, end)
				tot_weight = nx.dijkstra_path_length(G, start, end)
				shortest_paths[tot_weight +1] = shortest_path
		best = min(shortest_paths, key = shortest_paths.get)
	elif proportion == 1.0 and len(event) ==1 :
		best = 1.0
	return best


def update_score_in_db(abstracts_db, abstract_id, scores):
    abstracts_db.update({"_id":abstract_id},{"$set": {"scores":scores}})
    return



