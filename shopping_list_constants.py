# sqlite constants
SQL_LIST_TABLES = """SELECT name FROM sqlite_master WHERE type='table';"""
SQL_DELETE_RECORD_PARAMETER = """DELETE FROM products WHERE rowid = ?"""
