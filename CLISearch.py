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
if(len(search) == 0):
    print("Usage: search *search string*")

else:
    urlFront = "https://api.duckduckgo.com/?"
    altUrlFront = "https://duckduckgo.com/?q="
    altUrlBack = "&atb-v1-1&ia=web"
    apiSearch = ''.join(search[1:])
    stdSearch = '+'.join(search[1:])
<<<<<<< HEAD
    params = {'q': apiSearch, 'o':'json'}
=======
    params = {'q': search[1:], 'o':'json'}
>>>>>>> 986f30eaeb1824860bcf38fd334b1f27c5a5d9a5
    url = urlFront+urlencode(params, quote_via=quote_plus)
    altUrl = altUrlFront+stdSearch+altUrlBack

    try:
        print(url)
        answer = json.loads(requests.get(url).text)

    except:
        print("Please connect to a network.")
        sys.exit()

    if(answer['Answer'] != '' and answer['Answer']['id'] == 'calculator'):
        exp = str(parser.parse(apiSearch).evaluate({}))
        print('{} = {}'.format(apiSearch, exp))

    else:
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

        if(counter == 0):
            print("No instant answers available, here's a direct link:\n\t{}\n".format(altUrl))

<<<<<<< HEAD
        if counter != 0:
            print('Abstract URL:\n\t{}\n'.format(answer['AbstractURL']))
            print('Related topics:')
=======
        else:
            print('Abstract URL:\n\t{}\n'.format(answer['AbstractURL']))
>>>>>>> 986f30eaeb1824860bcf38fd334b1f27c5a5d9a5

            for i in range(0, counter):
                text.append(topics[i]['Text'])
                urls.append(topics[i]['FirstURL'])

            print('Related topics:')

            for i in range(0, counter):
                print('\t{}\n\t{}\n'.format(text[i], urls[i]))

