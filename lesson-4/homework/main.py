from mcp.server.fastmcp import FastMCP
import psycopg2
from psycopg2.extras import RealDictCursor

mcp = FastMCP("Demo PostgreSql")

DB_CONFIG = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "Dilrabo_613",
    "port": "5432"
}

@mcp.tool()
def execute_query(sql: str) -> str:
    """
    Executes SQL query on PostgreSQL database and returns result.
    Designed to handle SELECT queries and return data in a readable format.
    """
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor(cursor_factory=RealDictCursor)
        
        cur.execute(sql)
        
        if cur.description:
            results = cur.fetchall()
            cur.close()
            conn.close()
            return str(results)
        
        conn.commit()
        cur.close()
        conn.close()
        return "Success"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="stdio")