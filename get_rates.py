import json

FILE_NAME = "coords.json"


def get_swans_rates(file_name):
    with open(file_name, "r") as read_file:
        database = json.load(read_file)

        swans = dict()

        for detector in database["message"]:
            for swan in detector["swans"]:
                swan_id = swan["id"]
                swan_rate = swan["rate"]

                if swan_id not in swans.keys():
                    swans[swan_id] = []

                swans[swan_id].append(swan_rate)

        return swans


print(get_swans_rates(FILE_NAME))
