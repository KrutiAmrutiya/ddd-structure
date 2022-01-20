from rest_framework.decorators import api_view
from rest_framework.response import Response
from modules.common_utilities.di import obj_graph
from modules.accounts_module.business.user_module.services.user_service import UserService
from modules.accounts_module.business.user_module.dtos.user_dto import UserDto


@api_view(["GET", "POST"])
def register(request):
    """
    List all Task, or create a new Task.
    """
    if request.method == "GET":
        gettask = obj_graph.provide(UserService)
        res = gettask.get_list()
        return Response(res)

    elif request.method == "POST":
        create_tas = obj_graph.provide(UserService)
        dto = UserDto(
            username=request.data["username"], first_name=request.data["first_name"], last_name=request.data["last_name"],
            email=request.data["email"], password=request.data["password"], gender=request.data["gender"], phone_number=request.data["phone_number"],
            date_of_birth=request.data["date_of_birth"]
        )
        res = create_tas.create(dto)
        return Response(res)
