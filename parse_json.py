import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
django.setup()

from renderer.models import DetectAnomaly, Detector, Anomaly

FILE_NAME = "coords.json"
with open(FILE_NAME, "r") as read_file:
    database = json.load(read_file)

for detector in database["message"]:
    coords = detector["coords"]
    detector_id = detector["id"]
    detector1 = Detector.objects.get_or_create(
        id=detector_id,
        x_coord=coords[0],
        y_coord=coords[1]
    )
    print(detector1[0])

    for swan in detector["swans"]:
        swan_id = swan["id"]
        swan_rate = swan["rate"]
        anomaly = Anomaly.objects.get_or_create(
            id=swan_id
        )
        print(anomaly[0])
        detect_anomaly = DetectAnomaly.objects.get_or_create(
            detector_id=detector1[0],
            anomaly_id=anomaly[0],
            rate=swan_rate
        )
        print("Swan id:", swan_id, "rate:", swan_rate)


