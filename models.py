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
