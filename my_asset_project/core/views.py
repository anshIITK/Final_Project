from flask import render_template, request, Blueprint


core = Blueprint('core',__name__)

# Home Page
@core.route('/')
def index():
    return render_template('index.html')


