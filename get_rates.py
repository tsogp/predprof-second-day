import json

FILE_NAME = "coords.json"


def get_swans_true_false(file_name):
    with open(file_name, "r") as read_file:
        database = json.load(read_file)

        swans = dict()

        for detector in database["message"]:
            """
            for swan in detector["swans"]:
                swan_id = swan["id"]
                swan_rate = swan["rate"]

                if swan_id not in swans.keys():
                    swans[swan_id] = []

                swans[swan_id].append(swan_rate)
            """
            detector_swans_ids = []

            for swan in detector["swans"]:
                swan_id = swan["id"]
                swan_rate = swan["rate"]

                detector_swans_ids.append(swan_id)

                if swan_id not in swans.keys():
                    swans[swan_id] = []
                swans[swan_id].append(True)

            for s in swans.keys():
                if s not in detector_swans_ids:
                    swans[s].append(False)
        return swans

def get_swans_rates(file_name):
    with open(file_name, "r") as read_file:
        database = json.load(read_file)

        swans = dict()

        for detector in database["message"]:
            detector_swans_ids = []

            for swan in detector["swans"]:
                swan_id = swan["id"]
                swan_rate = swan["rate"]

                detector_swans_ids.append(swan_id)

                if swan_id not in swans.keys():
                    swans[swan_id] = []
                swans[swan_id].append(swan_rate)

            for s in swans.keys():
                if s not in detector_swans_ids:
                    swans[s].append(0.0)
        return swans

print(get_swans_true_false(FILE_NAME))

print(get_swans_rates(FILE_NAME))
