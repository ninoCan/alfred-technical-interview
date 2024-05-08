CREATE TEMP TABLE bronze_properties AS (
    SELECT * FROM read_csv('database/csvs/silver-rentals.csv')
);