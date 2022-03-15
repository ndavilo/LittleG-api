import json
#the file should be in the same directory as this code
def ReadJson(filename):
    f = open(str(filename))
    data = json.load(f)
    return data

#print(ReadJson('problem.json'))
