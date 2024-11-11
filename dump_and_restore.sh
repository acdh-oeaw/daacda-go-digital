#!/bin/bash

pg_dump -d daacda -h localhost -p 5433 -U  daacda -c -f daacda_dump.sql
psql -U postgres -d daacda < daacda_dump.sql
