from importlib import resources
import duckdb

from database import csvs

class DuckDBDAO:
    def __init__(self, db_path: str) -> None:
        """ Create an in-memory database if `db_path` is not provided. """
        self.db_path = db_path if db_path else ":memory:"
        self.connection = duckdb.connect(db_path)

    def _read_definition_statement(self, filename: str):
        """ Define a table from a .sqlite file"""
        return self.connection.sql((resources(csvs) / filename).read_text())

    def get_bronze_properties(self):
        return self._read_definition_statement("bronze-properties.sql")

    def get_silver_properties(self):
        return self._read_definition_statement("silver-properties.sql")

    def get_silver_rentals(self):
        return self._read_definition_statement("silver-rentals.sql")