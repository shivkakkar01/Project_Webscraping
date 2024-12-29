from googletrans import Translator

def translate_text(text):
    """Translate text from Spanish to English."""
    translator = Translator()
    translated = translator.translate(text, src="es", dest="en")
    return translated.text
