from janome.tokenizer import Tokenizer

t = Tokenizer()
text = 'すもももももももものうち'
for token in t.tokenize(text):
    print(token)
