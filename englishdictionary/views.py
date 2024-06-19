from django.shortcuts import render
import requests

# Variables
base_api = f"https://api.dictionaryapi.dev/api/v2/entries/en/" # api = base_api + word

# Functions
def get_audio(data):
    for item in data:
        audio = item.get("audio")
        if audio:
            return audio
    return None

def get_pronounciation(data):
    for item in data:
        text = item.get("text")
        if text:
            return text
    return None


# Create your views here

def home(request):
    return render(request, 'index.html')

def result(request):
    # Set defaults to avoid undefined errors
    word = None
    pronounciation = None
    audio = None
    meanings = []

    try:
        word = request.GET['search']
        api = base_api + word
        response = requests.get(api)
        if response.status_code == 200:
            data = response.json()
            meanings = data[0]['meanings']
            pronounciation = get_pronounciation(data[0]['phonetics'])
            audio = get_audio(data[0]['phonetics'])
    except:
        pass

    print(audio, pronounciation)

    context = {
        'word': word,
        'audio': audio,
        'pronounciation': pronounciation,
        'meanings': meanings,
    }
    return render(request, 'result.html', context)