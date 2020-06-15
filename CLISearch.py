#!/usr/bin/env python3
#Author: Jeremy Eudy
import json
import requests
import sys
from urllib.parse import urlencode, quote_plus
from py_expression_eval import Parser


#api url format: https://api.duckduckgo.com/?q=DuckDuckGo&format=json 
#standard url format: https://duckduckgo.com/?q=test+search&atb=v1-1&ia=web

search = sys.argv
parser = Parser()
wiki = False
if len(search) == 1 or search[1] == '-w' and len(search) == 2:
    print("\nUsage: search *search string*")

else:
    urlFront = "https://api.duckduckgo.com/?"
    altUrlFront = "https://duckduckgo.com/?q="
    altUrlBack = "&atb-v1-1&ia=web"
    if search[1] == '-w':
        wiki = True
        search.pop(1)
    apiSearch = ''.join(search[1:])
    stdSearch = '+'.join(search[1:])
    params = {'q': apiSearch, 'o':'json'}
    url = urlFront+urlencode(params, quote_via=quote_plus)
    altUrl = altUrlFront+stdSearch+altUrlBack

    try:
        answer = json.loads(requests.get(url).text)

    except:
        print("Please connect to a network.")
        sys.exit()

    if answer['Answer'] != '' and answer['Answer']['id'] == 'calculator':
        exp = str(parser.parse(apiSearch).evaluate({}))
        print('{} = {}'.format(apiSearch, exp))

    elif wiki == False:
        topics = answer['RelatedTopics']
        text = list("")
        urls = list("")
        counter = 0
        for elem in topics:
            try:
                if(elem['FirstURL'] != None):
                    counter+=1
            except:
                pass

        if counter == 0:
            print("No instant answers available, here's a direct link:\n\t{}\n".format(altUrl))

        if counter != 0:
            print('Abstract URL:\n\t{}\n'.format(answer['AbstractURL']))
            print('Related topics:')

            for i in range(0, counter):
                text.append(topics[i]['Text'])
                urls.append(topics[i]['FirstURL'])

            for i in range(0, counter):
                print('\t{}\n\t{}\n'.format(text[i], urls[i]))

