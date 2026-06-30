from flask import Flask, render_template, request
import csv
import datetime

app = Flask(__name__)

MENU = {
    "Veg Burger": 60,
    "Pasta": 80,
    "Cold Coffee": 50,
    "Rajma Chawal": 70,
    "Samosa": 20,
}

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/menu', methods=['POST'])
def menu():
    name = request.form['name']
    return render_template("menu.html", name=name, menu=MENU)

# @app.route('/order', methods=['POST'])
# def order():
#     name = request.form['name']
#     items = request.form.getlist('item[]')
#     quantities = request.form.getlist('quantity[]')
#     time = datetime.datetime.now().strftime("%H:%M")

#     with open('orders.csv', 'a', newline='') as f:
#         writer = csv.writer(f)
#         for i in range(len(items)):
#             writer.writerow([name, items[i], quantities[i], time, "Preparing"])

#     return render_template("order.html", name=name, items=zip(items, quantities))

@app.route('/order', methods=['POST'])
def order():
    name = request.form['name']
    items = request.form.getlist('item[]')
    quantities = request.form.getlist('quantity[]')

    time = datetime.datetime.now().strftime("%H:%M")

    with open('orders.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for i in range(len(items)):
            writer.writerow([name, items[i], quantities[i], time, "Preparing"])

    # send only item names to frontend
    return render_template("order.html", name=name, items=items)

@app.route('/admin')
def admin():
    orders = []
    try:
        with open('orders.csv', 'r') as f:
            reader = csv.reader(f)
            orders = list(reader)
    except:
        pass

    return render_template("admin.html", orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
