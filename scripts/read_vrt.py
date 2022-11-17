import sys
import re
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter


def argparser():
    ap = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    ap.add_argument('--time')
    ap.add_argument('--text')
    ap.add_argument('--party')
    ap.add_argument('--speaker')
    return ap

def read_text(inp):
    feats = []
    speaker = None
    time=None
    text = None
    party = None
    for line in inp:
        line=line.strip()
        if line.startswith("<paragraph id"):
#            print("L", line)
            if feats != []:
                yield(speaker, time,party,feats) # tässä tiedot mitä halutaan kerätä
                feats = []
                speaker = None
#                time=None
                party = None
            line=line.strip().split("=")
#            print()
            for item in line:
                    if "tierid" in item:
                        speaker=item.replace("tierid", "")
                    elif "speech_type" in item:
                        party=item.replace("speech_type", "")
                    else:
                        continue                                
        else:
            if line.startswith("<"): #kerättävät metatiedot
                if line.startswith("<text"):
                    line=line.strip().split(" ")
                    for item in line:
                        if item.startswith("date="):
                            time=item.replace("date=","")
                            time=time.replace("\"", "")
                            time=time.split("-")[0]
                        else:
                            continue
                else:
                    continue
            else:
                if line:
                    line=line.split("\t")
                    feats.append(line) 
                else:
                    feats.append("\n")
    yield(speaker,time,party, feats)

    
def print_all(speaker,time,party,feats):
    print("###C: NEWDOC")
    print("###C: SPEAKER", speaker)
    print("###C: TIME", time)
    print("###C: PARTY", party)
    print()
    for f in feats:
        print("\t".join(f))
    
    
options = argparser().parse_args(sys.argv[1:])


for speaker,time,party, feats in read_text(sys.stdin):
    printMe=None
    if options.speaker is not None:
        if options.speaker in speaker:
            printMe = True#_all(speaker,time,party,feats)
        else:
            continue
    elif options.party is not None:
        party=party.replace("\"", "")
        party=party.replace(" ", "")
        options.party=options.party.replace(" ", "")
        if party == options.party:
        
            printMe=True #print_all(speaker,time,party,feats)
    elif options.time is not None:
        if str(time) in str(options.time):
#            print("time match")
            printMe=True
    if printMe==True:
        print_all(speaker,time,party,feats)
        
