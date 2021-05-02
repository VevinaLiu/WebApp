# Report Y

from flask import Blueprint, render_template, make_response
from datetime import datetime
from dateutil.relativedelta import relativedelta
from myproject.models import con_sql
from myproject.ReportY.forms import batches
import pandas as pd
import io


bp_y = Blueprint('reporty',__name__, template_folder='templates/reporty')


def collect_info(supp_dict, writer, conn, next_month, due_date, first_date):


    for name, code in supp_dict.items():
        scode = "'" + code + "'"
        statement = '''
        SELECT
            VAR1, VAR2 ... 
        	,CASE WHEN VAR10 < {0} OR VAR10 IS NULL
        		THEN VAR11
        		ELSE NULL
        		END AS AMOUNT
        	,CASE WHEN VAR10 > {1} 
        		THEN VAR11
        		ELSE NULL
        		END AS N_AMOUNT
          FROM DB1
          WHERE VAR1 LIKE {2}
          AND VAR2  < {3}
          AND ...
          ORDER BY VAR12
          ;

        '''.format(next_month, due_date, scode, first_date)

        results = pd.read_sql(statement, conn)
        results.to_excel(writer, sheet_name=name, index=False)



@bp_y.route('/', methods=['GET','POST'])
def reporty():
    form = batches()
    dmonth = (datetime.today().replace(day=1) - relativedelta(days=1)).strftime("%b%y")
    first_d = datetime.today().replace(day=1)
    first_date = "'" + datetime.strftime(first_d, '%Y-%m-%d') + "'"
    next_m = first_d + relativedelta(months=1)
    due_d = next_m - relativedelta(days=1)
    due_date = "'" + datetime.strftime(due_d, '%Y-%m-%d') + "'"
    next_month = "'" + datetime.strftime(next_m, '%Y-%m-%d') + "'"
    BATCH1 = {"a":"a1", "b":"b1" .........}
    BATCH2 = {"o":"o1", "p":"p1" .........}
    BATCH3 = {............................}
    BATCH4 = {............................}
    if form.validate_on_submit():
        conn = con_sql().consql
        bio = io.BytesIO()
        writer = pd.ExcelWriter(bio, engine='xlsxwriter')
        batchname ='Batch' + dmonth
        if form.batchno.data == 'BATCH1':
            collect_info(BATCH1, writer, conn, next_month, due_date, first_date)
            batchname = 'Batch1_' + dmonth
        if form.batchno.data == 'BATCH2':
            collect_info(BATCH2, writer, conn, next_month, due_date, first_date)
            batchname = 'Batch2_' + dmonth
        if form.batchno.data == 'BATCH3':
            collect_info(BATCH3, writer, conn, next_month, due_date, first_date)
            batchname = 'Batch3_' + dmonth
        if form.batchno.data == 'BATCH4':
            collect_info(BATCH4, writer, conn, next_month, due_date, first_date)
            batchname = 'Batch4_' + dmonth

        writer.save()
        bio.seek(0)
        rv = make_response(bio.getvalue())
        bio.close()

        rv.headers['Content-Type'] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        rv.headers["Cache-Control"] = "no-cache"
        rv.headers['Content-Disposition'] = 'attachment; filename={}.xlsx'.format('BATCH')
        return rv


    return render_template('batches.html', form=form, dmonth=dmonth)

