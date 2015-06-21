import json

from openerp import http


class SwaggerSite(http.Controller):

    @http.route("/swagger/swagger.json", auth="public")
    def index(self, **kw):
        status = 200
        headers = {}
        response = None

        return self.response(response, status, headers)

    def response(self, response, status, headers):
        http_headers = {
        }
        http_headers.update(headers)
        return http.Response(
            json.dumps(response),
            content_type="application/json",
            status=status,
            headers=http_headers
        )
