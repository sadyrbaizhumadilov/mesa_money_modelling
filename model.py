import mesa
from agent import MoneyAgent
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector

class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, number_of_agents, width, height):
        self.num_agents = number_of_agents
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running=True
        self.datacollector_currents=DataCollector(
            {
               "Wealthy Agents":MoneyModel.current_wealthy_agents,
               "Non Wealthy Agents":MoneyModel.current_non_wealthy_agents,
            

        })
        # Create agents
        for i in range(self.num_agents):
            a = MoneyAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    
    def step(self):
        self.schedule.step()
        self.datacollector_currents.collect(self)
    @staticmethod
    def current_wealthy_agents(model) -> int:
      return sum([1 for agent in model.schedule.agents if agent.wealth > 0])
    @staticmethod
    def current_non_wealthy_agents(model) -> int:
      return sum([1 for agent in model.schedule.agents if agent.wealth == 0])