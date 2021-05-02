# Report x

from flask import Blueprint, render_template, url_for, redirect, session
from myproject.models import con_sql


bp_x = Blueprint('reportx', __name__,
                   template_folder='templates/reportx')


@bp_x.route('/', methods=['GET','POST'])
def reportx():
    conn = con_sql().consql
    cur = conn.cursor()
    statement = """SELECT * FROM DB3"""
    cur.execute(statement)
    xlist = cur.fetchall()
    return render_template('ReportX.html', xlist=xlist)




