from rest_framework.decorators import api_view
from rest_framework.response import Response
from modules.task_module.business.task_module.services.task_service import TaskService
from modules.task_module.business.task_module.Dtos.task_dto import TaskDto
from modules.common_utilities.di import obj_graph


@api_view(["GET", "POST"])
def task_list(request):
    """
    List all Task, or create a new Task.
    """
    if request.method == "GET":
        gettask = obj_graph.provide(TaskService)
        res = gettask.get_list()
        return Response(res)

    elif request.method == "POST":
        create_tas = obj_graph.provide(TaskService)
        dto = TaskDto(
            title=request.data["title"], description=request.data["description"]
        )
        res = create_tas.create(dto)
        return Response(res)
