from flask import render_template, url_for, request, redirect, Blueprint, flash
from flask_login import login_user, current_user, logout_user, login_required
from my_asset_project import db
from my_asset_project.assets.forms import BulkUploadForm, AddNewAssetForm, AssetSearchForm
import pandas as pd
from my_asset_project.models import Asset_Details

add_new_asset = Blueprint('add_asset', __name__)
asset_upload = Blueprint('assets', __name__)
asset_search = Blueprint('search_asset', __name__)


#Bulk Upload
@asset_upload.route('/bulk_upload', methods=['POST', 'GET'])
def bulk_upload():
    form = BulkUploadForm()

    if request.method== 'POST':
        excel_file = form.excel_file.data
        #Perform Excel upload operations on DB
        if excel_file:
            df = pd.read_excel(excel_file)  # Use pandas to read Excel data
            for index, row in df.iterrows():
                data = Asset_Details(column1=row['Column1'], column2=row['Column2'])  # Adjust columns accordingly
                db.session.add(data)
            db.session.commit()




        next = request.args.get('next')

        if next == None or not next[0]=='/':
            next = url_for('core.index')

            return redirect(next)
    
    return render_template('bulk_upload.html', form=form)



#Add New Asset
@add_new_asset.route('/add_asset', methods=['POST', 'GET'])
def add_asset():
    form = AddNewAssetForm()

    if request.method == 'POST':
        new_asset = Asset_Details(asset_number= form.asset_number.data, product_category= form.product_category.data, 
                                  product_name = form.product_name.data, 
                                  model_version= form.model_version.data, manufacturer = form.manufacturer.data, other_brand= form.other_brand.data,
                                  asset_status = form.asset_status.data, user_name=form.user_name.data, employee_id= form.employee_id.data, location=form.location.data,
                                  other_location=form.other_location.data, email=form.email.data, contact=form.contact.data, company=form.company.data, 
                                  other_company=form.other_company.data, asset_category= form.asset_category.data, 
                                  oem_serial_number = form.oem_serial_number.data, system_host_name = form.system_host_name.data, 
                                  ip_address = form.ip_address.data, 
                                  oem_asset_warranty = form.oem_asset_warranty.data, oem_warranty_expiry_date = form.oem_warranty_expiry_date.data, 
                                  insurance_coverage= form.insurance_coverage.data, insurance_company= form.insurance_company.data,
                                  policy_number = form.policy_number.data, 
                                  insured_amount = form.insured_amount.data, start_date = form.start_date.data, 
                                  end_date= form.end_date.data, supplier_name = form.supplier_name.data, 
                                  supplier_contact = form.supplier_contact.data, supplier_location = form.supplier_location.data, 
                                  supplier_email = form.supplier_email.data, 
                                  incident_id = form.incident_id.data, remarks = form.remarks.data, payment_done= form.payment_done.data, 
                                  payment_date = form.payment_date.data, 
                                  voucher_number = form.voucher_number.data, disposal_date = form.disposal_date.data, disposal_amount = form.disposal_amount.data, device_type = form.device_type.data, 
                                  desk_lap_os = form.desk_lap_os.data, desk_lap_hdd_type = form.desk_lap_hdd_type.data, 
                                  desk_lap_hdd_size = form.desk_lap_hdd_size.data, desk_lap_ram_type = form.desk_lap_ram_type.data, desk_lap_ram_size = form.desk_lap_ram_size.data, 
                                  desk_lap_ram_frequency = form.desk_lap_ram_frequency.data, desk_lap_ram_expandable = form.desk_lap_ram_expandable.data, 
                                  desk_lap_ram_slots = form.desk_lap_ram_slots.data, desk_lap_hdmi_port = form.desk_lap_hdmi_port.data, 
                                  desk_lap_display_size = form.desk_lap_display_size.data, desk_lap_graphics_card_size = form.desk_lap_graphics_card_size.data, 
                                  desk_lap_graphics_card_version = form.desk_lap_graphics_card_version.data, printer_type = form.printer_type.data, printing_type= form.printing_type.data, 
                                  printer_toner= form.printer_toner.data, printer_connectivity= form.printer_connectivity.data, hdd_size= form.hdd_size.data, 
                                  hdd_type= form.hdd_type.data, connectivity= form.connectivity.data, tab_os= form.tab_os.data, tab_storage= form.tab_storage.data, 
                                  tab_ram_size= form.tab_ram_size.data, tab_display_size= form.tab_display_size.data, tab_stylus= form.tab_stylus.data, 
                                  tab_connectivity= form.tab_connectivity.data, display_size= form.display_size.data, hdmi_port= form.hdmi_port.data, 
                                  speaker= form.speaker.data, ups_capacity= form.ups_capacity.data, amc= form.amc.data, ups_start_date= form.ups_start_date.data, 
                                  ups_end_date= form.ups_end_date.data, source_of_purchase= form.source_of_purchase.data, contract_id= form.contract_id.data, 
                                  invoice_amount= form.invoice_amount.data, invoice_date= form.invoice_date.data, invoice_upload= form.invoice_upload.data)
        # db.drop_all()
        # db.create_all()
        db.session.add(new_asset)
        db.session.commit()

        next = request.args.get('next')

        if next == None or not next[0]=='/':
            next = url_for('core.index')

            return redirect(next)
    
    return render_template('add_asset.html', form=form)


# Search Asset
@asset_search.route('/', methods=['GET', 'POST'])
def search_assets():
    form = AssetSearchForm()

    if request.method == 'POST':
        # Get the form data
        asset_number = request.form.get('asset_number')
        oem_serial_number = request.form.get('oem_serial_number')
        asset_status = request.form.get('asset_status')
        employee_id = request.form.get('employee_id')
        product_category = request.form.get('product_category')

        # Build the query or fetch data from the database
        # Your code to fetch and filter data goes here
        query = Asset_Details.query
        if asset_number:
            query = query.filter(Asset_Details.asset_number == asset_number)
        if oem_serial_number:
            query = query.filter(Asset_Details.oem_serial_number == oem_serial_number)
        if asset_status:
            query = query.filter(Asset_Details.asset_status == asset_status)
        if employee_id:
            query = query.filter(Asset_Details.employee_id == employee_id)
        if product_category:
            query = query.filter(Asset_Details.product_category == product_category)

        results = query.all()

        return render_template('index.html', results=results, form=form)

    return render_template('index.html', form=form)
