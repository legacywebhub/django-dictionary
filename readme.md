# About

This is an online English dictionary project built on Django web framework to get meanings, synonyms and antonyms of words. An external API was used to achieve this functionality.

# Libraries used

Django==3.2.2
requests==2.26.0

# API used

BASE API - https://api.dictionaryapi.dev/api/v2/entries/en/
Example - f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

# Challenge faced

API used was very dynamic with varying response per word/query. Extra measures were implemented to ensure the required values are gotten from the response.