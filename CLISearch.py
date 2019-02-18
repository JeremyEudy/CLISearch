#Author: Jeremy Eudy
import json
import requests
import sys
from urllib.parse import urlencode, quote_plus
from py_expression_eval import Parser

search = sys.argv
parser = Parser()
if(len(search) == 0):
    print("Usage: search *search string*")
else:
    urlFront = "https://api.duckduckgo.com/?"
    search = ''.join(search[1:])
    params = {'q': search, 'o':'json'}
    url = urlFront+urlencode(params, quote_via=quote_plus)
    answer = json.loads(requests.get(url).text)
    if(answer['Answer'] != '' and answer['Answer']['id'] == 'calculator'):
        exp = str(parser.parse(search).evaluate({}))
        print('{} = {}'.format(search, exp))

    else:
        print('Abstract URL:\n\t{}\n'.format(answer['AbstractURL']))
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

        for i in range(0, counter):
            text.append(topics[i]['Text'])
            urls.append(topics[i]['FirstURL'])

        print('Related topics:')
        for i in range(0, counter):
            print('\t{}\n\t{}\n'.format(text[i], urls[i]))
