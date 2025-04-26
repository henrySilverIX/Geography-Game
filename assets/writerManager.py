import pandas
from turtle import Turtle
import os

# Utilização do pacote os para guardar a informação do caminho absoluto da pasta do projeto
# Caminho absoluto baseado na localização do script
base_path = os.path.dirname(__file__)

ALIGNMENT = "center"
CLASS_FAMILY = "Montserrat"


class GeographyManager(Turtle):
    def __init__(self, mapa):
        super().__init__()
        self.mapa = mapa
        if self.mapa == 'Usa' or self.mapa == "Eua":
            csv_path = os.path.join(base_path, '..', 'public', 'data', '50_states.csv')
        elif mapa == "Brasil" or self.mapa == "Brazil":
            csv_path = os.path.join(base_path, '..', 'public', 'data', '26_states_brazil.csv')
        elif mapa == "Europa" or self.mapa == "Europe":
            csv_path = os.path.join(base_path, '..', 'public', 'data', 'europe_countries.csv')
        else:
            csv_path = os.path.join(base_path, '..', 'public', 'data', 'europe_countries.csv')

        self.geographyDataFrame = pandas.read_csv(csv_path)
        self.pt_list = self.geographyDataFrame["state_name_pt"].tolist()
        self.en_list = self.geographyDataFrame["state_name_en"].tolist()
        self.column_state_list = self.pt_list + self.en_list
        self.StatesFixedQTDE = int(len(self.column_state_list) / 2)
        self.create_state_marker()

    def create_state_marker(self):
        self.penup()
        self.hideturtle()
        self.color("black")
        self.speed("fastest")


    def write_state_on_map(self, state_name):
        #Guarda a informação de uma linha em uma variável
        state_info_row = self.geographyDataFrame[(self.geographyDataFrame["state_name_pt"] == state_name) | (self.geographyDataFrame["state_name_en"] == state_name)]
        coordinate_x = state_info_row.x.item()
        coordinate_y = state_info_row.y.item()
        self.goto(coordinate_x,coordinate_y)
        self.write(f"{state_name}", False, align=ALIGNMENT, font=(CLASS_FAMILY, 8, 'normal'))


    def personalized_title(self, frase):
        excecoes = {'e', 'de', 'do', 'da', 'em', 'and'}
        palavras = frase.split()
        resultado = []
        for i, palavra in enumerate(palavras):
            if palavra.lower() in excecoes and i != 0:
                resultado.append(palavra.lower())
            else:
                resultado.append(palavra.capitalize())
        return ' '.join(resultado)


    def create_csv_to_learn(self):
        mapa_selected = self.mapa
        missing_states_dict = {"states remaining": self.column_state_list}
        missing_states = pandas.DataFrame(missing_states_dict)
        missing_states.to_csv(f"public/data/states_to_learn_{mapa_selected}.csv")
        return missing_states

