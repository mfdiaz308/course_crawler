import json
import os

folders = ['course_crawler/coursera','course_crawler/edx','course_crawler/udemy']
all_jsons_file = 'course_crawler/all.json'

def combine_json(folders, all_jsons_file):
    res = []
    for folder in folders:
        for root, _, files in os.walk(folder):
            for file in files:
                if file.endswith('.json'):
                    with open(os.path.join(root, file), 'r') as f:
                        try:
                            data = json.load(f)
                            res.extend(data)
                        except json.JSONDecodeError as e:
                            print(f'Error al leer el archivo {file}: {e}')
    
    with open(all_jsons_file, 'w') as outfile:
        json.dump(res, outfile, indent=4)

if __name__ == '__main__':
    combine_json(folders,all_jsons_file)
    print('Json files combined.')