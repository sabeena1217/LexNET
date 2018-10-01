# pip install pycorenlp

from pycorenlp import StanfordCoreNLP

if __name__ == '__main__':
    nlp = StanfordCoreNLP('http://localhost:9000')
    text = (
        'DOg is an animal.')
    output = nlp.annotate(text, properties={
        'annotators': 'tokenize,ssplit,pos,,lemma,depparse,parse',
        'outputFormat': 'json'
    })
    tokens = output['sentences'][0]['tokens']
    for token in tokens:
        print token['lemma']

    print(output['sentences'][0]['parse'])
    print(tokens)


    output = nlp.tokensregex(text, pattern='/Pusheen|Smitha/', filter=False)
    print(output)
    output = nlp.semgrex(text, pattern='{tag: VBD}', filter=False)
    print(output)