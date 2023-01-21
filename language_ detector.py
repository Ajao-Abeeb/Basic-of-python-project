import langid
def check_language(text):
    print(langid.classify(text)[0])
text = input("language")
    
check_language(text)
    