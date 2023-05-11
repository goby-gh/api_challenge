# API Calls
import requests


# Integrate this dataset using cURL (from the bottom of https://data.nationalgrideso.com/ancillary-services/dynamic-containment-data#)
# # Get a list of dataset's resources
# curl -L -s https://data.nationalgrideso.com/ancillary-services/dynamic-containment-data/datapackage.json | grep path
#
# # Get resources
# curl -L https://data.nationalgrideso.com/backend/datastore/dump/6fd8e042-be27-4c67-ad59-5acdd2a7b0fd
#
# curl -L https://data.nationalgrideso.com/backend/datastore/dump/26aefbcc-fce0-403f-80e1-4a26af3fe84b
#
# curl -L https://data.nationalgrideso.com/backend/datastore/dump/ddc4afde-d2bd-424d-891c-56ad49c13d1a
#
# curl -L https://data.nationalgrideso.com/backend/datastore/dump/888e5029-f786-41d2-bc15-cbfd1d285e96
#
# curl -L https://data.nationalgrideso.com/backend/dataset/aca07dcb-f807-409c-a4ec-da5dc052b8ba/resource/0b8dbc3c-e05e-44a4-b855-7dd1aa079c68/download/dynamic_containment_masterdata.csv

# Explore resources
URL = "https://data.nationalgrideso.com/ancillary-services/dynamic-containment-data/datapackage.json"
r = requests.get(URL)
r.json()

for src in r.json()['resources']:
    print(f"{src['name']}: {src['path']}")
