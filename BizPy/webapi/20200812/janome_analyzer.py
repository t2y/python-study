from janome.analyzer import Analyzer
from janome.tokenfilter import POSKeepFilter, TokenCountFilter

text = 'すもももももももものうち'
token_filters = [POSKeepFilter('名詞'), TokenCountFilter()]
a = Analyzer(token_filters=token_filters)

for word, count in a.analyze(text):
    print(f'{word}: {count}')
