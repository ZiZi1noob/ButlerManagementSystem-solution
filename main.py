from JSON_ import json_operation
from RANDOM_ import random_data_list
import glob


if __name__ == '__main__':
    input_name = input('***IMPORTANT Instruction***: \n1. This demo will randomly generate items for testing. \n2. This demo will check whether the input name exists or not automatically (under current folder) \n3. Generated data will be appended into an existing file, or created a new file. \nPlease input a file name for testing (Case sensitive!!!); e.g. "sample.json" or "new_file.json"\n')
    input_name = input_name.split('.')[0] + '.json'
    if input_name in glob.glob("*.json"):
        json_operation(input_name).update_json(data=random_data_list())
    else:
        generated_data = random_data_list()
        json_operation.create_new_json(generated_data, input_name)
    
