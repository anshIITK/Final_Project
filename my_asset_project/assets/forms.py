from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField, IntegerField, SelectField, DateField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Email


class BulkUploadForm(FlaskForm):
    excel_file = FileField('Upload Excel File', validators=[DataRequired()])
    submit = SubmitField('Upload')


class AddNewAssetForm(FlaskForm):
    asset_number = StringField('asset_number', validators=[DataRequired()])
    product_category = SelectField("Product Category", choices=[
        ("", "Select an option"),
        ("Desktop", "Desktop"),
        ("Laptop", "Laptop"),
        ("Monitor", "Monitor"),
        ("Server", "Server"),
        ("UPS", "UPS"),
        ("Storage", "Storage"),
        ("Tablet", "Tablet"),
        ("Mobile", "Mobile"),
    ])
    system_host_name = StringField("System Host Name")
    product_name = StringField('product_name', validators=[DataRequired()])
    model_version = StringField('model_version', validators=[DataRequired()])
    manufacturer = SelectField("Manufacturer", choices=[
        ("", "Select a manufacturer"),
        ("DELL", "DELL"),
        ("LENOVO", "LENOVO"),
        ("HP", "HP"),
        ("SAMSUNG", "SAMSUNG"),
        ("TOSHIBA", "TOSHIBA"),
        ("ASUS", "ASUS"),
        ("ACER", "ACER"),
        ("APPLE", "APPLE"),
        ("XIAOMI", "XIAOMI"),
        ("ONEPLUS", "ONEPLUS"),
        ("SEAGATE", "SEAGATE"),
        ("WD", "WD"),
        ("LG", "LG"),
        ("IBM", "IBM"),
        ("PANASONIC", "PANASONIC"),
        ("NOKIA", "NOKIA"),
        ("PHILLIPS", "PHILLIPS"),
        ("EPSON", "EPSON"),
        ("BENQ", "BENQ"),
        ("EWITT", "EWITT"),
        ("GOOGLE", "GOOGLE"),
        ("INTEL", "INTEL"),
        ("HCL", "HCL"),
        ("VAIO", "VAIO"),
        ("AVITA", "AVITA"),
        ("MSI", "MSI"),
        ("HITACHI", "HITACHI"),
        ("SONY", "SONY"),
        ("ZEBRONICS", "ZEBRONICS"),
        ("IBALL", "IBALL"),
        ("AOC", "AOC"),
        ("Others", "Others"),
    ])
    other_brand = StringField("other_brand")
    asset_status = SelectField("Asset Status", choices=[
        ("", "Select an option"),
        ("In Stock", "In Stock"),
        ("Assigned", "Assigned")
    ])
    user_name = StringField("user_name")
    employee_id = StringField('employee_id', validators=[DataRequired()])
    location = SelectField("location", choices=[
        ("", "Select an location"),
        ("Residence", "Residence"),
        ("Ministry", "Ministry"),
        ("office", "office"),
        ("others", "others")
    ])
    other_location = StringField("other_location")
    email = StringField("email", validators=[Email()])
    contact = StringField("contact", validators=[InputRequired()])
    company = SelectField("company", choices=[
        ("", "Select a Company"),
        ("AIC", "AIC"),
        ("WIPRO", "WIPRO"),
        ("BHARAT IT", "BHARAT IT"),
        ("INTELLECT", "INTELLECT"),
        ("PROGILITY", "PROGILITY"),
        ("OTHERS", "OTHERS")
    ])
    other_company = StringField("other_company")
    asset_category = SelectField("Asset Category", choices=[
        ("", "Select asset category"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ])
    oem_serial_number = StringField('oem_serial_number', validators=[DataRequired()])
    ip_address = StringField('ip_address')
    oem_asset_warranty = SelectField("OEM asset Warranty(months)", choices=[
        ("", "Select a number"),
        *[(str(month), f"{month} months") for month in range(0, 61)],
    ])
    oem_warranty_expiry_date = DateField("OEM Warranty Expiry date")
    insurance_coverage = SelectField("Insurance Coverage", choices=[
        ("", "Select coverage"),
        ("Yes", "Yes"),
        ("No", "No"),
    ])
    insurance_company = SelectField("Insurance Company:", choices=[("", "Select company"), ("UIIC", "UIIC"), ("NICIL", "NICIL"), ("NIACL", "NIACL"), ("OICL", "OICL")], validators=[InputRequired()])
    policy_number = StringField("Policy Number", render_kw={"disabled": "true"})
    start_date = DateField("Start Date", render_kw={"disabled": "true"})
    end_date = DateField("End Date", render_kw={"disabled": "true"})
    insured_amount = StringField("Insured Amount", render_kw={"disabled": "true"})
    source_of_purchase = StringField("Source Of Purchase")
    contract_id = StringField("Contract ID")
    invoice_amount = StringField("Invoice Amount", validators=[DataRequired()])
    invoice_date = DateField("Invoice Date", validators=[InputRequired()])
    invoice_upload = StringField('invoice_upload')
    supplier_name = StringField("Supplier Name:", validators=[InputRequired()])
    supplier_contact = StringField("Supplier Contact:", validators=[InputRequired()])
    supplier_email = StringField("Supplier Email:", validators=[Email()])
    supplier_location = SelectField("Supplier Location Delhi (Yes/No):", choices=[("", "Select location status"), ("Yes", "Yes"), ("No", "No")])
    incident_id = StringField("Incident ID:")
    remarks = TextAreaField("Remarks:")
    payment_done = SelectField("Payment Done (Yes/No):", choices=[("", "Select payment status"), ("Yes", "Yes"), ("No", "No")])
    payment_date = StringField("Payment Date", render_kw={"class": "form-control payment-field", "disabled": "disabled"})
    voucher_number = StringField("FMS Invoice Number", render_kw={"class": "form-control payment-field", "disabled": "disabled"})
    disposal_date = StringField('disposal_date')
    disposal_amount = IntegerField('disposal_amount')
    device_type = SelectField("Device Type", choices=[
        ("", "Select a device type"),
        ("laptopDesktop", "Laptop/Desktop"),
        ("printer", "Printer"),
        ("HDD Specs", "HDD Specs"),
        ("tabletMobile", "Tablet/Mobile"),
        ("monitor", "Monitor"),
        ("ups", "UPS")
    ], validators=[InputRequired()])
    # Desktop/Laptop
    desk_lap_os = StringField("desk_lap_os")
    desk_lap_hdd_type = SelectField("desk_lap_hdd_type", choices=[("", "Select HDD type"), ("SATA", "SATA"), ("SSD", "SSD"), ("SAS", "SAS"), ("Others", "Others")])
    desk_lap_hdd_size = SelectField("desk_lap_hdd_size", choices=[("", "Select HDD size"), ("128", "128"), ("256", "256"), ("512", "512"), ("1024", "1024"), ("2048", "2048"), ("4096", "4096"), ("Others", "Others")])
    desk_lap_ram_type = SelectField("desk_lap_ram_type", choices=[("", "Select RAM type"), ("DDR", "DDR"), ("DDR2", "DDR2"), ("DDR3", "DDR3"), ("DDR4", "DDR4"), ("Others", "Others")])
    desk_lap_ram_size = SelectField("desk_lap_ram_size", choices=[("", "Select RAM size"), ("0", "0 GB"), ("2", "2 GB"), ("4", "4 GB"), ("8", "8 GB"), ("16", "16 GB"), ("32", "32 GB"), ("64", "64 GB"), ("128", "128 GB"), ("Others", "Others")])
    desk_lap_ram_frequency = SelectField("desk_lap_ram_frequency", choices=[("", "Select RAM frequency"), ("3000", "3000 MHz"), ("3200", "3200 MHz"), ("3600", "3600 MHz"), ("4000", "4000 MHz"), ("4200", "4200 MHz"), ("4400", "4400 MHz"), ("2933", "2933 MHz"), ("2666", "2666 MHz"), ("2133", "2133 MHz"), ("1600", "1600 MHz"), ("1333", "1333 MHz"), ("1066", "1066 MHz"), ("800", "800 MHz"), ("1000", "1000 MHz"), ("667", "667 MHz"), ("533", "533 MHz"), ("400", "400 MHz"), ("200", "200 MHz"), ("266", "266 MHz"), ("300", "300 MHz"), ("333", "333 MHz"), ("Others", "Others")])
    desk_lap_ram_expandable = SelectField("desk_lap_ram_expandable", choices=[("", "RAM Expandable Upto"), ("0", "0 GB"), ("2", "2 GB"), ("4", "4 GB"), ("8", "8 GB"), ("16", "16 GB"), ("32", "32 GB"), ("64", "64 GB"), ("128", "128 GB"), ("Others", "Others")])
    desk_lap_ram_slots = SelectField("desk_lap_ram_slots", choices=[("", "Select RAM size"), ("0", "0 GB"), ("1", "1 GB"), ("2", "2 GB"), ("3", "3 GB"), ("4", "4 GB"), ("5", "5 GB"), ("Others", "Others")])
    desk_lap_hdmi_port = SelectField("desk_lap_hdmi_port", choices=[("Yes", "Yes"), ("No", "No")])
    desk_lap_display_size = IntegerField("desk_lap_display_size")
    desk_lap_graphics_card_size = SelectField("desk_lap_graphics_card_size", choices=[("", "Select Graphic card size"), ("0", "0 GB"), ("2", "2 GB"), ("4", "4 GB"), ("8", "8 GB"), ("16", "16 GB"), ("32", "32 GB"), ("64", "64 GB"), ("128", "128 GB"), ("Others", "Others")])
    desk_lap_graphics_card_version = SelectField("desk_lap_graphics_card_version", choices=[("", "Graphic Card Version"), ("Nvidia GeForce", "NVidia GeForce"), ("Intel Iris Xe", "Intel Iris Xe"), ("AMD Raedon", "AMD Raedon"), ("Others", "Others")])
    # Printer
    printer_type = StringField("printer_type")
    printing_type = SelectField("printing_type", choices=[("", "printer type"), ("color", "color"), ("Mono", "Mono"), ("Others", "Others")])
    printer_connectivity = SelectField("printer_connectivity", choices=[("", "Connectivity"), ("Wifi", "Wifi"), ("Ethernet", "Ethernet"), ("Both", "Both")])
    printer_toner = StringField("printer_toner")
    # HDD
    hdd_size = IntegerField("hdd_size")
    hdd_type = StringField("hdd_type")
    connectivity = SelectField("connectivity", choices=[("", "Connectivity"), ("USB", "USB"), ("Type C", "Type C"), ("Both", "Both")])
    # Tablet
    tab_os = StringField("tab_os")
    tab_storage = IntegerField("tab_storage")
    tab_ram_size = IntegerField("tab_ram_size")
    tab_display_size = IntegerField("tab_display_size")
    tab_stylus = SelectField("tab_stylus", choices=[("Yes", "Yes"), ("No", "No")])
    tab_connectivity = SelectField("tab_connectivity:", choices=[("", "Connectivity"), ("Wifi", "Wifi"), ("SIM", "SIM"), ("Both", "Both")])
    # Monitor
    display_size = IntegerField("display_size")
    hdmi_port = SelectField("hdmi_port", choices=[("Yes", "Yes"), ("No", "No")])
    speaker = SelectField("speaker", choices=[("Yes", "Yes"), ("No", "No")])
    # UPS
    ups_capacity = IntegerField("ups_capacity")
    amc = SelectField("amc", choices=[("Yes", "Yes"), ("No", "No")])
    ups_start_date = DateField("ups_start_date")
    ups_end_date = DateField("ups_end_date")

    submit = SubmitField("Submit Asset")




class AssetSearchForm(FlaskForm):
    asset_number = StringField('Asset number')
    oem_serial_number = StringField('OEM Serial number')
    asset_status = SelectField('Asset Status', choices=[
        ('', 'Select an option'),
        ('In Stock', 'In Stock'),
        ('Assigned', 'Assigned'),
        ('Not working', 'Not Working'),
        ('Retained', 'Retained'),
        ('End Of Life', 'End Of Life'),
        ('Transferred', 'Transferred'),
        ('Disposed', 'Disposed')
    ])
    employee_id = StringField('User Employee ID')
    product_category = SelectField('Product Category', choices=[
        ('', 'Select an option'),
        ('Desktop', 'Desktop'),
        ('Laptop', 'Laptop'),
        ('Monitor', 'Monitor'),
        ('Server', 'Server'),
        ('UPS', 'UPS'),
        ('Storage', 'Storage'),
        ('Tablet', 'Tablet'),
        ('Mobile', 'Mobile')
    ])
    submit = SubmitField('Search')