from googleapiclient.discovery import build
import pprint

# use Google JSON API key & CSE Id
my_api_key = 'AIzaSyAM659XTN7L27KVybZG0rz9WdqPAgkGI9A'
my_cse_id = '3d1185b80729662d0'


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)

    res = service.cse().list(
                            q=search_term,
                            cx=cse_id,
                            # searchType='image',
                            # num=1,
                            **kwargs
                            ).execute()
    return res

result = google_search('Santosh Yadav CDW Canada', my_api_key, my_cse_id)

# pprint.pprint(result)

for item in result['items']:
    print(item['title'], item['link'])