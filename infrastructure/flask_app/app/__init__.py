from flask import Flask, jsonify, Response, request
from modules.todo_module.business.todo_module.dtos.todo_dto import TodoDto
from flask_restful import Api, Resource
from modules.todo_module.business.todo_module.services.todo_service import TodoService
from modules.common_utilities.di import obj_graph
from typing import List

app = Flask(__name__)

api = Api(app)


class TodosResource(Resource):
    """[summary]

    Args:
        Resource ([type]): [description]
    """

    def get(self) -> List[dict]:
        """[summary]

        Returns:
            List[dict]: [description]
        """
        ser = obj_graph.provide(TodoService)
        rs = ser.get_list()
        data = [dict(id=i.id, title=i.title, description=i.description) for i in rs]
        return data

    def post(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        ser = obj_graph.provide(TodoService)
        data = TodoDto(title=request.form["title"], description=request.form["title"])
        rs = ser.create(data)
        return Response(rs)


api.add_resource(TodosResource, "/")

if __name__ == "__main__":
    app.run(debug=True)
