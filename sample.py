import tkinter as tk
from tkinter import *


#connection = sqlite3.connect("Vehicle Management System.db")
#connection.execute("PRAGMA unlock_not_used")


def show_frame(frame):
    frame.tkraise()

def reverse(tuple):
    new_tup = tuple[::-1]
    return new_tup

#def insert(NAME,REGISTRATION_PLATE,VEHICLE_TYPE,VEHICLE_BRAND, FUEL_TYPE):
#    conn = sqlite3.connect("Vehicle Management System.db")
#    cursor = conn.cursor()
#    cursor.execute("""CREATE TABLE IF NOT EXISTS
#    vehicle_details(vehicleNAME TEXT, vehicleREGISTRATION_PLATE TEXT, vehilcleVEHICLE_TYPE TEXT, vehicleVEHICLEBRAND TEXT)""")
#    cursor.execute("INSET INTO vehicle VALUES ('"+str(NAME)+'", "'+str(REGISTRATION_PLATE)+'","'+str(VEHICLE_TYPE)+'","'+str(VEHICLE_BRAND)+'","'+str(FUEL_TYPE)+'"')
#    conn.commit()

#def delete(data):

# conn = sqlite3.connect("Vehicle Management System.db")
#    cursor = conn.cursor()
#    cursor.execute("""CREATE TABLE IF NOT EXISTS
#        vehicle_details(vehicleNAME TEXT, vehicleREGISTRATION_PLATE TEXT, vehilcleVEHICLE_TYPE TEXT, vehicleVEHICLEBRAND TEXT)""")
#    cursor.execute("DELETE FROM vehicle WHERE vehicleName='"+str(data)+'')

#def update(NAME,REGISTRATION_PLATE,VEHICLE_TYPE,VEHICLE_BRAND, FUEL_TYPE):
#    conn = sqlite3.connect("Vehicle Management System.db")
#    cursor = conn.cursor()
#    cursor.execute("""CREATE TABLE IF NOT EXISTS
#            vehicle_details(vehicleNAME TEXT, vehicleREGISTRATION_PLATE TEXT, vehilcleVEHICLE_TYPE TEXT, vehicleVEHICLEBRAND TEXT, vehicleFuel_type TEXT)""")
#    cursor.execute("UPDATE vehicle_details SET vehicleName='"+str(NAME)+'",vehicleREGISTRATION_PLATE="'+str(REGISTRATION_PLATE)+'", vehilcleVEHICLE_TYPE="'+str(VEHICLE_TYPE)+'",vehicleVEHICLEBRAND="'+str(VEHICLE_BRAND)+'",vehicleFuel_type="'+str(FUEL_TYPE)+'" WHERE vehicleREGISTRATION_PLATE='+str(NAME)+'""')
#    conn.commit()

#def read():
#    conn = sqlite3.connect("Vehicle Management System.db")
#    cursor = conn.cursor()
#    cursor.execute("""CREATE TABLE IF NOT EXISTS
#          vehicle_details(vehicleNAME TEXT, vehicleREGISTRATION_PLATE TEXT, vehilcleVEHICLE_TYPE TEXT, vehicleVEHICLEBRAND TEXT)""")
#    cursor.execute("SELECT * FROM vehicle_details")
#    results=cursor.fetchall()
#    conn.commit()
#    return results

#def insert_data():
#    vehicleNAME=str(name_entry.get())
#    vehicleReg = str(registration_entry.get())
#    vehicleBrand = str(vehicle_brand_entry.get())
#    vehicleType = str(vehicle_type_entry.get())
#    vehicleFueltype = str(fuel_type_entry.get())
#    if vehicleNAME ==''or  vehicleNAME =="___":
#        print("Error Inserting Name")
#    if vehicleReg ==''or  vehicleReg =="___":
#        print("Error Inserting Name")
#    if vehicleBrand ==''or  vehicleBrand =="___":
#        print("Error Inserting Name")
#    if vehicleType ==''or  vehicleType =="___":
#        print("Error Inserting Name")
#    if vehicleFueltype ==''or  vehicleFueltype =="___":
#        print("Error Inserting Name")
#    else:
#        insert(str(vehicleNAME),str(vehicleReg),str(vehicleBrand),str(vehicleType),str(vehicleFueltype))

#    for data in vehicle_details.get_children():
#        vehicle_details.delete(data)


#def update_data():
#    selected_item = vehicle_details.selection()[0]
#    update_name  = str(vehicle_details.item(selected_item)["values"][0])
#    update(name_entry.get(),registration_entry.get(),vehicle_type_entry.get,vehicle_brand_entry.get(),fuel_type_entry.get(), update_name)

#    for data in vehicle_details.get_children():
#        vehicle_details.delete(data)

#    for result in reverse(read()):
#        vehicle_details.insert(parent="", index="end", iid=0, text="", values=(result), tags="arow")

#    vehicle_details.tag_configure("grow", background="#EEEEEE", font=("comic sans mu", 15))
#    vehicle_details.grid(row=0, column=0)




win = tk.Tk()
win.geometry("1200x550")
win.title("MOTIVES MECHANICS")


automen_label = tk.Label(win, text=f" motives-mech", font=("organo", 21), bg="white", )
automen_label.place(x=0, y=0)


options_frame = tk.Frame(win, bg='blue', highlightcolor="black",bd="1",border="1",highlightbackground="black")


background = PhotoImage(file="img_2.png")
dashboard = PhotoImage(file="Dashboard_BTN.png")
mechanic = PhotoImage(file="mechnic_btn.png")
customer = PhotoImage(file="customer_btn.png")
request = PhotoImage(file="request_btn.png")
feedback = PhotoImage(file="Feedback_btn.png")


#=============================Frame code
def hide_indicator():
    dashboard_btn_indicate.config(bg="#FFFFFF")
    mechanic_btn_indicate.config(bg="#FFFFFF")
    customer_btn_indicate.config(bg="#FFFFFF")
    request_indicate.config(bg="#FFFFFF")
    feedback_btn_indicate.config(bg="#FFFFFF")

def indicate(lb, page):
    hide_indicator()
    lb.config(bg="black")
    page()


frame_title= tk.Label(win, )
frame_title.place(x=245, y=8)
dashboard_btn_indicate = Label(options_frame,text='', bg='white')
dashboard_btn_indicate.place(x=3, y=100, width=5, height=62)

mechanic_btn_indicate = Label(options_frame, text='', bg='white')
mechanic_btn_indicate.place(x=3, y=170, width=5, height=62)

customer_btn_indicate = Label(options_frame,text='', bg='white')
customer_btn_indicate.place(x=3, y=250, width=5, height=75)

request_indicate = Label(options_frame,text='', bg='white')
request_indicate.place(x=3, y=332, width=5, height=62)

feedback_btn_indicate = Label(options_frame,text='', bg='white')
feedback_btn_indicate.place(x=3, y=400, width=5, height=62)

options_frame= tk.Frame(win, bg='#FFFFFF',highlightbackground="black",highlightcolor="black")
options_frame.place(x=0, y=0, height="1500", width="248")

dashboard_btn = tk.Button(options_frame,image=dashboard, bd=0,
                          command=lambda: show_frame(dashboard_frame))
dashboard_btn.place(x=5, y=20)
mechanic_btn = tk.Button(options_frame, image=mechanic, bd=0,
                         command=lambda: show_frame(mechanic_frame))
mechanic_btn.place(x=5, y=90)

customer_btn = Button(options_frame, image=customer,bd=0, bg='white',
                      command=lambda: show_frame(customer_frame))
customer_btn.place(x=10, y=140)

request_btn = Button(options_frame, image=request,bd=0, bg='white',
                     command=lambda: show_frame(request_frame))
request_btn.place(x=10, y=210)

feedback_btn = Button(options_frame, image=feedback,bd=0, bg='white',
                      command=lambda: show_frame(feedback_frame))
feedback_btn.place(x=10, y=280)



mainframe = tk.Frame(win, )
mainframe.place(x=250, y=0, height="1500", width="1900")

search = Entry(win, bg="grey", width=50, font=("Comic Sans UI", 17))
search.place(x=350, y=3)
search.insert(0, f"                                               Search")
search.configure(state=NORMAL)
mainframe_background = tk.Label(mainframe, image=background)
mainframe_background.place(x=0, y=10)
mainframe_background = tk.Label(mainframe, text="Welcome to Automen Mechanics......", font=("Organo", 22))
mainframe_background.place(x=20, y=40)


#=================================dashboard FRAME CODE

dashboard_frame = tk.Frame(mainframe)
dashboard_label = tk.Label(dashboard_frame, image=background)
dashboard_label.pack()
message_1 = tk.Message(dashboard_frame,
                text='Welcome to Motives Mechanics',bg='#FFFFFF',font=("Organo", 25),width=600,padx=2,pady=0)
message_1.place(x=20, y=50)
message_1 = tk.Message(dashboard_frame,
                text="Here is whats happening at your garage",bg='#FFFFFF',font=("comic sans ms", 13, "italic"),width=600,padx=2,pady=0)
message_1.place(x=20, y=90)
total_customer = tk.Button(dashboard_frame, text="TOTAL CUSTOMER", border="0", bg="#ED1C24",
                           font=("comic sans ms", 13), anchor='n')
total_customer.place(x=600, y=120,width="230", height="170")
total_vehicle = tk.Button(dashboard_frame, text="TOTAL VEHICLES", border="0",bg="#8969AB", font=("comic sans ms", 13),anchor='n')
total_vehicle.place(x=100, y= 120, width="230", height="170")
total_mechanic = tk.Button(dashboard_frame, text="TOTAL MECHANICS", border="0",bg="#25817D", font=("comic sans ms", 13),anchor='n')
total_mechanic.place(x=350, y=120, width="230", height="170")
total_feedback = tk.Button(dashboard_frame, text="TOTAL FEEDBACK", border="0",bg="#EA3680", font=("comic sans ms", 13),anchor='n')
total_feedback.place(x=120, y=340, width="230", height="170")
total_user_attempts = tk.Button(dashboard_frame, text="TOTAL LOGIN ATTEMPTS", border="0",bg="#EACE15", font=("comic sans ms", 13),anchor='n')
total_user_attempts.place(x=560, y=340, width="230", height="170")
dashboard_frame.place(x=0, y=0, height=900, width=950)
dashboard_label.configure(state=NORMAL)


#vehicle_details = ttk.Treeview(dashboard_frame)

#vehicle_details["columns"]=("NAME","REGISTRATION PLATE","VEHICLE TYPE","VEHICLE BRAND","FUEL TYPE")
#vehicle_details.column("NAME", anchor=W, width=150)
#vehicle_details.column("REGISTRATION PLATE", width=150,anchor=W)
#vehicle_details.column("VEHICLE TYPE",width=150,anchor=W)
#vehicle_details.column("VEHICLE BRAND", width=200,anchor=W)
#vehicle_details.column("FUEL TYPE", width=150,anchor=W)
#vehicle_details.heading("NAME",text="NAME", anchor=W)
#vehicle_details.heading("REGISTRATION PLATE",text="REGISTRATION PLATE",anchor=W)
#vehicle_details.heading("VEHICLE TYPE",text="VEHICLE TYPE", anchor=W)
#vehicle_details.heading("VEHICLE BRAND",text="VEHICLE TYPE", anchor=W)
#vehicle_details.heading("FUEL TYPE",text="FUEL TYPE", anchor=W)

#for data in vehicle_details.get_children():
#    vehicle_details.delete(data)

#for result in reverse():
#    vehicle_details.insert(parent="", index="end",iid="o", text="", values=(result), tags="arip")

#vehicle_details.tag_configure("row", background="#EEEEEE", font=("comic sans mu", 15))
#vehicle_details.place(x=5, y=300)

driverdetails = PhotoImage(file="driver details btn.png")

#style = tk.style()
#style.configure("Treeview Heading", font=("comic sans ms", 15))
#==================================Mechanic FRAME CODE
mechanic_frame = tk.Frame(mainframe)
mechanic_label = tk.Label(mechanic_frame, image=background)
mechanic_label.pack()
total_mechanic = tk.Button(mechanic_frame, text="Work Completed", border="0",bg="#8969AB", font=("comic sans ms", 13),anchor='n',
                           command= lambda :show_frame(work_completed_frame))
total_mechanic.place(x=80, y=90, width="170", height="120")
total_mechanic = tk.Button(mechanic_frame, text="Work in Progress", border="0",bg="#25817D", font=("comic sans ms", 13),anchor='n',
                           command= lambda :show_frame(work_in_progress_frame))
total_mechanic.place(x=300, y=90, width="170", height="120")
total_mechanic = tk.Button(mechanic_frame, text="New Work Assigned", border="0",bg="#EACE15", font=("comic sans ms", 13),anchor='n',
                           command= lambda :show_frame(new_work_assigned))
total_mechanic.place(x=530, y=90, width="170", height="120")
total_mechanic = tk.Button(mechanic_frame, text="Report", border="0",bg="#ED1C24", font=("comic sans ms", 13),anchor='n',
                           command= lambda :show_frame(report))
total_mechanic.place(x=750, y=90, width="170", height="120")
work_completed_frame = tk.Frame(mechanic_frame, bg="grey")
work_completed_frame.place(x=150, y=300,  height=300, width=700)
fun = tk.Label(work_completed_frame, text="do it")
fun.pack()
work_in_progress_frame = tk.Frame(mechanic_frame, bg="grey")
work_in_progress_frame.place(x=150, y=300,  height=300, width=700)
key = tk.Label(work_in_progress_frame, text="it ok")
key.pack()
new_work_assigned = tk.Frame(mechanic_frame, bg="grey")
new_work_assigned.place(x=150, y=300,  height=300, width=700)
big = tk.Label(new_work_assigned, text="graphic")
big.pack()
report = tk.Frame(mechanic_frame, bg="grey")
report.place(x=90, y=300,  height=300, width=700)
report_label = tk.Label(report, text="Report", font=("game of squids", 16, "italic"), bg="grey", fg="red")
report_label.pack()
registered_date_label = tk.Label(report, text="REGISTERED DATE", anchor="n", font=("comic sans ms", 15))
registered_date_label.place(x=150, y=50)
registration_label = tk.Label(report, text="REGISTERED USER", anchor="n", font=("comic sans ms", 15))
registration_label.place(x=150, y=100)
vehicle_type_label = tk.Label(report, text="VEHICLE MILAGE", anchor="n", font=("comic sans ms", 15))
vehicle_type_label.place(x=150, y=150)
vehicle_brand_label = tk.Label(report, text="ISSUE/S", anchor="n", font=("comic sans ms", 15))
vehicle_brand_label.place(x=150, y=200)
registered_user_entry = tk.Entry(report, font=("comic sans ms", 15))
registered_user_entry.place(x=500, y=100)
registered_entry = tk.Entry(report, font=("comic sans ms", 15))
registered_entry.place(x=500, y=50)
vehicle_milage_entry = tk.Entry(report, font=("comic sans ms", 15))
vehicle_milage_entry.place(x=500, y=150)
issues_entry = tk.Entry(report, font=("comic sans ms", 15))
issues_entry.place(x=500, y=200)
mechanic_frame.place(x=0, y=0)


#==================================customer FRAME CODE
customer_frame = tk.Frame(mainframe)
customer_label = tk.Label(customer_frame, image=background)
customer_label.pack()
vehicle_details_btn = tk.Button(customer_frame, text="VEHICLE DETAILS",bg="#8969AB",font=("comic sans ms", 13), anchor='n',
                                command= lambda: show_frame(vehicle_detailsframe))
vehicle_details_btn.place(x=40, y=120, width="230", height="100")
driverdetails_btn = tk.Button(customer_frame, text="DRIVER DETAILS", border="0",bg="#ED1C24", font=("comic sans ms", 13), anchor='n',
                              command= lambda: show_frame(driver_detailsframe))
driverdetails_btn.place(x=700, y=120, width="230", height="100")
availablebkng_btn = tk.Button(customer_frame, text="BOOKING", border="0",bg="#EACE15",font=("comic sans ms", 11),anchor='n',
                              command= lambda: show_frame(booking_frame))
availablebkng_btn.place(x=400, y=120, width="230", height="100")
#===========================vehicle details================================
vehicle_detailsframe = tk.Frame(customer_frame, bg="dark grey", height="1500", width='950')
vehicle_detailsframe.place(x=0, y=250)
vehicle_details_label = tk.Label(vehicle_detailsframe, text="Vehicle Details", anchor="n", font=("game of squids", 15))
vehicle_details_label.place(x=400, y=0)
name_label = tk.Label(vehicle_detailsframe, text="NAME", anchor="n", font=("comic sans ms", 15))
name_label.place(x=150, y=50)
registration_label = tk.Label(vehicle_detailsframe, text="REGISTRATION PLATE", anchor="n", font=("comic sans ms", 15))
registration_label.place(x=150, y=100)
vehicle_type_label = tk.Label(vehicle_detailsframe, text="VEHICLE TYPE", anchor="n", font=("comic sans ms", 15))
vehicle_type_label.place(x=150, y=150)
vehicle_brand_label = tk.Label(vehicle_detailsframe, text="VEHICLE BRAND", anchor="n", font=("comic sans ms", 15))
vehicle_brand_label.place(x=150, y=200)
fuel_type_label = tk.Label(vehicle_detailsframe, text="FUEL TYPE", anchor="n", font=("comic sans ms", 15))
fuel_type_label.place(x=150, y=250)
name_entry = tk.Entry(vehicle_detailsframe, font=("comic sans ms", 15))
name_entry.place(x=500, y=50)
registration_entry = tk.Entry(vehicle_detailsframe, font=("comic sans ms", 15))
registration_entry.place(x=500, y=100)
vehicle_type_entry = tk.Entry(vehicle_detailsframe, font=("comic sans ms", 15))
vehicle_type_entry.place(x=500, y=150)
vehicle_brand_entry = tk.Entry(vehicle_detailsframe, font=("comic sans ms", 15))
vehicle_brand_entry.place(x=500, y=200)
fuel_type_entry = tk.Entry(vehicle_detailsframe, font=("comic sans ms", 15))
fuel_type_entry.place(x=500, y=250)
#enter_btn = tk.Button(vehicle_detailsframe, text="Enter", font=("ardestine", 15), bd=0,command=insert_data())
#enter_btn.place(x=800, y=250)



#==========driver details===============================
driver_detailsframe = tk.Frame(customer_frame, bg="dark grey", height="1500", width='950')
driver_detailsframe.place(x=0, y=250)
driver_detailslabel = tk.Label(driver_detailsframe, text="Driver Details", anchor="s", font=("game of squids", 15))
driver_detailslabel.place(x=400, y=0)
first_name_label = tk.Label(driver_detailsframe, text="FIRST NAME", anchor="n", font=("comic sans ms", 15))
first_name_label.place(x=150, y=50)
last_name_label = tk.Label(driver_detailsframe, text="LAST NAME", anchor="n", font=("comic sans ms", 15))
last_name_label.place(x=150, y=100)
national_id_label = tk.Label(driver_detailsframe, text="NATIONAL ID", anchor="n", font=("comic sans ms", 15))
national_id_label.place(x=150, y=150)
address_label = tk.Label(driver_detailsframe, text="ADDRESS", anchor="n", font=("comic sans ms", 15))
address_label.place(x=150, y=200)
phone_num_label = tk.Label(driver_detailsframe, text="PHONE NUMBER", anchor="n", font=("comic sans ms", 15))
phone_num_label.place(x=150, y=250)
licence_category_label = tk.Label(driver_detailsframe, text="LICENSE CATEGORY", anchor="n", font=("comic sans ms", 15))
licence_category_label.place(x=150, y=250)
first_name_entry = tk.Entry(driver_detailsframe, font=("comic sans ms", 15))
first_name_entry.place(x=500, y=50)
last_name_entry = tk.Entry(driver_detailsframe, font=("comic sans ms", 15))
last_name_entry.place(x=500, y=100)
national_id_entry = tk.Entry(driver_detailsframe, font=("comic sans ms", 15))
national_id_entry.place(x=500, y=150)
address_entry = tk.Entry(driver_detailsframe, font=("comic sans ms", 15))
address_entry.place(x=500, y=200)
phone_num_entry = tk.Entry(driver_detailsframe, font=("comic sans ms", 15))
phone_num_entry.place(x=500, y=250)
enter_btn = tk.Button(driver_detailsframe, text="Enter", font=("ardestine", 15), bd=0, )
enter_btn.place(x=800, y=250)
#=========booking
booking_frame = tk.Frame(customer_frame, bg="dark grey", height="1500", width='950')
booking_frame.place(x=0, y=250)
availabledates_details_label = tk.Label(booking_frame, text="Booking", anchor="center", font=("game of squids", 15))
availabledates_details_label.place(x=390, y=0)
booking_date_label = tk.Label(booking_frame, text="BOOKING DATE", anchor="n", font=("comic sans ms", 15))
booking_date_label.place(x=150, y=50)
start_date_label = tk.Label(booking_frame, text="START DATE", anchor="n", font=("comic sans ms", 15))
start_date_label.place(x=150, y=100)
end_id_label = tk.Label(booking_frame, text="END DATE", anchor="n", font=("comic sans ms", 15))
end_id_label.place(x=150, y=150)
security_deposit_label = tk.Label(booking_frame, text="SECURITY DEPOSIT", anchor="n", font=("comic sans ms", 15))
security_deposit_label.place(x=150, y=200)
vehicle_category_label = tk.Label(booking_frame, text="VEHICLE CATEGORY", anchor="n", font=("comic sans ms", 15))
vehicle_category_label.place(x=150, y=250)
start_date_entry = tk.Entry(booking_frame, font=("comic sans ms", 15))
start_date_entry.place(x=500, y=50)
end_date_entry = tk.Entry(booking_frame, font=("comic sans ms", 15))
end_date_entry.place(x=500, y=100)
security_deposit_entry = tk.Entry(booking_frame, font=("comic sans ms", 15))
security_deposit_entry.place(x=500, y=150)
vehicle_category_label = tk.Entry(booking_frame, font=("comic sans ms", 15))
vehicle_category_label.place(x=500, y=200)
enter_btn = tk.Button(booking_frame, text="Enter", font=("ardestine", 15), bd=0, )
enter_btn.place(x=800, y=250)

customer_label1 = tk.Label(customer_frame, text="No Cap,  All Frap", fg="white", font=("comic sans ui", 24, "italic","bold"), border="0", bg="#101115")
customer_label1.place(x=40, y=60)
customer_frame.place(x=0, y=0)
#==================================feedback FRAME CODE
feedback_frame = tk.Frame(mainframe)
feedback_label = tk.Label(feedback_frame, image=background)
feedback_label.pack()
feedback_label1 = tk.Label(feedback_frame, text="Drop your feedback in the message box below", font=("organo", 14), bg='black', fg="white")
feedback_label1.place(x=150, y=60)
feedback_entry = tk.Entry(feedback_frame, font=("comic sans ms",14))
feedback_entry.place(x=200, y=200, height=200, width=500)
feedback_frame.place(x=0, y=0)


#==================================request FRAME CODE
request_frame = tk.Frame(mainframe)
request_label = tk.Label(request_frame, image=background)
request_label.place(x=0, y=0)
request_label1 = tk.Label(request_frame, text="Whats your request on our garage", font=("organo", 17), bg='blue')
request_label1.place(x=150, y=60)




#=============================Options_F 2 code
#frame2_title= tk.Label(frame, text="Mechanic Details ", bg="blue")
#frame2_title.pack(fill="x")

#frame2_btn = tk.Button(frame, text="Enter", command=s
#frame2_btn.pack()

#=============================Frame 3 code
#frame3_title= tk.Label(mainframe, text="Customer Details ", bg="black")
#frame3_title.pack(fill="x")

#frame3_btn = tk.Button(mainframe, text="Enter", command=lambda:show_frame(mainframe))
#frame3_btn.pack()

#show_frame(mainframe)
options_frame.place(x=0, y=30)
win.mainloop()
