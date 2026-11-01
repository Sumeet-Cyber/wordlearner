from wordlearner.config import DATA
import json
import os

def load_initial_data():
    """This function loads the data file at startup, this file has the information about decks. It returns a Python dictionary of decks"""
    try:
        # data = str(config.DATA)
        with open(DATA / "data.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f" File 'data.json' is missing from data directory!")
    except json.JSONDecodeError:
        print(f" Trying to read data.....\n..... The 'data.json' file is corrupted!")
        print(f" Removing the previous file")
        
        os.remove(DATA / 'data.json')

    print(f"Creating a new 'data.json' file for index data")
    try:
        dir_list = os.listdir(DATA / "decks")
        dir_list = list(filter(lambda s: s.endswith('.json'), dir_list))
    except FileNotFoundError:
        print(f"No directory named 'decks' found at path : {DATA}, creating one")
        os.makedirs(DATA / "decks", exist_ok = True)
        dir_list = []

    # create an empty dictionary and then fill it by iterating over the valid listnames found in /decks
    data_dic = dict()
    for file in dir_list:
        with open(DATA / 'decks' / file, 'r') as deckn:
            data = json.load(deckn)
            data_dic[file] = {
                    "name": data["name"],
                    "deck_id"  : data["deck_id"],
                    "size": data["size"],
                    "filename": file
              }

    # if file is corrupt or not found, create a new file 
    with open(DATA / 'data.json', 'w') as data:
        json.dump(data_dic, data)

    return data_dic

def load_deck(filename):
    """This function loads the deck files data, pass the filename of the file"""
    try:
        # data = str(config.DATA)
        with open(DATA / "decks" / filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundEror:
        print(f'Cannot find the required deck file {filename}')
        return None
    except json.JSONDecodeError:
        print(f'{filename} file seems to be corrupted, program cannot read it! Delete the file and create a new deck')
        return None

def save_deck(deck_data):
    with open(temp_file, 'w') as file:
        json_data = json.dumps(deck_data)
        file.write(json_data)
        
