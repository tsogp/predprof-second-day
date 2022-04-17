import json


FILE_NAME = "coords.json"
with open(FILE_NAME, "r") as read_file:
    database = json.load(read_file)

for detector in database["message"]:
    coords = detector["coords"]
    detector_id = detector["id"]
    print("Detector id", detector_id)
    print("Coords:", coords)

    for swan in detector["swans"]:
        swan_id = swan["id"]
        swan_rate = swan["rate"]
        print("Swan id:", swan_id, "rate:", swan_rate)


