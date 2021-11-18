import sys

cols = ["ID","FORM","LEMMA","UPOS","XPOS","FEAT","HEAD","DEPREL","DEPS","MISC"]

def read_conll(inp,max_sent=0,drop_tokens=True,drop_nulls=True):
    comments=[]
    sent=[]
    yielded=0
    for line in inp:
        line=line.rstrip("\n")
        if line.startswith("#"):
            comments.append(line)
        elif not line:
            if sent:
                yield sent,comments
                yielded+=1
            if max_sent>0 and yielded==max_sent:
                break
            sent,comments=[],[]
        else:
            cols=line.split("\t")
            sent.append(cols)
    else:
        if sent:
            yield sent,comments

for one_sent,comments in read_conll(sys.stdin,5):
    words=(word_line[cols.index("FORM")] for word_line in one_sent)
    col = sys.argv[1]
    lemmas=(word_line[cols.index(col)] for word_line in one_sent)
    print(" ".join(words))
    print(" ".join(lemmas))
    print()

