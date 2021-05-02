from flask import Blueprint, render_template, request, make_response, flash

from myproject.ProcessR.forms import dltemp
import pandas as pd
import io

bp_processr = Blueprint('reb_process', __name__, template_folder='templates/reb_process')


@bp_processr.route('/', methods=['GET','POST'])
def processr():
    form = dltemp()
    if form.validate_on_submit():
        if form.submit1.data:
            bio = io.BytesIO()
            writer = pd.ExcelWriter(bio, engine='xlsxwriter')
            df1 = pd.DataFrame(columns=['NAME','NET_AMOUNT','DATE','CODE','REF1','REF2','DESCRIPTION1','DESCRIPTION2','DESCRIPTION3'])
            df2 = pd.DataFrame(columns=['Instructions'])
            df2.loc[0] = "Instruction 1"
            df2.loc[1] = "Instruction 2"
            df2.loc[2] = "Instruction 3"
            df1.to_excel(writer, sheet_name='template', index=False)
            df2.to_excel(writer, sheet_name='instructions', index=False)
            writer.save()

            bio.seek(0)
            rv = make_response(bio.getvalue())
            bio.close()

            rv.headers['Content-Type'] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            rv.headers["Cache-Control"] = "no-cache"
            rv.headers['Content-Disposition'] = 'attachment; filename={}.xlsx'.format('process_template')

            return rv
        if form.submit2.data:
            f = request.files['file']
            if not f:
                flash('Please upload the file to process')
            elif f.filename[-5:] != '.xlsx':
                flash('Please upload .xlsx file')
            else:
                stream = io.BytesIO(f.stream.read())
                df3 = pd.read_excel(stream)

    return render_template('processr.html', form=form)