# 2021-01-08
# Backend technical challenge
#
from api import fetch_todays_results
from models

# This is SILLY (since this app doesn't serve anything)
# but its the quickest way I know of to get sqlalch and alembic up and running and I'm working as fast as I can!
from flask import Flask, request
from flask_migrate import Migrate



# Intro:
#
# Habitat Energy submit their batteries into a frequency service called dynamic
# containment each day. The service operates as an auction where you submit your price
# and you find out if you are accepted or not.
#
# The results of the auction can be seen on the national grid ESO data page
# https://data.nationalgrideso.com/ancillary-services/dynamic-containment-data#. There is
# an API for this data -> click on tender results -> API.


# Read the auction result (via the API)
results = fetch_todays_results()

# Save the results
