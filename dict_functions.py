from deep_translator import GoogleTranslator

def translate_en_to_fa(text):
    """
    Translates English text to Persian.

    Args:
        text (str): The text to be translated.

    Returns:
        str: The Persian translation of the input text.
    """
    translator = GoogleTranslator(source='english', target='persian')
    translated_text = translator.translate(text)
    return translated_text

def translate_fa_to_en(text):
    """
    Translates Persian text to English.

    Args:
        text (str): The text to be translated.

    Returns:
        str: The English translation of the input text.
    """
    translator = GoogleTranslator(source='persian', target='english')
    translated_text = translator.translate(text)
    return translated_text


def translate_fr_to_en(text):
  """
  Translates French text to English.

  Args:
    text (str): The text to be translated.

  Returns:
    str: The English translation of the input text.
  """
  translator = GoogleTranslator(source='french', target='english')
  translated_text = translator.translate(text)
  return translated_text

def translate_en_to_fr(text):
  """
  Translates English text to French.

  Args:
    text (str): The text to be translated.

  Returns:
    str: The French translation of the input text.
  """
  translator = GoogleTranslator(source='english', target='french')
  translated_text = translator.translate(text)
  return translated_text


def translate_de_to_en(text):
  """
  Translates German text to English.

  Args:
    text (str): The text to be translated.

  Returns:
    str: The English translation of the input text.
  """
  translator = GoogleTranslator(source='german', target='english')
  translated_text = translator.translate(text)
  return translated_text

def translate_en_to_de(text):
  """
  Translates English text to German.

  Args:
    text (str): The text to be translated.

  Returns:
    str: The German translation of the input text.
  """
  translator = GoogleTranslator(source='english', target='german')
  translated_text = translator.translate(text)
  return translated_text

def translate_ar_to_en(text):
  """
  Translates Arabic text to English.

  Args:
    text (str): The text to be translated.

  Returns:
    str: The English translation of the input text.
  """
  translator = GoogleTranslator(source='arabic', target='english')
  translated_text = translator.translate(text)
  return translated_text

def translate_en_to_ar(text):
  """
  Translates English text to Arabic.

  Args:
    text (str): The text to be translated.

  Returns:
    str: The Arabic translation of the input text.
  """
  translator = GoogleTranslator(source='english', target='arabic')
  translated_text = translator.translate(text)
  return translated_text
