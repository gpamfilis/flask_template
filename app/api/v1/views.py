from flask import jsonify
from flask.views import MethodView
from . import mobile

class Test(MethodView):

    def get(self):
        return jsonify({"status":"OK"})

    def post(self):
        return jsonify({"status":"OK"})

    def put(self):
        return jsonify({"status":"OK"})

    def delete(self):
        return jsonify({"status":"OK"})

mobile.add_url_rule("/test", view_func=Test.as_view("test"), methods=['GET','POST','PUT','DELETE'])
