import requests, uuid, json

# BING TRANSLATOR

# Example Return

# json_example = [
#     {
#         "detectedLanguage": {
#             "language": "en",
#             "score": 1.0
#         },
#         "translations": [
#             {
#                 "text": "Bewerk de JSON hieronder handmatig.",
#                 "to": "nl"
#             }
#         ]
#     }
# ]


def translate(text='', azureKey='', to_language='nl', json="true"):

    endpoint = 'https://api.cognitive.microsofttranslator.com/'

    subscription_key = azureKey

    path = '/translate?api-version=3.0'
    params = '&to=nl'
    constructed_url = endpoint + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [
        {
            'text': text
        }
    ]
    request = requests.post(constructed_url, headers=headers, json=body)
    if request.status_code != 200:
        raise PermissionError('Did you check the Microsoft Azure API-Key')
    response = request.json()
    if json:
        return response
    pretty_response = json.dumps(response, sort_keys=True, indent=4,
                 ensure_ascii=False, separators=(',', ': '))
    return pretty_response