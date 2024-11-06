from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from analyst_generix.tools.mysql_tools import MySQLQueryTool
from langchain.llms import OpenAI
import yaml
import os
from crewai import LLM

# Load environment variables at the start of the file
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))), '.env'))

# At the top of the file, after load_dotenv()
print(f"OpenAI API Key: {os.getenv('OPENAI_API_KEY')[:10]}...")  # Only print first 10 chars for security

# After load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

@CrewBase
class ResearchCrew:
    """Database Analysis crew"""
    # Get the current directory path
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Set config paths relative to current file
    agents_config = os.path.join(base_path, 'config', 'agents.yaml')
    tasks_config = os.path.join(base_path, 'config', 'tasks.yaml')

    def __init__(self):
        super().__init__()
        self.mysql_tool = MySQLQueryTool()

    @agent
    def query_writer(self) -> Agent:
        llm = LLM(model="gpt-4o")
        return Agent(
            config=self.agents_config['query_writer'],
            tools=[],
            llm=llm,
            verbose=True,
            memory=True
        )

    @agent
    def query_reviewer(self) -> Agent:
        llm = LLM(model="gpt-4o")
        return Agent(
            config=self.agents_config['query_reviewer'],
            tools=[MySQLQueryTool()],
            llm=llm,
            verbose=True,
            memory=True
        )
    

    @agent
    def data_analyst(self) -> Agent:
        llm = LLM(model="gpt-4o")
        return Agent(
            config=self.agents_config['data_analyst'],
            tools=[],
            llm=llm,
            verbose=True,
            memory=True
        )


    @task
    def write_queries(self) -> Task:
        return Task(
            config=self.tasks_config['write_queries'],
            agent=self.query_writer()
        )

    @task
    def review_and_execute_queries(self) -> Task:
        return Task(
            config=self.tasks_config['review_and_execute_queries'],
            agent=self.query_reviewer(),
            context=[self.write_queries()]
        )
    
    @task
    def document_results(self) -> Task:
        return Task(
            config=self.tasks_config['document_results'],
            agent=self.data_analyst(),
            context=[self.review_and_execute_queries(), self.write_queries()],
            output_file= "Database Analysis.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Database Analysis crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            memory=True,
            verbose=True
        )