import csv 
import json
import pickle
from eventregistry import *

def create_datafiles(apiKey, lang, source_lst):

    #use 'https://eventregistry.org/documentation/api?tag=Event' to set more parameters
    url_endpoint = 'https://eventregistry.org/api/v1/event/getEvent'
    url_params = {  
                    'eventUri': '', 
                    'resultType': 'info', #use similarEvents info sourceExAggr
                    'includeEventTitle' : 'true',
                    'includeEventSummary' : 'true',
                    'includeEventSentiment' : 'true',
                    'includeEventLocation' : 'true',
                    'includeEventDate' : 'true',
                    'includeEventArticleCounts' : 'true',
                    'includeEventCategories' : 'true',
                    'includeSourceTitle' : 'true',
                    'includeSourceLocation' : 'true',
                    'includeSourceUri' : 'true',
                    'includeSourceRanking' : 'true',
                    'includeLocationCountryArea' : 'true',
                    'includeLocationCountryContinent' : 'true',
                    'includeEventConcepts' : 'false',
                    'apiKey' : ''
                }
    #REST API call to get the event details

    #csv file 
    csvfile = open('data/raw/dataset.csv', 'a', newline='\n')

    writer = csv.writer(csvfile, delimiter=',')

    with open("data/intermediate/uri_dict.txt", "rb") as myFile:
        uri_dict = pickle.load(myFile)

    fieldnames = ['uri','title','event_date','sentiment','categories','loc_country','loc_continent','article_count','total_article_count','summary']

    _list = []
    for src in source_lst:

        src_val = src.split('.')[0]
        _list.append(src_val)
        fieldnames.append(src_val)

    writer.writerow(fieldnames)

    source_lst = _list

    for uri in uri_dict:

        url_params['eventUri'] = uri
        url_params['apiKey'] = apiKey

        response = requests.get(url_endpoint, params=url_params)
        y = json.loads(response.text)
        
        for result in y: 
            row_text = []
            row_text.append(uri)
             
            row_text.append(y[uri]['info']['title'][lang].replace('\n', ''))
            row_text.append(y[uri]['info']['eventDate'])
            row_text.append(y[uri]['info']['sentiment'])

            if y[uri]['info']['categories']:
                cat_arr = ''
                for category in y[uri]['info']['categories']:
                    cat_arr += category['label'] + ', '

                row_text.append(cat_arr.rstrip(', '))
            else:
                row_text.append('-')
                
            if y[uri]['info']['location']:

                if y[uri]['info']['location']['country']:
                    row_text.append(y[uri]['info']['location']['country']['label']['eng'])
                else:
                    row_text.append('-')

                if y[uri]['info']['location']['country']['continent']:
                    row_text.append(y[uri]['info']['location']['country']['continent'])
                else:
                    row_text.append('-')
            else:
                row_text.append('-')
                row_text.append('-')
            
            row_text.append(y[uri]['info']['totalArticleCount'])
            row_text.append(y[uri]['info']['articleCounts'][lang])
                
            row_text.append(y[uri]['info']['summary'][lang].replace('\n', ' '))

            #row_text.append(source_uri)
            src_list = list(set(uri_dict[uri]))

            for src in source_lst:

                if src in src_list:
                    row_text.append('1')
                else:
                    row_text.append('0')

            writer.writerow(row_text)
