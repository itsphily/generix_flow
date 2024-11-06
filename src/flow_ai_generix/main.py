#!/usr/bin/env python
from crews.research_crew.research_crew import ResearchCrew
import os
from pathlib import Path


def read_file(file_name):
    """
    Read a file and return its contents
    """
    project_root = Path(__file__).parent.parent.parent
    file_path = os.path.join(project_root, "docs", file_name)
    
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"Could not find {file_name} at {file_path}")
        return None
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        return None

def run():
    """
    Run the pipeline.
    """
    # Read the files
    trends = read_file("trends.md")
    queries = read_file("queries.md")
    database_name = os.getenv("MYSQL_DATABASE_NAME")

    if not all([trends, queries, database_name]):
        print("Error: Missing required input files or environment variables")
        return

    # Set up inputs as a single dictionary
    inputs = {
        "trends": trends,
        "queries": queries,
        "database_name": database_name
    }
   
    ResearchCrew().crew().kickoff(inputs)

run()