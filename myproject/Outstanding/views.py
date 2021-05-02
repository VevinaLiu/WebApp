from flask import Blueprint, render_template, url_for, redirect, session
from myproject.missinglines.forms import datefilter
from myproject.models import con_sql
from datetime import datetime

bp_otsd = Blueprint('outstanding',__name__,template_folder='templates/claim')


@bp_otsd.route('/', methods=['GET','POST'])
def claim():
    form = datefilter()

    sql1 = """
        SELECT *
        FROM DB2
        WHERE VAR1 > 0
            AND ....        
    """
    sql2 = """GROUP BY VAR5 ORDER BY 1"""
    global alist
    if form.validate_on_submit():
        conn = con_sql().consql
        cur = conn.cursor()
        session['sdate'] = datetime.strftime(form.sdate3.data,'%Y-%m-%d')
        qsdate = "'" + session['sdate'] + "'"
        session['edate'] = edate = datetime.strftime(form.edate.data,'%Y-%m-%d')
        qedate = "'" + session['edate'] + "'"

        joinsql = f"""AND VAR7 >= {qsdate} AND VAR7 <= {qedate}"""

        statement = sql1 + joinsql +sql2
        cur.execute(statement)
        alist = cur.fetchall()

        return redirect(url_for('claim_results', alist=alist))
    return render_template('claim.html', form=form)

@bp_otsd.route('/claim_results')
def claim_results():
    global allist
    return render_template('claim_results.html', alist=alist)