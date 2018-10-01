import spacy
from nltk import Tree


nlp = spacy.load('en')
# #             0         1    2       3          4        5       6
# doc = nlp(u"Autonomous cars shift insurance liability toward manufacturers")

doc = nlp(u"parrot is a bird.")
case1 = nlp(u'What are the companies which organize shark feeding events for scuba divers?')
case2 = nlp(u'What are the best hotels around snorkeling and surfing areas in Mauritius?')
case3 = nlp(u'What is the waiting time at Victoria Falls airport for a visa?')
case4 = nlp(u'Are insects like mosquitos an issue in Mauritius?')
case5 = nlp(u'[parrot] is a member of the [bird] family')
case6 = nlp(u'Dog is an animal.')
case7 = nlp(u'Rat is an animal')
case8 = nlp(u'Dogs such as animals, are very clever')

def to_nltk_tree(node):
    # print('node :', node)
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


def extract_noun_chunks():
    for chunk in doc.noun_chunks:
        print(chunk.text, chunk.root.text, chunk.root.dep_,
              chunk.root.head.text)
        print("chunk_orth_",chunk.orth_)
        print("chunk_start", chunk.start)
        print("chunk_end", chunk.end)



# [to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
# [extract_noun_chunks()]

[to_nltk_tree(sent.root).pretty_print() for sent in case1.sents]
[to_nltk_tree(sent.root).pretty_print() for sent in case2.sents]
[to_nltk_tree(sent.root).pretty_print() for sent in case3.sents]
[to_nltk_tree(sent.root).pretty_print() for sent in case4.sents]
[to_nltk_tree(sent.root).pretty_print() for sent in case5.sents]
[to_nltk_tree(sent.root).pretty_print() for sent in case6.sents]
[to_nltk_tree(sent.root).pretty_print() for sent in case7.sents]
[to_nltk_tree(sent.root).pretty_print() for sent in case8.sents]

for sent in case6.sents:
    for token in sent:
        print(token, token.pos_, token.dep_)