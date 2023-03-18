from flask import Blueprint
from utils.fetch_data import hit_url
from task_two import first_task


tasktwo = Blueprint("tasktwo", __name__, url_prefix="/api")


@tasktwo.route("/tasktwo/<resource>")
def task_three(resource):
    data_ = first_task()
    response_data = data_.get(resource)
    resources = [element for element in response_data]

    names = []
    for resource in resources:
        resource_data = hit_url(resource)
        resource_data = resource_data.json()
        names.append(resource_data.get("name"))

    return names
