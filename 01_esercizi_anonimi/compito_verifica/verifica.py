import json
from flask import Flask, request, render_template

app = Flask(__name__)


def read_file_json(filename: str) -> list:
    with open(filename, 'r') as file:
        data = json.load(file)
    return data
 
def update_file_json(filename, colors_list):
    with open(filename, 'w') as f:
        json.dump(colors_list, f)

#è troppo complesso non ci capisco più niente


def add_new_user_data(name: str, surname: str, favourite_color: str, colors_list: list) -> None:
    user_item = {
        "name": name,
        "surname": surname,
        "favourite_color": favourite_color
    }
    colors_list.append(user_item)

#tra poco impazzisco

def get_favourites_colors():
    colors_list = read_file_json('colors.json')
    if colors_list is not None:
        return [user["favourite_color"] for user in colors_list]
    else:
        return []

def get_colors_by_name(name, surname):
    colors_list = read_file_json('colros.json')
    if colors_list is not None:
        return [user["favourite_color"] for user in colors_list if user["name"] == name and user["surname"] == surname]
    else:
        return []
    
    #il 6 politico me lo merito
    

filename = 'colors.json'

colors_list = read_file_json(filename)
print(colors_list)

name = str(input("Inserire nome da aggiungere"))
surname = str(input("Inserire cognome da aggiungere"))
favourite_color = str(input("Inserire colore da aggiungere"))

add_new_user_data(name, surname, favourite_color, colors_list)

print("new list")
print(colors_list)


# aggiorna file json
update_file_json(filename, colors_list)

