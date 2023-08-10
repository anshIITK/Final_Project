from my_asset_project import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"
    

class Asset_Users(db.model):
    __tablename__ = 'asset_users'

    user_employee_id = db.Column(db.String(30), primary_key = True)
    username = db.Column(db.String(20))
    user_email = db.Column(db.String(30))
    user_contact_number = db.Column(db.Integer(20))
    company = db.Column(db.String(40))
    location = db.Column(db.String(50))

    assets = db.relationship('Asset_Details',backref='assigned_user', lazy=True)

    def __init__(self, emp_id, username, email, contact_number, company, location):
        self.user_employee_id = emp_id
        self.username = username
        self.user_email = email
        self.user_contact_number = contact_number
        self.company = company
        self.location = location

class Asset_Details(db.Model):

    __tablename__ = 'asset_details'
    asset_users = db.relationship(Asset_Users)

    
    id = db.Column(db.Integer, primary_key= True)
    user_emp_id = db.Column(db.String, db.ForeignKey('asset_users.user_employee_id'))
    asset_number = db.Column(db.String(20))
    product_category = db.Column(db.String(20))
    product_name = db.Column(db.String(20))
    model_version = db.Column(db.String(20))
    manufacturer = db.Column(db.String(20))
    asset_status = db.Column(db.String(20))
    asset_category =db.Column(db.String(20))
    oem_serial_number = db.Column(db.String(20))
    system_host_name = db.Column(db.String(30))
    ip_address = db.Column(db.String(20))
    oem_asset_warranty = db.Column(db.String(20))
    oem_warranty_expiry_date = db.Column(db.String(20))
    insurance_coverage = db.Column(db.String(20))
    insurance_company = db.Column(db.String(20))
    policy_number = db.Column(db.String(20))
    insured_amount = db.Column(db.Integer(20))
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    supplier_name = db.Column(db.String(20))
    supplier_contact = db.Column(db.String(20))
    supplier_location = db.Column(db.String(20))
    supplier_email = db.Column(db.String(20))
    incident_id = db.Column(db.String(20))
    remarks = db.Column(db.String(50))
    payment_done = db.Column(db.String(20))
    payment_date = db.Column(db.String(20))
    voucher_number = db.Column(db.String(20))
    disposal_date = db.Column(db.String(20))
    disposal_amount = db.Column(db.Integer(20))
    transfer_date = db.Column(db.String(20))
    transfer_amount = db.Column(db.Integer(20))
    transferred_from = db.Column(db.String(20))
    transfer_to = db.Column(db.String(20))
    desk_lap_operating_system = db.Column(db.String(20))
    desk_lap_hdd_type = db.Column(db.String(20))
    desk_lap_hdd_size = db.Column(db.Integer(20))
    desk_lap_ram_type = db.Column(db.String(20))
    desk_lap_ram_size = db.Column(db.Integer(20))
    desk_lap_ram_frequency = db.Column(db.Integer(20))
    desk_lap_ram_expandable_upto = db.Column(db.Integer(20))
    desk_lap_no_of_ram_slots =  db.Column(db.Integer(20))
    desk_lap_hdmi_port = db.Column(db.String(20))
    desk_lap_display_size = db.Column(db.Integer(20))
    desk_lap_graphics_card_size = db.Column(db.Integer(20))
    desk_lap_graphics_card_version = db.Column(db.String(20))
    printer_type = db.Column(db.String(20))
    printing_type = db.Column(db.String(20))
    printer_toner_name = db.Column(db.String(20))
    printer_connectivity = db.Column(db.String(20))
    hdd_size = db.Column(db.Integer(20))
    hdd_type = db.Column(db.String(20))
    hdd_connectivity = db.Column(db.String(20))
    tab_os = db.Column(db.String(20))
    tab_storage =  db.Column(db.Integer(20))
    tab_ram_size =  db.Column(db.Integer(20))
    tab_display_size = db.Column(db.Integer(20))
    tab_stylus = db.Column(db.String(20))
    tab_connectivity = db.Column(db.String(20))
    monitor_display_size = db.Column(db.Integer(20))
    monitor_hdmi_port = db.Column(db.String(20))
    monitor_speaker = db.Column(db.String(20))
    ups_capacity = db.Column(db.String(20))
    ups_amc = db.Column(db.String(20))
    ups_start_date = db.Column(db.String(20))
    ups_end_date =db.Column(db.String(20))
    source_of_purchase = db.Column(db.String(20))
    contract_id = db.Column(db.String(20))
    invoice_amount = db.Column(db.Integer(20))
    invoice_date = db.Column(db.String(20))
    invoice_upload = db.Column(db.String(140))



    def __init__(self, asset_number, product_category, product_name, model_version, manufacturer,
                asset_status, asset_category, oem_serial_number, system_host_name, ip_address,
                oem_asset_warranty, oem_warranty_expiry_date, insurance_coverage, insurance_company,
                policy_number, insured_amount, start_date, end_date, supplier_name, supplier_contact,
                supplier_location, supplier_email, incident_id, remarks, payment_done, payment_date,
                voucher_number, disposal_date, disposal_amount, transfer_date, transfer_amount,
                transferred_from, transfer_to, desk_lap_operating_system, desk_lap_hdd_type,
                desk_lap_hdd_size, desk_lap_ram_type, desk_lap_ram_size, desk_lap_ram_frequency,
                desk_lap_ram_expandable_upto, desk_lap_no_of_ram_slots, desk_lap_hdmi_port,
                desk_lap_display_size, desk_lap_graphics_card_size, desk_lap_graphics_card_version,
                printer_type, printing_type, printer_toner_name, printer_connectivity, hdd_size,
                hdd_type, hdd_connectivity, tab_os, tab_storage, tab_ram_size, tab_display_size,
                tab_stylus, tab_connectivity, monitor_display_size, monitor_hdmi_port, monitor_speaker,
                ups_capacity, ups_amc, ups_start_date, ups_end_date, source_of_purchase, contract_id,
                invoice_amount, invoice_date, invoice_upload):
        
        self.asset_number = asset_number
        self.product_category = product_category
        self.product_name = product_name
        self.model_version = model_version
        self.manufacturer = manufacturer
        self.asset_status = asset_status
        self.asset_category = asset_category
        self.oem_serial_number = oem_serial_number
        self.system_host_name = system_host_name
        self.ip_address = ip_address
        self.oem_asset_warranty = oem_asset_warranty
        self.oem_warranty_expiry_date = oem_warranty_expiry_date
        self.insurance_coverage = insurance_coverage
        self.insurance_company = insurance_company
        self.policy_number = policy_number
        self.insured_amount = insured_amount
        self.start_date = start_date
        self.end_date = end_date
        self.supplier_name = supplier_name
        self.supplier_contact = supplier_contact
        self.supplier_location = supplier_location
        self.supplier_email = supplier_email
        self.incident_id = incident_id
        self.remarks = remarks
        self.payment_done = payment_done
        self.payment_date = payment_date
        self.voucher_number = voucher_number
        self.disposal_date = disposal_date
        self.disposal_amount = disposal_amount
        self.transfer_date = transfer_date
        self.transfer_amount = transfer_amount
        self.transferred_from = transferred_from
        self.transfer_to = transfer_to
        self.desk_lap_operating_system = desk_lap_operating_system
        self.desk_lap_hdd_type = desk_lap_hdd_type
        self.desk_lap_hdd_size = desk_lap_hdd_size
        self.desk_lap_ram_type = desk_lap_ram_type
        self.desk_lap_ram_size = desk_lap_ram_size
        self.desk_lap_ram_frequency = desk_lap_ram_frequency
        self.desk_lap_ram_expandable_upto = desk_lap_ram_expandable_upto
        self.desk_lap_no_of_ram_slots = desk_lap_no_of_ram_slots
        self.desk_lap_hdmi_port = desk_lap_hdmi_port
        self.desk_lap_display_size = desk_lap_display_size
        self.desk_lap_graphics_card_size = desk_lap_graphics_card_size
        self.desk_lap_graphics_card_version = desk_lap_graphics_card_version
        self.printer_type = printer_type
        self.printing_type = printing_type
        self.printer_toner_name = printer_toner_name
        self.printer_connectivity = printer_connectivity
        self.hdd_size = hdd_size
        self.hdd_type = hdd_type
        self.hdd_connectivity = hdd_connectivity
        self.tab_os = tab_os
        self.tab_storage = tab_storage
        self.tab_ram_size = tab_ram_size
        self.tab_display_size = tab_display_size
        self.tab_stylus = tab_stylus
        self.tab_connectivity = tab_connectivity
        self.monitor_display_size = monitor_display_size
        self.monitor_hdmi_port = monitor_hdmi_port
        self.monitor_speaker = monitor_speaker
        self.ups_capacity = ups_capacity
        self.ups_amc = ups_amc
        self.ups_start_date = ups_start_date
        self.ups_end_date = ups_end_date
        self.source_of_purchase = source_of_purchase
        self.contract_id = contract_id
        self.invoice_amount = invoice_amount
        self.invoice_date = invoice_date
        self.invoice_upload = invoice_upload






