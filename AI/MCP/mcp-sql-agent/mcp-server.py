import sqlite3
import re
from loguru import logger
from fastmcp import FastMCP




mcp = FastMCP("SQL Agent Server")

SAFE_QUERY_PATTERN = re.compile(r"^\s*SELECT\b", re.IGNORECASE)

# Whitelist of allowed tables (optional, but safer)
ALLOWED_TABLES = {"users", "nutrition", "meals"}

@mcp.tool()
def query_data(sql: str) -> str:
    """Execute SQL queries safely."""
    logger.info(f"Executing SQL query: {sql}")
    
    if not SAFE_QUERY_PATTERN.match(sql):
        return "Error: Only SELECT queries are allowed for security reasons."
    tokens = re.findall(r"\bFROM\s+(\w+)", sql, re.IGNORECASE)
    for table in tokens:
        if table.lower() not in ALLOWED_TABLES:
            return f"Error: Access to table '{table}' is not allowed."
    connection = sqlite3.connect("./database.db") # target db
    
    try:
        result = connection.execute(sql).fetchall()
        connection.commit()
        return "\n".join(str(row) for row in result)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        connection.close()

if __name__ == "__main__":
    print("Starting server...")
    mcp.run(transport="stdio")
        
