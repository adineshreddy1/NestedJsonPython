import json,os,sys


def retriveCountry(jsonFileName):
    '''This method reads values from json file
    and retunrs value '''
    
    jsonFile = open(os.path.join(sys.path[0],jsonFileName))

    jsonFileData = json.load(jsonFile)
    CountryName = jsonFileData['Data']["WorkAssignments"]["Items"][0]["Location"]["LegalEntity"]["Country"]["Name"]
    print("key",CountryName)
    jsonFile.close()
    return CountryName

print(retriveCountry("file/sample.json"))