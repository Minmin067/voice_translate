from googletrans import Translator
tr = Translator()
text = tr.translate(text="hello", src="en", dest="ja").text
print(text)