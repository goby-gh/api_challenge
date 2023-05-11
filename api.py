# API Calls
import requests
import datetime
from urllib import parse
from pprint import pprint

def fetch_todays_results():
    ''' Quick and dirty api call using the example code
        generated by the query builder (with my date modification) so I can
        get data flowing and rough out the rest.
    '''
    today_date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
    tomorrow_str = tomorrow.strftime("%Y-%m-%d")
    # Define api params
    sql_query =  f'''SELECT COUNT(*) OVER () AS _count, * FROM "ddc4afde-d2bd-424d-891c-56ad49c13d1a" WHERE "Company" = 'HABITAT ENERGY LIMITED' AND "EFA Date" >= '{today_date_str}T00:00:00.000Z' AND "EFA Date" < '{tomorrow_str}T00:00:00.000Z' ORDER BY "_id" ASC LIMIT 100'''
    params = {'sql': sql_query}
    # Query the api
    try:
        response = requests.get('https://api.nationalgrideso.com/api/3/action/datastore_search_sql', params = parse.urlencode(params))
        data = response.json()["result"]
        print("Received:")
        pprint(data) # Printing data
    except requests.exceptions.RequestException as e:
        print(e.response.text)
    return response.json()["result"]["records"]
