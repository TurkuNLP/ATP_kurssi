import sys
import re
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


###C: NEWDOC
###C: 0
###C:TIME 2020-03-30 23:59:55
###C:TEXT


def argparser():
    ap = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    ap.add_argument('--time')
    ap.add_argument('--text')
    return ap

def read_text(inp):
    feats = []
    id = None
    time=None
    text = None
    for line in inp:
#        print(line)
        line=line.strip()
        if line.startswith("###C: NEWDOC"):
            if time != None:
                yield(id, time,text, feats) # tässä tiedot mitä halutaan kerätä
                feats = []
                id = None
                time=None
                text = None
            else:
                continue
        else:
            if line.startswith("#"): #kerättävät metatiedot
                if line.startswith("###C:TIME"):
                    time = line
                elif line.startswith("###C:TEXT"):
                    text = line
                else:
                    continue
            else:
                if line:
                    line=line.split("\t")
                    feats.append(line) #nyt tämä kerää pelkät sanat, mutta esim. 2lla saa lemmat (kolmas sarake)
                else:
                    feats.append("\n")
    yield(id, time,text, feats)

    
def print_all(time,text,feats):
    print(time)
    print(text)
    for f in feats:
        print("\t".join(f))
    

    
options = argparser().parse_args(sys.argv[1:])


for id, time,text, feats in read_text(sys.stdin):
    if options.text is not None:
        if options.text in text:
            if options.time is not None:
                if options.time in time:
                    print_all(time,text,feats)
                else:
                    continue
            else:
                print_all(time,text,feats)

    else:
        if options.time is not None:
            if options.time in time:
                print_all(time,text,feats)
