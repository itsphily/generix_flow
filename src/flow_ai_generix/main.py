#!/usr/bin/env python
import asyncio
from flow_ai_generix.pipelines.pipeline import FlowAiGenerixPipeline
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

async def run():
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
   
    # Run the pipeline
    pipeline = FlowAiGenerixPipeline()
    results = await pipeline.kickoff(inputs)
    
    # Process and print results
    for result in results:
        print(f"Raw output: {result.raw}")
        if result.json_dict:
            print(f"JSON output: {result.json_dict}")
        print("\n")

def main():
    asyncio.run(run())

if __name__ == "__main__":
    main()