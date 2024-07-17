import os
import json

import requests as r
import wikipediaapi

import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy

import pandas as pd


pd.set_option('display.max_columns', None) # show all columns
pd.set_option('display.max_rows', None) # show all rows
pd.set_option('display.width', 200) # widen display width if needed

# search for topic: topic name -> article names, pages_id
API_ENDPOINT = 'https://en.wikipedia.org/w/api.php' # API endpoint to query pages from
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'
VALID_ENTITIES = ['PERSON','NORP','FAC','ORG','GPE','LOC','PRODUCT','EVENT','WORK_OF_ART','LAW','LANGUAGE']
WIKI = wikipediaapi.Wikipedia(USER_AGENT, 'en')

def save_to_json(new_data: dict):

    try:
        with open(r'articles.json', mode='r') as data_file:
            # Reading old data
            data = json.load(data_file)

    except FileNotFoundError:
        with open(r'articles.json', mode='w') as data_file:
            # Saving updated data
            json.dump(new_data, data_file, indent=4)

    else:
        for title, url in new_data.items():        
            if title in data:
                print(f'The page "{title}" has already been saved.')
            else:
                # Updating old data with new data
                data.update({title : url})
                with open(r'data.json', mode='w') as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)

def get_articles(topic: str, limit: int):
    search_params = {
        'action' : 'query', # to fetch data
        'list' : 'search', # to perform a full-text search
        'srsearch' : topic, # query for text
        'srlimit' : limit, # items to return
        'format' : 'json', # return format
        'maxlag' : 1 # will prevent task from running when the load on the servers is high: Wiki team's official recommendation when scraping pages.
    }

    resp = r.get(API_ENDPOINT, params=search_params, timeout=10)

    # search for url: title, pageid -> title, url
    titles = {}
    pages = resp.json()['query']['search']

    for page in pages:
        titles.update({page['title'] : page['pageid']})
    
    url_titles = {}
    for title, pageid in titles.items():
        parse_params = {
            'action' : 'query',
            'prop': 'info', # to query for an info about a page
            'inprop': 'url', # to query specificaty for a URL
            'pageids': pageid,
            'format': 'json',
        }

        resp1 = r.get(API_ENDPOINT, params=parse_params, timeout=10)
        url = resp1.json()['query']['pages'][f'{pageid}']['fullurl']
        page_title = url.split("/")[-1]
        
        url_titles.update({title : page_title})
    
    return url_titles


# Get page text: page URL title -> text of the article
def get_text(page_title):
    page = WIKI.page(page_title)
    article_text = page.text
    
    return article_text


# text processing -> clean text
def process_text(article_text):
    tokens = word_tokenize(article_text)

    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    cleaned_tokens = [re.sub(r'[^a-zA-Z0-9]', '', word.lower()) for word in filtered_tokens if word.isalnum()]

    cleaned_text = ' '.join(cleaned_tokens)
    
    return cleaned_text


# Get entities from an article -> list of entities
def get_entites(cleaned_text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(cleaned_text)
    entities = [(entity.text, entity.label_) for entity in doc.ents if entity.label_ in VALID_ENTITIES]

    return entities


# filter entities -> list of unique entitites
def filter_entities(entities):
    unique_entities = set()

    filtered_entities = []
    for entity_text, entity_label in entities:
        if entity_text not in unique_entities:
            unique_entities.add(entity_text)
            filtered_entities.append((entity_text, entity_label))
    
    return filtered_entities


# fetch wiki url for entity
def fetch_wikipedia_page(entity):
    page = WIKI.page(entity)
    if page.exists():
        return page.fullurl
    else:
        return None


# map entitites to a wikipedia article
def map_entities(filtered_entities):
    
    linked_entities = []
    for entity_text, entity_label in filtered_entities:
        page_url = fetch_wikipedia_page(entity_text)
        if page_url:
            linked_entities.append((entity_text, entity_label, page_url))
        else:
            linked_entities.append((entity_text, entity_label, None))

    return linked_entities

def save_data(df, filename, title):
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
        print(f"Appended {title} to {filename}")
    else:
        df.to_csv(filename, index=False)
        print(f"Created and saved {title} to {filename}")

titles = get_articles('Russian-Ukrainian War', 13)
print('Articles found!')
save_to_json(titles)
print('Articles saved!')

for title, page_title in titles.items():
    article_text = get_text(page_title)
    cleaned_text = process_text(article_text)
    entities = get_entites(cleaned_text)
    filtered_entities = filter_entities(entities)
    # linked_entities = map_entities(filtered_entities)
    # print('Mapped Entities...')

    df = pd.DataFrame(filtered_entities, columns=['Entity', 'Label']).assign(Article=title)
    save_data(df, 'data.csv', title)