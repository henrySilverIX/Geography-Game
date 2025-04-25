import turtle
from assets.writerManager import GeographyManager



GeoManager = GeographyManager()
usa_state_data = GeoManager.geographyDataFrame

#Criação da tela do jogo
screen = turtle.Screen()
screen.title("U.S. States Game")
img_path = "public/img/blank_states_img.gif"
turtle.addshape(img_path)
turtle.shape(img_path)


GAME_IS_ON = True

corrected_states = 0

while GAME_IS_ON:
    states_guessed_write = []
    answer_state = screen.textinput(title=f"Corrected States: {corrected_states}/50", prompt="Type a state name that you remember:\nType Exit to leave")
    answer_state = answer_state.title()
    print(answer_state)
    screen.update()


    #Check if the state is in the list of all states
    if answer_state in GeoManager.column_state_list:
        GeoManager.write_state_on_map(answer_state)
        corrected_states += 1
        GeoManager.column_state_list.remove(answer_state)

    #Count if the player answer all states correctly or if the player's typed exit to leave the game
    if corrected_states == 50 or not GeoManager.column_state_list or answer_state == "Exit":
        break

    print(f"States Remaining: {len(GeoManager.column_state_list)}")



#Create a csv with the states that weren't typed
missing_states = GeoManager.create_csv_to_learn()
print(missing_states)