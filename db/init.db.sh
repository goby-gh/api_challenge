#!/bin/bash

# This script runs exactly once: the first time this docker image is instanced and ran.
#
# As part of resolving this script (and other db setup) the postgres backend creates some files in the data directory that have a side-effect of acting as a semaphore that initialization has already ran.
#

set -e
echo "  ~~~~~                                        ~~~~~~"
echo " ~~~~~~ RUNNING custom sql on first-time init! ~~~~~~~"
echo "~~~~~~~                                        ~~~~~~~~"
psql -v ON_ERROR_STOP=1 --username postgres --dbname habitat <<-EOSQL
  BEGIN;
    CREATE SCHEMA IF NOT EXISTS noah;
    -- Note: Data can't be added here because the db migrations haven't been run yet.
  COMMIT;
EOSQL

# Run the migration file 
psql -v ON_ERROR_STOP=1 --username postgres --dbname habitat -f /tmp/migrations.sql
