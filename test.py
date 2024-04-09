from flask import Flask,render_template,jsonify

app= Flask(__name__)


food_items=[
    {
        "id":1,
        "food":'Dhokla',
        'mrp':'₹50'
    },
    {
        "id":2,
        "food":'Biryani',
        'mrp':'₹100'
    },
    {
        "id":3,
        "food":'Chole Bhature',
        'mrp':'₹150'
    }
]

@app.route("/")
def hello_world():
    return render_template("index.html",food=food_items)


@app.route('/api/food')
def food_itemslist():
    return jsonify(food_items)
    
app.run(debug=True)

