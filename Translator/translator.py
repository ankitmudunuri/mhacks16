from googletrans import Translator

translator = Translator()

s = ("right and when were in legendary was all their stuff too")
s.encode(encoding='utf-8')

x = translator.translate(s, dest='es', src='en')
print(x.text)