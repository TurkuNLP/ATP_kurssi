from trankit import Pipeline
from trankit import trankit2conllu
import sys

p = Pipeline('english')

#doc_text = '''Hello! This is Trankit.'''

# perform all tasks on the input
all = p(sys.stdin())
all_conllu = trankit2conllu(all)
print(all_conllu)
