"""Flask Application"""

from flask import Flask, jsonify as jsn
import sys

from src.endpoints.sum_value import sum_value

app = Flask(__name__)

app.register_blueprint(sum_value, url_prefix="/api/v1/sum_value")


from src.api_spec import spec

with app.test_request_context():
    for fn_name in app.view_functions:
        if fn_name == 'static':
            continue
        print(f"Loading swagger docs for function: {fn_name}")
        view_fn = app.view_functions[fn_name]
        spec.path(view=view_fn)

@app.errorhandler(403)
def resource_not_found(e):
    output = {"msg": f"403 - Forbidden."}
    return jsn(output), 403


@app.errorhandler(404)
def resource_not_found(e):
    output = {"msg": f"404 - The requested URL was not found on the server."}
    return jsn(output), 404

@app.errorhandler(405)
def resource_not_found(e):
    output = {"msg": f"405 - Method not allowed."}
    return jsn(output), 405

@app.errorhandler(500)
def resource_not_found(e):
    output = {"msg": f"500 - Internal server error."}
    return jsn(output), 500

@app.route("/api/swagger.json")
def create_swagger_spec():
    return jsn(spec.to_dict())

from src.endpoints.swagger import swagger_ui_blueprint, SWAGGER_URL
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)