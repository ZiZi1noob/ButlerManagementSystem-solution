import json
import glob

class json_operation:
    def __init__(self, path=None):
        if path != None:
            self.path = path
        
    def read_json(self, path=None):
        # return list
        if path == None:
            path = self.path
        file = open(path)
        json_data = json.load(file)
        return json_data

    def update_json(self, data, path=None):
        # a easy way is to overwirte raw file
        # appending data within raw file might be a better altenative
        # data could be list or dict
        if path == None:
            path = self.path
        raw_data = json_operation(path).read_json()
        if type(data) == list:
            for i in range(len(data)):
                raw_data.append(data[i])
        else:
            raw_data.append(data)
        with open(path, 'w') as outfile:
            json.dump(raw_data, outfile, indent=4)
            print('Update Data Successful')
            
    def create_new_json(data, path, notif=None):
        with open(path, 'w') as outfile:
            json.dump(data, outfile, indent=4)
            if notif == None:
                print('It"s saved as {} with {} items'.format(path, len(data)))
    
    def detect_incomplete_ticket(path=None):
        # supports a list or a single path
        # if path wasn't provided, currect folder will be detected
        if path == None:
            paths = glob.glob("*.json")
        else:
            if type(path) == list:
                # unfinished
                paths = []
                for i in path:
                    i = i.split('.')[0] + '.json'
                    paths.append(i)
            elif type(path) == str:
                path = path.split('.')[0] + '.json'
                paths = [path]
        for path_ in paths:
            temp_data = json_operation().read_json(path=path_)
            result_data = []
            for dic in temp_data:
                if 'createdAt' in list(dic.keys()) and 'tel' in list(dic.keys()):
                    result_data.append(dic)
            json_operation.create_new_json(result_data, path_, True)
            print("'file': {}, incomplete items detected: {}".format(path_, len(temp_data) - len(result_data)))
                        
                        

if __name__ == '__main__':
    inp = input('Detect incomplete ticket supports three modes: 1. check all json files under currect folder (press "ENTER") 2. input a specific name (e.g. "sample" or "sample.json") \nPlease input:')
    if inp == '':
        json_operation.detect_incomplete_ticket()
    else:
        json_operation.detect_incomplete_ticket(inp)
    

