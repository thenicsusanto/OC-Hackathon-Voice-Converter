import deepl

def translate(text, target):
    print("Translating: " + text + " in " + target)
    translator = deepl.Translator('e9cbd685-6cf3-e907-9336-b0a06e3def40:fx') 
    result = translator.translate_text(text, target_lang=target) 
    translated_text = result.text
    print("Result: " + translated_text)
    return translated_text