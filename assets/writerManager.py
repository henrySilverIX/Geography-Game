import pandas
from turtle import Turtle
import os

# Utilização do pacote os para guardar a informação do caminho absoluto da pasta do projeto
# Caminho absoluto baseado na localização do script
base_path = os.path.dirname(__file__)

ALIGNMENT = "center"
CLASS_FAMILY = "Montserrat"


class GeographyManager(Turtle):
    def __init__(self, country):
        super().__init__()
        self.country = country
        if country == 'Usa':
            csv_path = os.path.join(base_path, '..', 'public', 'data', '50_states.csv')
        elif country == "Brasil":
            csv_path = os.path.join(base_path, '..', 'public', 'data', '26_states_brazil.csv')

        self.geographyDataFrame = pandas.read_csv(csv_path)
        self.column_state_list = self.geographyDataFrame["state"].tolist()
        self.create_state_marker()

    def create_state_marker(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")


    def write_state_on_map(self, state_name):
        #Guarda a informação de uma linha em uma variável
        state_info_row = self.geographyDataFrame[self.geographyDataFrame["state"] == state_name]

        coordinate_x = state_info_row.x.item()
        coordinate_y = state_info_row.y.item()
        self.goto(coordinate_x,coordinate_y)
        self.write(f"{state_name}", False, align=ALIGNMENT, font=(CLASS_FAMILY, 8, 'normal'))

    def create_csv_to_learn(self):
        country_selected = self.country
        missing_states_dict = {"states remaining": self.column_state_list}
        missing_states = pandas.DataFrame(missing_states_dict)
        missing_states.to_csv(f"public/data/states_to_learn_{country_selected}.csv")
        return missing_states

