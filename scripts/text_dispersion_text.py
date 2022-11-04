import glob
import re
import math
import sys
import gzip
from collections import Counter
from common import load_key_data,text_count,word_count,total_wc
import statistics
from statistics import mean
from analyze import print_text, print_text_text

target_reg = sys.argv[1] # give target register as an argument (e.g. NA or NA_ne)
ref_reg = sys.argv[2]

#Declare and initialize dictionaries
counts_T = {}
counts_R = {}
keyness = {}
text_count_T = {} # dictionaries for text dispersion count (no of texts a word appears in)
text_count_R = {}
word_count_T = {} # dictionaries for word frequency count (no of times a word appears in a corpus)
word_count_R = {}

total_T = 0 # number of texts in a corpus
total_R = 0
words_total_T = 0 # number of words in a corpus
words_total_R = 0

#print(sys.argv[1:])
for file in sys.argv[1:]: # read all files from path -> run from corpus directory
    word_list_T = []
    word_list_R = []
 #   if file in sys.argv[1:]:
    print("Reading a file named", file, flush=True)
    f = print_text_text(file)
    f=f.split("\n")
#    print("LEN", len(f))
 #   print("f0", f[0])


#Count the texts in the target and reference corpora
    for line in f:
        line=line.strip()
        if sys.argv[1]  == file:
            total_T += 1
        else:
            total_R += 1
        line = line.lower()
        line = re.sub('[^\w|\s|\'|\-]', '', line)
        words=line.split( )
#If the file comes from the target register(s) then add to target word count, add all words to file word list. If the file comes from any other register, add to reference corpus dictionary
        if re.match(sys.argv[1], file):
            word_list_T.extend(words)
#            print("word_list", word_list_T)
            words_total_T += len(words)
 #           print("LEN", words_total_T)
        else:
            word_list_R.extend(words)
            words_total_R += len(words)
 
#Create a list of word types in this file, and add these words to a dictionary (to track text counts for each word)
# in addition, add the word counts to the word count dictionary to track word frequencies
        word_list_T_unique = list(set(word_list_T))
        for x in word_list_T_unique:
            text_count_T[x] = text_count_T.get(x,0) + 1
            word_count_T[x] = word_count_T.get(x,0) + Counter(word_list_T)[x]

        word_list_R_unique = list(set(word_list_R))
        for x in word_list_R_unique:
            text_count_R[x] = text_count_R.get(x,0) + 1
            word_count_R[x] = word_count_R.get(x,0) + Counter(word_list_R)[x]

        word_list_T = []
        word_list_R = []

#calculate log-likelihood formula for each word in target dictionary
for i in (text_count_T):

        freq_T = text_count_T[i]
        freq_R = 0
        cfreq_T = word_count_T[i]
        cfreq_R = 0
#If the current word is in the reference corpus then use this formula
        if i in text_count_R:
            freq_R = text_count_R[i]
            cfreq_R = word_count_R[i]
            E_T = total_T * ((freq_T + freq_R) / (total_T + total_R))
            E_R = total_R * ((freq_T + freq_R) / (total_T + total_R))
            G2 = 2 * ((freq_T * math.log(freq_T / E_T)) + (freq_R * math.log(freq_R / E_R)))
            if (freq_R / E_R) > (freq_T / E_T):
                G2 = (G2 * -1)
            cE_T = words_total_T * ((cfreq_T + cfreq_R) / (words_total_T + words_total_R))
            cE_R = words_total_R * ((cfreq_T + cfreq_R) / (words_total_T + words_total_R))
            cG2 = 2 * (cfreq_T * math.log(cfreq_T / cE_T)) + (cfreq_R * math.log(cfreq_R / cE_R))
            if (cfreq_R / cE_R) > (cfreq_T / cE_T):
                cG2 = (cG2*-1)
            keyness[i] = (G2, cG2)

#If the current word is not in the reference corpus use this formula
        else:
            E_T = total_T * (freq_T + freq_R) / (total_T + total_R)
            E_R = total_R * (freq_T + freq_R) / (total_T + total_R)
            G2 = 2 * (freq_T * math.log(freq_T / E_T))
            cE_T = words_total_T * (cfreq_T + cfreq_R) / (words_total_T + words_total_R)
            cE_R = words_total_R * (cfreq_T + cfreq_R) / (words_total_T + words_total_R)
            cG2 = 2 * (cfreq_T * math.log(cfreq_T / cE_T))
            keyness[i] = (G2, cG2)

#Write out the words and keyness (log-likelihood) values for each word
count = 0
target_100 = []
ref_100 = []
text_target_100 = []
text_ref_100 = []

word_fr_t = 0
word_fr_r = 0
print()
print("Text dispersion keywords for", sys.argv[1])
dists = {}
for i in sorted(keyness, key = keyness.get, reverse=True):
        print(i, keyness[i][0])

