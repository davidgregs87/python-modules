''' script that adds all arguments to a Python list, and then save them to a file
'''
import json
import sys

save_to_json_file = __import__('Input_Output').save_to_json_file
load_from_json_file = __import__('Input_Output').load_from_json_file

try:
        items = load_from_json_file("add_item.json") #deserialize from json to python object
except FileNotFoundError: #if file is not found return an empty list
        items = []
        items.extend(sys.argv[1:])# Iterate through the command line arguments and append to 
        #item variable(list)  
        save_to_json_file(items, "add_item.json") # saves the item variable in a file "add_item.json"
        # if the file does not exist it create a new file with the filename "add_item.json"