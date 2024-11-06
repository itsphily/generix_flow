from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class WriteXCrew:
    """Research Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def x_writer_agent(self) -> Agent:
        return Agent(config=self.agents_config["x_writer_agent"], verbose=True)

    @task
    def write_x_task(self) -> Task:
        return Task(
            config=self.tasks_config["write_x_task"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Write X Crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
