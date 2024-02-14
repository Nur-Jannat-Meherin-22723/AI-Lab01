import re
import requests
import pandas as pd

def clean_filename(filename):
    filename = re.sub(r'[\\/*?:"<>|]', "", filename)
    return filename

def build_payload(query, start=1, num=10, date_restrict = 'm1', **params):
        payload={
            'key' : API_KEY,
            'q' : query,
            'cx' : SEARCH_ENGINE_ID,
            'start' : start,
            'num' : num,
            'dataRestrict' : date_restrict
        }
        
        payload.update(params)
        return payload
    
def make_request(payload):
    response = requests.get('https://www.googleapis.com/customsearch/v1',params = payload)
    if response.status_code != 200:
        raise Exception('Request Failed')
    return response.json()

def main(query, result_total=10):
    items = []
    reminder = result_total%10
    if reminder > 0:
        pages = (result_total // 10) + 1
    else:
        pages = result_total // 10
        
    for i in range(pages):
        if pages == i+1 and reminder > 0:
            payload = build_payload(query, start=(i+1)*10, num=reminder)
        else:
            payload = build_payload(query, start=(i+1)*10)
        response = make_request(payload)
        items.extend(response['items'])
    query_string_clean = clean_filename(query)
    df = pd.json_normalize(items)
    # df.to_excel('Google Search Result_{0}.xlsx'.format(query_string_clean), index=False)
    # df.to_excel('Google Search Result_{0}.xlsx'.format(query_string_clean), index=False)
    try:
        file_path = r'D:\4-1\AI\Lab\Assignment_01\MMK_Task_02\search_api_lesson\Google Search Result_{0}.xlsx'.format(query_string_clean)
        df.to_excel(file_path, index=False)

        # df.to_excel('Google Search Result_{0}.xlsx'.format(query_string_clean), index=False)
        print("Excel file successfully created.")
    except Exception as e:
        print("Error creating Excel file:", e)


        

if __name__ == '__main__':
    API_KEY = 'AIzaSyAbd79evFzHrJREpL-bFLUrKQidOzHC4sk'
    SEARCH_ENGINE_ID = 'a0dcdef1d620a4ca4'
    search_query = 'Barak Obama'
    total_results = 3
    main(search_query,total_results)