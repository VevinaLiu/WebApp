

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

###############################
##### register blueprint ######
###############################

from myproject.ReportX.views import bp_x
from myproject.Outstanding.views import bp_otsd
from myproject.ReportY.views import bp_y
from myproject.ProcessR.views import bp_processr

app.register_blueprint(bp_x, url_prefix='/reportx')
app.register_blueprint(bp_otsd, url_prefix='/outstanding')
app.register_blueprint(bp_y, url_prefix='/reporty')
app.register_blueprint(bp_processr, url_prefix='/processr')
