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
    # Set config paths relative to current file
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def query_writer(self) -> Agent:
        llm = LLM(model="o1-preview")
        return Agent(
            config=self.agents_config['query_writer'],
            llm=llm,
            verbose=True
        )

    @agent
    def query_reviewer(self) -> Agent:
        llm = LLM(model="o1-preview")
        return Agent(
            config=self.agents_config['query_reviewer'],
            tools=[MySQLQueryTool()],
            llm=llm,
            verbose=True
        )
    
    @agent
    def data_analyst(self) -> Agent:
        llm = LLM(model="o1-preview")
        return Agent(
            config=self.agents_config['data_analyst'],
            llm=llm,
            verbose=True
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
            agent=self.query_reviewer()
        )
    
    @task
    def document_results(self) -> Task:
        return Task(
            config=self.tasks_config['document_results'],
            output_file= 'Database_analysis.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Database Analysis crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True
        )