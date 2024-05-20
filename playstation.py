import json
from pprint import pprint

import requests



headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': 'application/json',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://store.playstation.com/',
    'content-type': 'application/json',
    'X-PSN-Store-Locale-Override': 'en-TR',
    'X-PSN-App-Ver': '@sie-ppr-web-store/app/@sie-ppr-web-store/app@0.86.1-59ea95edc813eb4af70fbfef95adc32b06f5de4c',
    'X-PSN-Correlation-Id': 'cabc82a9-d620-4cf2-bb9d-9af385e945a9',
    'apollographql-client-name': '@sie-ppr-web-store/app',
    'apollographql-client-version': '@sie-ppr-web-store/app@0.86.1',
    'X-PSN-Request-Id': '2f742a0f-fad8-4929-91e9-b8eaefd2376a',
    'Origin': 'https://store.playstation.com',
    'Connection': 'keep-alive',
    # 'Cookie': '_abck=D0A994E7DEDA0E4D15B5494675AB2626~-1~YAAQXAxAF8A3hMuOAQAAAqmyCwuwCD072mXP2zBmA286jmGwft4jMwXyV/UdPHNLjVyRvz/hq2EUhEECQbLZYnQCzKWAWW2tsaoP79YEemilKs4x+88ZUqc3BNUeBiLUDcMarqq8BN1QsD/flGncbCxrnLCd+2Ro0ePdr8hO8rInISqrDU4Uf2suLscZ/piU/Y1aYNAY+HjW46M0qgSiVNCthnmxzSd8/zBgOegbhKFTwjEOJzn5LFtFdoiSogEajHleEW+3um1ahphUn4wtPrXy4Mjrl7YIt7WmSXZsaECvFkIFl2ftjw07bXq5vrikViN5+sIBuyEYXN6Npozb1MI09lOcEJNCb7hFtlPKFYBUzY4cC4yItveYWYPaPmheiios87OULzzF8Sm8SdZIJQ07Ck67QbG1rDOBnjDn24sZ8PsuuUMWYbTbug8TmgokUvxsiJgxaJDYkN/dgdGqHNZ9wCK+GAC1WtAmYrMbCCRrjvY=~-1~-1~-1; bm_sz=F27C241ED61B557F00D3F4F34B6F132A~YAAQXAxAF8E3hMuOAQAAAqmyCxfy5kBVbPo8eNaS80GJg8b0vYQlRth9eqfaZuGSDlVaV0f0XJh9JUkcIg1re2kxwpwFeTHgbcMqAtrG57d5i6ALS7FZLD6RgOF/HGHKymSulpnRK8YtNKceKYTTEDH2BA3TziGZJsbCq09Az5al5kkzXEVemZdqAvwmjiqXvT152DeBttYQ2MWZk2qJUfobcgy6VVwq+xj5EzLPZrnx28Gffz0vBT5vkDHLU2xKfpOcW4NlkET/4H7BiIMY/BYYoQeFisSCwaKwZXNrl7oKdL5/jDRTkEk8rvw8PQm8RzyBwqrvQmQDJM/BnmbB+QzJAs5iAg0qCQC0j6vqTzRaRdctA3vpCALWKl0m1XTLWoTq8V+XIZhuQLo1xz6IxPb7mz945sr8rnKxdC48Gnp6EO41K/DFmK5fMw==~3223619~3487282; ak_bmsc=C74822FA7552E4D3E1ED9C641F9D13FF~000000000000000000000000000000~YAAQhwxAFxcID8mOAQAALEmxCxdp5bKd4qhdn9Ia8n6lTPVXA8+iHcEuowShPH9G/NL7vsfTYQ2PYClEVKtDJmKiiV4ypC9WrWQLiGDK3QkSlm8jdnShvwc0Aqb+V0OnujE6BngMKBHDrsk6uKjeQai6x22ggPrBhf0zXMCEKG5Rt3ZBEkHCotvOYxkO6CxBgbj508Tw/xGnfd18Mx2slxQqf9svjWskkrbWxAIYSX6A6Lm7/bpiEQrBxvC6WW/jvbJhbJUVKkJeTWmzv6sAucbYHFSZLlP7toCDnu7YXj7Ke5utAGSQusulHCT/94+PWhKZPokZQzpn/6P0cOXohIRqSjaCe2NdFRFWk5KXILsrERav1KSNfaWcgo7U8N/knNruWyLamfNMZ0rqTy+9wTGN9Q==; bm_sv=7DD20346236C28D3B2C64A232A633977~YAAQhwxAF0AID8mOAQAAOEyxCxd8SJPDLzecbtiRlB5/Of0gYeqZ0yLkpn0+ps8jXJXPTK0pjFd+J8ohSptWL/I1myHv8NRsKV2w5Bl4f6nI9/xkVDrLr3xIPogsJkfbDDT7KG/4J1tbGgDVjoFMZ3kIWzaeIc0xABmmrA+rs7w9pAHrC/E4kso128tJ9TkjT8wdvroasCQW1h6q4gz/sQujU3R2TY4FttALvoWk8v3a9ivypo4ZRGBRtZgC4whOyIPzUGPcndQ=~1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    # Requests doesn't support trailers
    # 'TE': 'trailers',
}

params = {
    'operationName': 'queryRetrieveTelemetryDataPDPProduct',
    'variables': '{"conceptId":null,"productId":"EP7839-PPSA11382_00-8139869505025767"}',
    'extensions': '{"persistedQuery":{"version":1,"sha256Hash":"cfa5de2267b804d86eb54507238c29d7c63fe5a6bc2e439f89360eb16e7a4239"}}',
}

response = requests.get('https://web.np.playstation.com/api/graphql/v1//op', params=params, headers=headers)


pprint(response.json()['data']['productRetrieve']['webctas'][0]['price']['discountedPrice'].replace('\xa0TL',''))
#with open('play.json','w',encoding='utf-8') as f:
   # json.dump(response.json(), f, ensure_ascii=False, indent=2)