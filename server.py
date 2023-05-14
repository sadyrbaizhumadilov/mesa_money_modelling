from model import MoneyModel
import mesa
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid,ChartModule
from mesa.visualization.UserParam import UserSettableParameter

NUMBER_OF_CELL=30
SIZE_OF_CANVAS_IN_PIXELS_X=700
SIZE_OF_CANVAS_IN_PIXELS_Y=500
simulation_params= {
    "number_of_agents": UserSettableParameter( 
    "slider",
    "Number of Agents",
    50, #default
    10, #min 
    200, #max
    1.0, #step
    description="Choose how many agents to include in the simulation",
    ),
   
    "width": NUMBER_OF_CELL,
    "height": NUMBER_OF_CELL,
}


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "r": agent.wealth +0.1}

    if agent.wealth > 2:
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
    elif agent.wealth > 1:
        portrayal["Color"] = "yellow"
        portrayal["Layer"] = 1
    elif agent.wealth > 0:
        portrayal["Color"] = "red"
        portrayal["Layer"] = 2
    else:
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 3
        portrayal["r"] = 0.7
    return portrayal

grid = CanvasGrid(agent_portrayal, NUMBER_OF_CELL, NUMBER_OF_CELL, SIZE_OF_CANVAS_IN_PIXELS_X, SIZE_OF_CANVAS_IN_PIXELS_Y)

chart_currents=ChartModule(
    [
    {"Label":"Wealthy Agents","Color":"green"},
     {"Label":"Non Wealthy Agents","Color":"grey"},
    ],
    canvas_height=300,
    data_collector_name="datacollector_currents"

)
server = ModularServer(MoneyModel,
                       [grid,chart_currents], "Money Model",simulation_params)

server.port = 8521 # The default
server.launch()