import nltk
from nltk import ne_chunk
from nltk.chunk import tree2conlltags
from pprint import pprint
import regex as re
from nltk.corpus import stopwords
from textblob import TextBlob

#remove stopwords
#word_tokenize accepts a string as an input, not a file.
stop_words = set(stopwords.words('english'))
file1 = open("text.txt")
line = file1.read()# Use this to read file content as a stream:
words = line.split()
for r in words:
    if not r in stop_words:
        appendFile = open('filteredtext.txt','a')
        appendFile.write(" "+r)
        appendFile.close()
file1.close()

#split based on capital letters
file1 = open("filteredtext.txt")
article = file1.read()
file1.close()
l = re.split(r'[ ](?=[A-Z])', article)
f = open("new.txt", 'w')
for i in l:
    f.write(i)
    f.write('\n')
f.close()

#get noun phrases
f = open('new.txt', 'r')
f1 = open('new1.txt', 'w')
k = 1
article = f.readlines()
for i in article:
    if i != '\n':
        blob = TextBlob(i)
        f1.write(str(k))
        f1.write('.\n')
        for j in blob.noun_phrases:
            f1.write('\t*' + j)
            f1.write('\n')
        k+=1
f.close()
f1.close()


"""
f.close()
blob = TextBlob(article)
f = open('new1.txt', 'w+')
for i in blob.noun_phrases:
    f.write('*' + i)
    f.write('\n')
f.close()
"""
"""def fn_preprocess(art):
    art = nltk.word_tokenize(art)
    art = nltk.pos_tag(art)
    return art

art_processed = fn_preprocess(article)

results = ne_chunk(art_processed)

for x in str(results).split('\n'):
    if '/NN' in x:
        print(x)

pattern = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(pattern)
cs = cp.parse(art_processed)
print(cs)

iob_tagged = tree2conlltags(cs)
pprint(iob_tagged)"""