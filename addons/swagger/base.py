import json


class Swagger(object):
    swagger = "2.0"

    def to_json(self):
        return json.dumps({
            "swagger": self.swagger
        })

