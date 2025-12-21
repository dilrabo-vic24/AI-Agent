from database import engine
from sqlalchemy import text

def db_tool(sql_query: str) -> str:
    """
    Executes sql query in PostgreSql database. 
    Table: Products
    ColumnsL id(int), name(str), price(float), stock(int)
    Example: 'SELECT * FROM products WHERE price > 1000'
    """

    with engine.connect() as conn:
        result = conn.execute(text(sql_query))

        rows = [dict(row._mapping) for row in result]
        return str(rows)
    