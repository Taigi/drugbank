

# -*- coding: utf8 -*-
#!/pkg/ldc/bin/python2.5
#-----------------------------------------------------------------------------
# Name:        drugbankCorpusAccessor.py
#
# Author:      Horacio
#
# Created:     2015/10/28
# accessor to drugbank corpus
# 
#-----------------------------------------------------------------------------

import sys


##user='horacioCluster'
user='horacioLocal'
if user == 'horacioCluster':
    dirDRUGBANK = '/home/usuaris/horacio/corpora/drugbank/'
elif user == 'horacioLocal':
    dirDRUGBANK = 'C:/Users/horacio/Desktop/docencia/dmkm/data/'
else:
    print 'unknown user'

  
lang='en'

##most of these modules are in fact not needed, there are here because copy & paste

import re
from string import *
from os import listdir,path
from os import fsync
from os.path import split, splitext, abspath
from sgmllib import *
import pickle
from copy import deepcopy
import locale
from types import StringType
import nltk
import tokenize
try:
    import punkt
except:
    pass
from nltk import stem

locale.setlocale(locale.LC_ALL, '')

##global


##classes


class MySGMLParser (SGMLParser):
##a refinement of the class SGMLParser

    def unknown_starttag(self, tag, attrs):
        global drugbankData, drugbankEntity
        drugbankData._stack_of_tags.push(tag)
        drugbankData._current_text=""

    def unknown_endtag(self, tag):
        global drugbankData, drugbankEntity
        drugbankData._stack_of_tags.pop_until(tag)

    def handle_data(self,data):
        global drugbankData, drugbankEntity
        try:
            drugbankData._current_text += data
        except UnicodeDecodeError:
            drugbankData._current_text = ''

    def handle_charref(self, ref):
        global drugbankData, drugbankEntity
        self.handle_data (unichr(int(ref)))


    def start_drugbankid(self, attributes):
##
##        examples
##  <drugbank-id primary="true">DB00001</drugbank-id>
##  <drugbank-id>BIOD00024</drugbank-id>
##        
        global drugbankData, drugbankEntity
        d=dict(attributes)
##        print 'start_drugbankid', d
        drugbankData._stack_of_tags.push('drugbankid')
        if not drugbankData._in_pathways and not drugbankData._in_targets:
            if 'primary' in d and d['primary']=='true':
                drugbankData._is_primary = True
            else:
                drugbankData._is_primary = False
            
    def end_drugbankid(self):
        global drugbankData, drugbankEntity
##        print 'end_drugbankid'
        drugbankData._stack_of_tags.pop_until('drugbankid')
        drugbankData._current_text = drugbankData._current_text.replace('\n','').strip()
        if not drugbankData._in_pathways and not drugbankData._in_targets:
            if drugbankData._is_primary:
                drugbankData.addEntity(drugbankData._current_text)
            else:
                drugbankEntity.idS.add(drugbankData._current_text)
        drugbankData._current_text = ''

    def start_drug(self, attributes):
##        
##        examples
##  <drug type="biotech" created="2005-06-13" updated="2015-02-23">
##        
        global drugbankData, drugbankEntity
        d=dict(attributes)
##        print 'start_drug', d
        drugbankData._stack_of_tags.push('drug')
        if not drugbankData._in_pathways and not drugbankData._in_targets:
            drugbankData._current_text = ''
            
    def end_drug(self):
        global drugbankData, drugbankEntity
##        print 'end_drug'
        drugbankData._stack_of_tags.pop_until('drug')
        drugbankData._current_text = drugbankData._current_text.replace('\n','').strip()
        if not drugbankData._in_pathways and not drugbankData._in_targets:
            drugbankEntity.name = drugbankData._current_text
            drugbankData._current_text = ''                

    def start_name(self, attributes):
##        
##        examples
##    <name>Lepirudin</name>
##    valid_name()checks whether the context of the name is valid (corresponds to the main name)
##        
        global drugbankData, drugbankEntity
        d=dict(attributes)
##        print 'start_name', d, valid_name()
        if valid_name():
            drugbankData._stack_of_tags.push('name')
            drugbankData._current_text = ''                
            
    def end_name(self):
        global drugbankData, drugbankEntity
##        print 'end_name', valid_name()
        if valid_name():
            drugbankData._stack_of_tags.pop_until('name')
            drugbankData._current_text = drugbankData._current_text.replace('\n','').strip()
            if drugbankEntity.name == '':
                drugbankEntity.name = drugbankData._current_text
##            print '***', drugbankEntity.name
            drugbankData._current_text = ''                

    def start_pathways(self, attributes):
        global drugbankData, drugbankEntity
##        print 'start pathways'
        drugbankData._stack_of_tags.push('pathways')
        drugbankData._current_text = ''                
        drugbankData._in_pathways = True                
            
    def end_pathways(self):
        global drugbankData, drugbankEntity
##        print 'end pathways'
        drugbankData._stack_of_tags.pop_until('pathways')
        drugbankData._current_text = ''                
        drugbankData._in_pathways = False                

    def start_targets(self, attributes):
        global drugbankData, drugbankEntity
##        print 'start targets'
        drugbankData._stack_of_tags.push('targets')
        drugbankData._current_text = ''                
        drugbankData._in_targets = True                

    def end_targets(self):
        global drugbankData, drugbankEntity
##        print 'end targets'
        drugbankData._stack_of_tags.pop_until('targets')
        drugbankData._current_text = ''                
        drugbankData._in_targets = False                
        
    def start_pfams(self, attributes):
        global drugbankData, drugbankEntity
##        print 'start pfams'
        drugbankData._stack_of_tags.push('pfams')
        drugbankData._current_text = ''                
        drugbankData._in_pfams = True                

    def end_pfams(self):
        global drugbankData, drugbankEntity
##        print 'end pfams'
        drugbankData._stack_of_tags.pop_until('pfams')
        drugbankData._current_text = ''                
        drugbankData._in_pfams = False                
        
            

class STACK:
##a simple implementation of the class STACK
    
    def __init__(self):
        self.content=[]
        self.size=-1
    def is_empty(self):
        return self.size==-1
    def push(self,x):
        self.size+=1
        self.content.append(x)
    def pop(self):
        if self.size >= 0:
            self.content.pop()
            self.size-=1
    def top(self):
        return self.content[self.size]
    def pop_until(self,x):
        while (not(self.is_empty()) and (self.top() != x)):
            self.pop()
        if not(self.is_empty()):
            self.pop()

class DRUGBANK:
##the class describing the corpus

    def __init__(self):
        self._init_vars()
    
    def _init_vars(self):
        self.entities={}
        self._current_text=''
        self._current_entity=''
        self._stack_of_tags=STACK()
        self._is_primary=False
        self._in_pathways=False
        self._in_targets=False
        self._in_pfams=False
        
    def addEntity(self,e):
        global drugbankData, drugbankEntity
        self.entities[e]=DRUGBANKENTITY(e)
        drugbankEntity = self.entities[e]

    def getEntity(self,e):
        if e not in self.entities:
            return None
        return self.entities[e]

    def _describe(self, verbose=False):
        print 'entities', len(self.entities)
        if verbose:
            for i in self.entities:
                print '\t',i


class DRUGBANKENTITY:
##the class describing an entry of the corpus

    def __init__(self,id):
        self._init_vars(id)
        
    def _init_vars(self,id):
        self.id=id
        self.idS = set([])
        self.name=''

    def _describe(self,verbose=False):
        print 'DRUGBANKENTITY primary id', self.id
        print 'not primary idS', self.idS
        print 'name', self.name



##auxiliar functions

##########################################################################
# Guess Character Encoding
##########################################################################

# adapted from io.py in the docutils extension module (http://docutils.sourceforge.net)
# http://www.pyzine.com/Issue008/Section_Articles/article_Encodings.html

def guess_encoding(data):
    """
    Given a byte string, attempt to decode it.
    Tries the standard 'UTF8' and 'latin-1' encodings,
    Plus several gathered from locale information.

    The calling program *must* first call::

        locale.setlocale(locale.LC_ALL, '')

    If successful it returns C{(decoded_unicode, successful_encoding)}.
    If unsuccessful it raises a C{UnicodeError}.
    """
    successful_encoding = None
    # we make 'utf-8' the first encoding
    encodings = ['utf-8']
    #
    # next we add anything we can learn from the locale
    try:
        encodings.append(locale.nl_langinfo(locale.CODESET))
    except AttributeError:
        pass
    try:
        encodings.append(locale.getlocale()[1])
    except (AttributeError, IndexError):
        pass
    try: 
        encodings.append(locale.getdefaultlocale()[1])
    except (AttributeError, IndexError):
        pass
    #
    # we try 'latin-1' last
    encodings.append('latin-1')
    for enc in encodings:
        # some of the locale calls 
        # may have returned None
        if not enc:
            continue
        try:
            decoded = unicode(data, enc)
            successful_encoding = enc

        except (UnicodeError, LookupError):
            pass
        else:
            break
    if not successful_encoding:
         raise UnicodeError(
        'Unable to decode input data.  Tried the following encodings: %s.'
        % ', '.join([repr(enc) for enc in encodings if enc]))
    else:
         return (decoded, successful_encoding)            

def _encode(data):
	return data.encode('utf8')

def _decode(data):
	return data.decode('utf8')

def multiple_replace(dict, text): 

  """ Replace in 'text' all occurences of any key in the given
  dictionary by its corresponding value.  Returns the new tring.""" 

  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

##functions

def valid_name():
    global drugbankData, drugbankEntity
    return not drugbankData._in_pathways and not drugbankData._in_targets and not drugbankData._in_pfams
    
def listIntersection(l1,l2):
    "intersection of two lists"
    return list(set(l1).intersection(set(l2)))

def listUnion(l1,l2):
    "Union of two lists"
    return list(set(l1).union(set(l2)))

def listRemoveDuplicates(l):
    "returns the list without duplicates without changing the order"
    rta = []
    for i in l:
        if i in rta:
            continue
        rta.append(i)
    return rta

def listDifference(l1,l2):
    "l1 - l2"
    return list(set(l1).difference(set(l2)))

def load_pickle_drugbank(ent):
    global drugbankData
    ent=open(ent,'rb')
    drugbankData=pickle.load(ent)
    ent.close()
    drugbankData._describe()

def save_pickle_drugbank(sal):
    global drugbankData
    sal=open(sal,'wb')
    pickle.dump(drugbank,sal)
    sal.close()
    print 'drugbank saved', len(drugbank)

def getDRUGBANKcorpusFromFile(inF):
    global p, drugbankData
    print 'loading drugbank corpus from file',inF
    drugbankData=DRUGBANK()
    p = MySGMLParser()
    drugbankData._current_file = inF
    entrada=open(inF).read()
    entrada = multiple_replace({
        'drugbank-id':'drugbankid',
        'international-brand':'internationalbrand'
        }, entrada)
    p.feed(entrada)
    p.close()


        
# main

getDRUGBANKcorpusFromFile(dirDRUGBANK+'aaa.txt')
for i in drugbankData.entities:
    print i
    drugbankData.entities[i]._describe()


