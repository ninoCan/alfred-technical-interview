CREATE TABLE IF NOT EXISTS bronze_properties (
    id INTEGER PRIMARY KEY,
    price INTEGER NOT NULL CHECK (price > 0),
    location TEXT NOT NULL,
    type TEXT CHECK (type = ''),
)