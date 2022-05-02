"""OpenAPI v3 Specification"""

# apispec via OpenAPI
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields
import os
import pandas as pd

# Create an APISpec
spec = APISpec(
    title="Desafio de Lógica de Programação - Helder Prado",
    version="1.0.0",
    openapi_version="3.0.2",
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

# Define schemas
class InputSchema(Schema):
    number = fields.Int(description="An integer.", required=True)

class OutputSchema(Schema):
    msg = fields.String(description="A message.", required=True)

# register schemas with spec
spec.components.schema("Input", schema=InputSchema)
spec.components.schema("Output", schema=OutputSchema)


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    SQLITE_DB_DIR = None
    SQLALCHEMY_DATABASE_URI = None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRICE_FILE = None

# class LocalDevelopmentConfig(Config):
#     SQLITE_DB_DIR = os.path.join(basedir)
#     SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(SQLITE_DB_DIR, "toolcodes.sqlite3")
#     PRICE_FILE = pd.read_excel("./static/assets/tool_price.xlsx")
#     SUM = pd.read_excel(open('./static/assets/tool_price.xlsx', 'rb'), sheet_name='Sheet3')  

#     DEBUG = True

# add swagger tags that are used for endpoint annotation
tags = [
            {'name': 'Test Methods',
             'description': 'Methods for testing the API.'
            },
            {'name': 'Calculation Methods',
             'description': 'Methods for calculating data.'
            },
       ]

for tag in tags:
    print(f"Adding tag: {tag['name']}")
    spec.tag(tag)