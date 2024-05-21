import json

def open(filename: str) -> list:
    with open(filename, 'r') as file:
        data = json.load(file)
        
    return data
data = open('colors.json')

