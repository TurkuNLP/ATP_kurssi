import sys
import gzip
import re

def load_data(data,clas):
    target = []
    ref = []
    filename = data
    if filename.endswith("gz"):
        corpus = gzip.open(filename,"rt")
    else:
        corpus = open(filename,"r")
    for line in corpus:
        line=line.strip().lower().split(" ")
        if line[0].startswith(str(clas)):
            target.append(line[1:])
        else:
            ref.append(line)
    return(target,ref)
#print("target corpus document number: ", len(target), "reference corpus document number: ", len(ref))

def load_key_data(data):
    target = []
#    ref = []
    if data.endswith("gz"):
        corpus = gzip.open(data,"rt")
    else:
        corpus = open(data,"r")
    for line in corpus:
        line=line.strip().lower()#.split(" ")
        line=line[2:]
        line = re.sub('[^\w|\s|\'|\-]', '', line)
        line=line.replace("  ", " ")
        line2 = []
        for e in line.split(" "):
            if len(e) >0:
                line2.append(e)
        target.append(line2)
#        if line[0].startswith(str(clas)):
#        target.append(line[1:])
 #       else:
  #          ref.append(line)
    return(target)

def total_wc(data):
    wc = 0
    for line in data:
        for word in line:
            wc +=1
    return wc
    
def text_count(word,data):
#    print("search word", word)
    text_c = 0
#    total_text_c = 0
    for te in data:
 #       print("text")
        myc = None
        for w in te:
 #           print("w", w)
#            print("myc", myc, text_c)
            if w==word.lower():
                myc=True
#        if any(item == word.lower() for item in set(t)):
        if myc==True:
            text_c +=1
#        print("m", myc,text_c)
    return(str(text_c), str(int(text_c)/len(data)))
#    return(str(text_c),  str((int(text_c)/len(data))*100))


def word_count(word,data):
    word_c = 0
    total_wc = 0
    for line in data:
#        line=line.strip().split(" ")
        for w in line:
            w=w.lower()
            total_wc += 1
            if w==word:
                word_c +=1
    return(str(word_c), str((int(word_c)/total_wc)*1000))

#def compar(target,reference):
    
                            

#searchword = sys.argv[2]
#print("text frequency for ", searchword,  "in target: ", " ".join(text_count(searchword,target)), "in reference: ", " ".join(text_count(searchword, ref)))
#print("word frequency for ", searchword,  "in target: ", " ".join(word_count(searchword,target)), "in reference: ", " ".join(word_count(searchword, ref)))
