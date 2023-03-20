import json
import requests
from flask import Blueprint, Response
from utils.randgen import ProduceNum
from task_one import get_url


# Flask is a class we used to instantiate an application
taskone = Blueprint("taskone", __name__, url_prefix="/api")


@taskone.route("/taskone/<resource>/<int:count>/<int:start>/<int:end>")
def task_one(resource, count, start, end):
    obj = ProduceNum(start, end, count)

    resources_ids = [element for element in obj]
    print(f"[ INFO ] fetching data for following ids :{resources_ids}")

    content = []
    for resource_id in resources_ids:
        print(f"[ INFO ] fetching data for resource id number : {resource_id}")

        url = get_url(resource, resource_id)

        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            try:
                content.append(result["name"])
            except KeyError:
                content.append(result.get("title"))

    output = {"Count": len(content), "Names": content}

    return Response(json.dumps(output), status=200, mimetype="application/json")
