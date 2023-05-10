# 2021-01-08
# Backend technical challenge
#

'''
Intro:

Habitat Energy submit their batteries into a frequency service called dynamic
containment each day. The service operates as an auction where you submit your price
and you find out if you are accepted or not.

The results of the auction can be seen on the national grid ESO data page
https://data.nationalgrideso.com/ancillary-services/dynamic-containment-data#. There is
an API for this data -> click on tender results -> API.
'''

def fetch_auction_result():
    ''' Read the auction result (via the API)
    '''
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

def save_current_days_result():
    ''' Save Habitat's current day's result to a local database.

        > The database model and testing database you use is up to you.
        > Also this might not be the only data we get from ESO,
        > so think about your code structure.
    '''

'''
Additional info:

    > To complete the task we must be able to run your code to see that it works (try not to
    > make any assumptions about the operating system), so please add documentation to
    > explain how it works.
    >
    > Try not to spend more than 3 hours on this task. If the task is going to take you longer
    > than 3 hours, please send us what you have and write in the documentation what you
    > would do next. Please send us your code as a compressed archive e.g. zip, tar.gz, bzip2
    > etc.
    >
    > Happy coding
    > Habitat Energy Tech team
''''
