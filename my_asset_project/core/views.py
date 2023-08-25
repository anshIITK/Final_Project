from flask import render_template, request, Blueprint
from my_asset_project.assets.forms import AssetSearchForm


core = Blueprint('core',__name__)

# Home Page
@core.route('/')
def index():
    form = AssetSearchForm()
    return render_template('index.html', form = form)


