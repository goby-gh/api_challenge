BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 460acb4a4c71

CREATE TABLE noah.auction_results (
    auction_result_id BIGSERIAL NOT NULL, 
    created_at TIMESTAMP WITHOUT TIME ZONE, 
    modified_at TIMESTAMP WITHOUT TIME ZONE, 
    dc_id INTEGER, 
    dc_count INTEGER, 
    company TEXT, 
    unit_name TEXT, 
    service TEXT, 
    technology_type TEXT, 
    location TEXT, 
    cancelled TEXT, 
    efa NUMERIC(12, 6), 
    cleared_volume NUMERIC(12, 6), 
    clearing_price NUMERIC(12, 6), 
    delivery_start TIMESTAMP WITHOUT TIME ZONE, 
    delivery_end TIMESTAMP WITHOUT TIME ZONE, 
    dc_full_text TEXT, 
    efa_date DATE, 
    PRIMARY KEY (auction_result_id)
);

INSERT INTO alembic_version (version_num) VALUES ('460acb4a4c71') RETURNING alembic_version.version_num;

COMMIT;

