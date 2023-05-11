# Sqlalchemy db models
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()

class AuctionResult(db.Model):
    __tablename__ = 'auction_results'
    __table_args__ = {'schema': 'noah' }
    # Ours
    auction_result_id = db.Column(db.BigInteger, primary_key=True)
    created_at  = db.Column(
        db.DateTime,
        default=db.func.current_timestamp())
    modified_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())
    # From API
    dc_id = db.Column(db.Integer)
    dc_count = db.Column(db.Integer, nullable=True)
    company = db.Column(db.Text, nullable=True)
    unit_name = db.Column(db.Text, nullable=True)
    service = db.Column(db.Text, nullable=True)
    technology_type = db.Column(db.Text, nullable=True)
    location = db.Column(db.Text, nullable=True)
    cancelled = db.Column(db.Text, nullable=True)
    efa = db.Column(db.Numeric(12,6), nullable=True)
    cleared_volume = db.Column(db.Numeric(12,6), nullable=True)
    clearing_price = db.Column(db.Numeric(12,6), nullable=True)
    delivery_start = db.Column(db.DateTime, nullable=True)
    delivery_end = db.Column(db.DateTime, nullable=True)
    dc_full_text = db.Column(db.Text, nullable=True)
    efa_date = db.Column(db.Date, nullable=True)
    def __str__(self):
        return f"AuctionResult<{self.auction_result_id}>"
    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except SQLAlchemyError as e:
            print(f'error saving {self}: {e}')
            db.session.rollback()
            return False
    @classmethod
    def from_json(cls, res):
        ar_kw_args = {
            'dc_count': res.get('_count'),
            'dc_id': res.get('_id'),
            'dc_full_text': res.get('_full_text'),
            'company': res.get('Company'),
            'unit_name': res.get('Unit Name'),
            'efa_date': res.get('EFA Date'),
            'delivery_start': res.get('Delivery Start'),
            'delivery_end': res.get('Delivery End'),
            'efa': res.get('EFA'),
            'service': res.get('Service'),
            'cleared_volume': res.get('Cleared Volume'),
            'clearing_price': res.get('Clearing Price'),
            'technology_type': res.get('Technology Type'),
            'location': res.get('Location'),
            'cancelled': res.get('Cancelled')
        }
        new_auction_result = cls(**ar_kw_args)
        return new_auction_result

# Notes:
# Fields from the API:
# fields = [
#     {'id': '_count', 'type': 'int8'},
#     {'id': '_id', 'type': 'int4'},
#     {'id': '_full_text', 'type': 'tsvector'},
#     {'id': 'Company', 'type': 'text'},
#     {'id': 'Unit Name', 'type': 'text'},
#     {'id': 'EFA Date', 'type': 'date'},
#     {'id': 'Delivery Start', 'type': 'timestamp'},
#     {'id': 'Delivery End', 'type': 'timestamp'},
#     {'id': 'EFA', 'type': 'numeric'},
#     {'id': 'Service', 'type': 'text'},
#     {'id': 'Cleared Volume', 'type': 'numeric'},
#     {'id': 'Clearing Price', 'type': 'numeric'},
#     {'id': 'Technology Type', 'type': 'text'},
#     {'id': 'Location', 'type': 'text'},
#     {'id': 'Cancelled', 'type': 'text'}
# ]


example_records = [
    {   'Cancelled': '',
        'Cleared Volume': '39',
        'Clearing Price': '3',
        'Company': 'HABITAT ENERGY LIMITED',
        'Delivery End': '2023-05-10T03:00:00',
        'Delivery Start': '2023-05-09T23:00:00',
        'EFA': '1',
        'EFA Date': '2023-05-10',
        'Location': 'PR2',
        'Service': 'DCH',
        'Technology Type': 'Batteries',
        'Unit Name': 'AG-HEL00G',
        '_count': '35',
        '_full_text': "'-05':8,11,17 '-09':12 '-10':9,18 "
        "'00':14,15,20,21 '1':22 '2023':7,10,16 '3':25 "
        "'39':24 'ag':5 'ag-hel00g':4 'batteri':26 "
        "'dch':23 'energi':2 'habitat':1 'hel00g':6 "
        "'limit':3 'pr2':27 't03':19 't23':13",
        '_id': 250778},
    {   'Cancelled': '',
        'Cleared Volume': '16',
        'Clearing Price': '0.9',
        'Company': 'HABITAT ENERGY LIMITED',
        'Delivery End': '2023-05-10T07:00:00',
        'Delivery Start': '2023-05-10T03:00:00',
        'EFA': '2',
        'EFA Date': '2023-05-10',
        'Location': 'OL113HA',
        'Service': 'DCL',
        'Technology Type': 'Batteries',
        'Unit Name': 'AG-HEL0AG',
        '_count': '35',
        '_full_text': "'-05':8,11,17 '-10':9,12,18 '0.9':25 "
        "'00':14,15,20,21 '16':24 '2':22 '2023':7,10,16 "
        "'ag':5 'ag-hel0ag':4 'batteri':26 'dcl':23 "
        "'energi':2 'habitat':1 'hel0ag':6 'limit':3 "
        "'ol113ha':27 't03':13 't07':19",
        '_id': 250789}]
