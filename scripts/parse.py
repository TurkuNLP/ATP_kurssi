from trankit import Pipeline
from trankit import trankit2conllu
import sys

p = Pipeline('english')

#doc_text = '''Hello! This is Trankit.'''

# perform all tasks on the input
for line in sys.stdin:
    line=line.strip()
    all = p(line)
    all_conllu = trankit2conllu(all)
    print(all_conllu)
