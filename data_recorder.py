import csv
import os

file_path = "game_data.csv"
def save_data(state, action):
    file_exists = os.path.isfile(file_path)
    with open(file_path,mode= 'a',newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['head_x','head_y','food_x','food_y','direction','action'])
        writer.writerow([state["head_x"], state["head_y"], state["food_x"], state["food_y"], state["direction"], action])