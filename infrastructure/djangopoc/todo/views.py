from rest_framework.decorators import api_view
from rest_framework.response import Response
from modules.common_utilities.di import obj_graph
from modules.todo_module.business.todo_module.services.todo_service import TodoService
from modules.todo_module.business.todo_module.dtos.todo_dto import TodoDto


@api_view(["GET", "POST"])
def todo_list(request):
    """
    List all Task, or create a new Task.
    """
    if request.method == "GET":
        gettask = obj_graph.provide(TodoService)
        res = gettask.get_list()
        return Response(res)

    elif request.method == "POST":
        create_tas = obj_graph.provide(TodoService)
        dto = TodoDto(
            title=request.data["title"], description=request.data["description"]
        )
        res = create_tas.create(dto)
        return Response(res)
