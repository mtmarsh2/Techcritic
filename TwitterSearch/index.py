__author__ = 'Asus'
from TwitterAPI import TwitterAPI
import nltk

sentence = "BioBots Is A 3D Printer For Living Cells"
tokens = nltk.word_tokenize(sentence.lower())
filtered_words = [w for w in tokens if not w in nltk.corpus.stopwords.words('english')]
tagged = nltk.pos_tag(filtered_words)
print tagged
q=""
for pair in tagged:
    if pair[1]=='NN' or pair[1]=='NNP' or pair[1]=='NNS':
        q+=pair[0]+" "

print q

#consumer_key, consumer_secret, access_token_key, access_token_secret
api = TwitterAPI("",
                 "",
                 "",
                 "")
r = api.request('search/tweets', {'q':q,'count':'5','lang':'en'})
response = r.json()
for post in response["statuses"]:
    print post["text"]+"\n"