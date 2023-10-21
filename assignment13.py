from flask import Flask, request, jsonify #importing request will call local host, jsonify will convert data to list or dict without using keyword
import sqlite3 #sql linberary to create database in python and easyly modify it
from datetime import datetime #  in python there not to data method so have to use date time module or inbuilt funtion


app = Flask(__name__) #it create an app to run on

connection = sqlite3.connect('delivery.db') # creating conection to db
cursor = connection.cursor() # creating cursor to add tables data in here

'''
 all table data is here and new table have to be added in this section
'''

cursor.execute('''
    CREATE TABLE IF NOT EXISTS flipkart(
        fid INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL, 
        last_name TEXT NOT NULL,
        mobile INTEGER NOT NULL,
        email_id TEXT NOT NULL,
        Address TEXT NOT NULL
        )
''')
cursor.execute('''
      CREATE TABLE IF NOT EXISTS orders(
      order_id INTEGER PRIMARY KEY, 
      fid INTEGER,	 
      pickup_address TEXT NOT NULL,
      destination_address TEXT NOT NULL,
      pickup_date DATETIME NOT NULL,
      estimate_delivery_date DATETIME NOT NULL,
      status TEXT NOT NULL,
      courier_id integer NOT NULL,
      foreign key (fid) references flipkart(fid),
      foreign key (courier_id) references couriers (courier_id)
      )
''')

cursor.execute('''
               CREATE TABLE IF NOT EXISTS couriers(
               courier_id integer PRIMARY KEY,
               courier_name text NOT NULL,
               contact_number integer NOT NULL
        )
''')
cursor.execute('''
      CREATE TABLE IF NOT EXISTS tracking_history(
      tracking_id integer primary key,
      order_id integer,
      status text NOT NULL ,
      location text NOT NULL,
      update_time DATETIME NOT NULL,
      foreign key (order_id) references orders (order_id)
      )
''')
connection.commit()
connection.close()


'''
this section is for operation purpose getting data from table,alteration, deletion, updation and
new operation will be perform here, onwards.
'''

@app.route('/Flipkart_customers')
def all_customers():
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    data = cursor.execute('select * from flipkart').fetchall()
    connection.close()
    return jsonify({'flipkart': data})

@app.route('/my-details', methods=['POST'])
def my_account():
    data = request.get_json()
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    cursor.execute('select * from flipkart where fid = ?', (data['fid'],))
    account = cursor.fetchone()
    connection.close()
    if account:
        return jsonify({'flipkart': account})
    else:
        return 'Account Not Found', 404


@app.route('/all_orders')
def orders():
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    data = cursor.execute('select * from orders').fetchall()
    connection.close()
    return jsonify({'orders': data})

@app.route('/my_orders', methods = ['POST'])
def my_orders():
    data = request.get_json()
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    cursor.execute('select * from orders join flipkart on flipkart.fid = orders.fid where flipkart.fid = ?', (data['fid'],))
    order = cursor.fetchall()
    connection.close()
    if order:
        return jsonify({'orders': order})
    else:
        return 'Order Not Found', 404

@app.route('/all_couriers')
def all_couriers():
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    data = cursor.execute('select * from couriers').fetchall()
    connection.close()
    return jsonify({'couriers' : data})

@app.route('/all_tracking')
def all_tracking():
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    data = cursor.execute('select * from tracking_history').fetchall()
    connection.close()
    return jsonify({'tracking_history' : data})

@app.route('/track_myorder', methods = ['POST'])
def track_myorder():
    data = request.get_json()
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    cursor.execute('select * from tracking_history where tracking_id = ?',(data['tracking_id'],))
    my_tracking = cursor.fetchone()
    connection.commit()
    connection.close()
    if my_tracking:
        return jsonify({'tracking_history' : my_tracking})
    else:
        return 'Order Not Found PLease Entre Valid Tracking ID'

@app.route('/cancel_my_order', methods = ['POST'])
def cancel_my_order():
    data = request.get_json()
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    cursor.execute('select order_id from orders where order_id = ?',(data['order_id'],))
    active_order = cursor.fetchone()
    if active_order:
        cursor.execute('delete from orders where order_id = ?',(data['order_id'],))
        connection.commit()
        connection.close()
        return 'Order Has Been Successfully Canceled'
    else:
        connection.close()
        return 'Order Not Found PLease Enter Valid Order id'



'''
add all details like flipkart_customer_Details,
new_order,courier_details and order_tracking in this section
'''

@app.route('/new_user_registration', methods=['POST'])
def new_user():
    data = request.get_json()
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    cursor.execute('insert into flipkart (fid,first_name,last_name,mobile,email_id,address)values(?,?,?,?,?,?)',(data['fid'],data['first_name'],data['last_name'],data['mobile'],data['email_id'],data['address']))
    connection.commit()
    connection.close()
    return 'Flipkart Customer Account Created successfully..'

@app.route('/new_order', methods=['POST'])
def new_order():
    data = request.get_json()
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    pickup_date = datetime.strptime(data['pickup_date'],'%Y-%m-%d %H:%M:%S')
    estimate_delivery_date = datetime.strptime(data['estimate_delivery_date'], '%Y-%m-%d %H:%M:%S')
    cursor.execute('insert into orders(order_id,fid,pickup_address,destination_address,pickup_date,estimate_delivery_date,status,courier_id) values(?, ?, ?, ?, ?, ?, ?, ?)',(data['order_id'],data['fid'],data['pickup_address'],data['destination_address'],pickup_date,estimate_delivery_date,data['status'],data['courier_id']))
    connection.commit()
    connection.close()
    return 'New Order Created Successfully..'


@app.route('/courier_details', methods = ['POST'])
def courier_details():
    data = request.get_json()
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    cursor.execute('insert into couriers (courier_id,courier_name,contact_number) values(?, ?, ?)',(data['courier_id'],data['courier_name'],data['contact_number']))
    connection.commit()
    connection.close()
    return ' New Courier ID Added SuccessFully'

@app.route('/track_order', methods = ['POST'])
def track_order():
    data = request.get_json()
    connection = sqlite3.connect('delivery.db')
    cursor = connection.cursor()
    update_time = datetime.strptime(data['update_time'],'%Y-%m-%d %H:%M:%S')
    cursor.execute('insert into tracking_history(tracking_id,order_id,status,location,update_time) values(?,?,?,?,?)',(data['tracking_id'],data['order_id'],data['status'],data['location'],update_time))
    connection.commit()
    connection.close()
    return 'Order Tracking Details added Successfully'

if __name__ == '__main__':
    app.run(port=5001)
'''
order delivered successfully
order has shiped and will be delivered by estimate_delivery_date
out for delivery
order has reached nearby hub and will be delivered by estimate_delivery_date
'''
