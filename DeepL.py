import deepl

def translate(text, target):
    print("Translating: " + text + " in " + target)
    translator = deepl.Translator("ENTER KEY HERE") 
    result = translator.translate_text(text, target_lang=target) 
    translated_text = result.text
    print("Result: " + translated_text)
    return translated_text
