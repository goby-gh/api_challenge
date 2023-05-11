# 2021-01-08
# Backend technical challenge
#
from api import fetch_todays_results
from models import db, AuctionResult

# This is SILLY (since this app doesn't serve anything)
# but its the quickest way I know of to get sqlalch and alembic up and running and I'm working as fast as I can!
from flask import Flask, request
from flask_migrate import Migrate

# Create an App to handle config and let us invoke flask on the command line
class Config(object):
    # Postgres connection info not used by sqlalchemy
    _PGUSER        = 'postgres'
    _PGDATABASE    = "habitat"
    _PGPASSWORD    = 'energy'
    _PGHOST        = 'db'
    _PGPORT        = '5432'
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{_PGUSER}:{_PGPASSWORD}@{_PGHOST}:{_PGPORT}/{_PGDATABASE}"

def create_app(config_obj):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    db.init_app(app)
    Migrate(app, db)
    return app

app = create_app(Config)

if __name__ == '__main__':
    # Read the auction result (via the API)
    results = fetch_todays_results()
    print(f"Fetched {len(results)} auction results.")

    # Save the results
    with app.app_context():
        for res in results:
            ar = AuctionResult.from_json(res)
            ar.save()
            print(f"Saved {ar}")
