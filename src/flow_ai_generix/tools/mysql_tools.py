from typing import Any
from crewai_tools import BaseTool
from sqlalchemy import create_engine, text
import os

class MySQLQueryTool(BaseTool):
    name: str = "MySQL Query Tool"
    description: str = """
    Use this tool to execute MySQL queries and retrieve data from the database.
    """

    def _run(self, query: str) -> Any:
        """Execute a MySQL query and return results"""
        try:
            # Clean the input - remove any JSON formatting if present
            if isinstance(query, str):
                if query.startswith('{') and query.endswith('}'):
                    import json
                    query_dict = json.loads(query)
                    query = query_dict.get('query', query)

            connection = os.getenv("MYSQL_CONNECTION_STRING")
            if not connection:
                raise ValueError("MySQL connection string not found in environment variables")
            
            print(f"\nExecuting query:\n{query}\n")
            
            engine = create_engine(connection)
            with engine.connect() as conn:
                # Use SQLAlchemy text() to properly handle the query
                result = conn.execute(text(query))
                rows = result.fetchall()
                # Convert rows to list of dictionaries for better output
                columns = result.keys()
                return [dict(zip(columns, row)) for row in rows]
                
        except Exception as e:
            return f"Error executing query: {str(e)}"
