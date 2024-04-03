from django.shortcuts import render
from PyDictionary import PyDictionary
from googletrans import Translator

def index(request):
    return render(request, 'index.html')

def wordview(request):
    search = request.GET.get('search')

    dictionary = PyDictionary()

    # Get meanings, synonyms, antonyms
    meaning = dictionary.meaning(search)
    synonyms = dictionary.synonym(search)
    antonyms = dictionary.antonym(search)

    # Translate the meaning into Hindi and Marathi using googletrans
    translator = Translator()
    hindi_translation = translator.translate(search, dest='hi').text
    marathi_translation = translator.translate(search, dest='mr').text

    context = {
        'meaning': meaning,
        'synonyms': synonyms,
        'antonyms': antonyms,
        'hindi_meaning': hindi_translation,
        'marathi_meaning': marathi_translation,
    }

    return render(request, 'word.html', context)
