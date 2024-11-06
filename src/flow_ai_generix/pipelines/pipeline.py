# Common imports for both examples
from crewai import Pipeline
from pathlib import Path

from ..crews.research_crew.research_crew import ResearchCrew
from ..crews.write_x_crew.write_x_crew import WriteXCrew


class FlowAiGenerixPipeline:
    def __init__(self):
        # Initialize crews
        self.research_crew = ResearchCrew().crew()
        #self.write_x_crew = WriteXCrew().crew()
    
    def create_pipeline(self):
        return Pipeline(
            stages=[
                self.research_crew,
                #self.write_x_crew
            ]
        )
    
    async def kickoff(self, inputs):
        pipeline = self.create_pipeline()
        # Convert inputs to list of dictionaries if it's not already
        stage_inputs = [inputs]  # Wrap the inputs dictionary in a list
        results = await pipeline.kickoff(stage_inputs)
        return results

