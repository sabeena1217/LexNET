from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'../../stanford-corenlp-full-2018-02-27/', memory= '2g')
res = nlp.annotate("I love you. I hate him. You are nice. He is dumb",
                   properties={
                       'annotators': 'tokenize,ssplit,pos',
                       'outputFormat': 'json',
                       'timeout': 1000,
                   })

sentence = 'Dog is an animal.'
tokens = nlp.word_tokenize(sentence)
print 'Part of Speech:', nlp.pos_tag(sentence)
# print 'Named Entities:', nlp.ner(sentence)
print 'Constituency Parsing:', nlp.parse(sentence)
print 'Dependency Parsing:', nlp.dependency_parse(sentence)