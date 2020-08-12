from janome.tokenizer import Tokenizer

t = Tokenizer()
text = 'すもももももももものうち'
for token in t.tokenize(text):
    if token.part_of_speech.find('名詞') >= 0:
        print(token)
