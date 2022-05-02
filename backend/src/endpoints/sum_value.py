from distutils.log import debug
from flask import Blueprint, jsonify as jsn, request as r
from pandas import ExcelFile
import pathlib as pl
from datetime import date, datetime as dt

sum_value = Blueprint(name="sum_value", import_name=__name__)

path = pl.Path(__file__).parent.resolve()

def excel2dict(xls):
    df = xls.parse(xls.sheet_names[0])
    xls_dict = df.to_dict()
    return xls_dict



def get_file_content(file):
    xls = ExcelFile(file)
    dict = excel2dict(xls)
    return dict

def sum_items(start_date, end_date):
    start_date = dt.strptime(start_date, "%Y-%m-%d")
    end_date = dt.strptime(end_date, "%Y-%m-%d")
    content = get_file_content('%s/../static/assets/excel/ipca 2.xlsx'%(path))
    
    sum_items = 0
    keys = content["valor"].keys()
    for idx in keys:
        dt_item = content["data"][idx]
        sum_items += content["valor"][idx] if (start_date <= dt_item <= end_date) else 0
    return sum_items

@sum_value.route('/last_12_months', methods=['GET'])
def last_12_months():
    current_date = date.today()
    start_date = current_date.replace(year=current_date.year - 1)
    start_date = start_date.strftime('%Y-%m-%d')
    end_date = current_date.strftime('%Y-%m-%d')
    content = sum_items(start_date, end_date)
    ret = {
        "total": round(content, 2)
    }
    return jsn(ret)


@sum_value.route('/period', defaults={'start_date':None,'end_date':None}, methods=['GET'])
@sum_value.route('/period/<string:start_date>', defaults={'end_date':None}, methods=['GET'])
@sum_value.route('/period/<string:start_date>/<string:end_date>', methods=['GET'])
def period(start_date, end_date):
    end_date = end_date if end_date is not None else date.today().strftime('%Y-%m-%d')
    content = sum_items(start_date, end_date)
    ret = {
        "total": round(content, 2)
    }
    return jsn(ret)


@sum_value.errorhandler(404)
def resource_not_found(e):
    output = {"msg": f"404 - The requested URL was not found on the server."}
    return jsn(output), 404

@sum_value.errorhandler(405)
def resource_not_found(e):
    output = {"msg": f"405 - This method is not allowed."}
    return jsn(output), 405

@sum_value.errorhandler(500)
def resource_not_found(e):
    output = {"msg": f"500 - Internal server error."}
    return jsn(output), 500