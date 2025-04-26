import turtle
from assets.writerManager import GeographyManager


print("Escolha um mapa (Brasil, USA ou Europa): ")
map_chosen = input().title()
GeoManager = GeographyManager(map_chosen)


#Criação da tela do jogo
screen = turtle.Screen()
screen.title("Country States")
screen.setup(width=750, height=750, startx=350, starty=10)
if map_chosen == "Usa" or map_chosen == "Eua":
    img_path = "public/img/blank_states_img.gif"
elif map_chosen == "Brasil" or map_chosen == "Brazil":
    img_path = "public/img/Brazil_states.gif"
elif map_chosen == "Europa" or map_chosen == "Europe":
    img_path = "public/img/Europa_countries.gif"
else:
    img_path = "public/img/nenhum_pais_selecionado.gif"
turtle.addshape(img_path)
turtle.shape(img_path)



GAME_IS_ON = True
corrected_states = 0
qtde_States_fixed = GeoManager.StatesFixedQTDE



# def print_coord(x, y):
#     print(f"{int(x)},{int(y)}")
# screen.onscreenclick(print_coord)


#Managing the game
while GAME_IS_ON:
    USER_PROMPT = "Type a state name that you remember:\nType Exit to leave"
    TITLE_INPUT = f"Corrected States: {corrected_states}/{qtde_States_fixed}"
    states_guessed_write = []
    answer_state = screen.textinput(title=TITLE_INPUT, prompt=USER_PROMPT)
    answer_state = GeoManager.personalized_title(answer_state)
    print(answer_state)
    screen.update()


    #Check if the state is in the list of all states
    if answer_state in GeoManager.column_state_list:
        GeoManager.write_state_on_map(answer_state)
        corrected_states += 1
        if answer_state in GeoManager.pt_list:
            GeoManager.en_list.pop(GeoManager.pt_list.index(answer_state))
            GeoManager.pt_list.remove(answer_state)
            GeoManager.column_state_list.clear()
            GeoManager.column_state_list = GeoManager.en_list + GeoManager.pt_list
        else:
            GeoManager.pt_list.pop(GeoManager.en_list.index(answer_state))
            GeoManager.en_list.remove(answer_state)
            GeoManager.column_state_list.clear()
            GeoManager.column_state_list = GeoManager.en_list + GeoManager.pt_list


    #Count if the player answer all states correctly or if the player's typed exit to leave the game
    if corrected_states == 50 or not GeoManager.column_state_list or answer_state == "Exit":
        break

    print(f"States Remaining: {int(len(GeoManager.column_state_list)/2)}")


#Only creates a csv learn file if there's a missing states
if len(GeoManager.column_state_list) != 0:
    #Create a csv with the states that weren't typed
    missing_states = GeoManager.create_csv_to_learn()
    print(missing_states)


# turtle.mainloop()
