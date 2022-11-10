from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class proList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.id
    
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        quantity = request.form.get("quantity")
        price = request.form.get("price")
        
        newProduct = proList(name=name,quantity=quantity, price=price)
        db.session.add(newProduct)
        db.session.commit()
        
    all = proList.query.order_by(proList.id).all()
    return render_template('index.html', products = all)
        

@app.route('/edit/', methods=["POST", "GET"])
def edit():
    if request.method == "POST":
        id = request.form.get("id")
        newName = request.form.get("name")
        newQuantity = request.form.get("quantity")
        newPrice = request.form.get("price")
        
        item = proList.query.get(id)
        
        if newName:
            item.name = newName
        if newQuantity:
            item.quantity = newQuantity
        if newPrice:
            item.price = newPrice
        
        db.session.commit()
        return redirect('/')
    else:
        id = request.args.get("id")
        all = proList.query.order_by(proList.id).all()
        product = proList.query.filter_by(id=id).first()
        return render_template("editModal.html", id=id, products=all, product=product)



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)