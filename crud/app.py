
from flask import Flask, render_template,request,redirect,url_for
from models import db, Details
from flask_migrate import Migrate, migrate

app=Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://root:1234@localhost/flask_1_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False


db.init_app(app)
migrate=Migrate(app,db)


@app.route('/list')
def details():
    all_data=Details.query.all()
    return  render_template('list.html',data=all_data)


@app.route('/form',methods=["GET","POST"])
def details_add():

    if request.method=='POST':
        name=request.form["name"]
        age = request.form["age"]
        print(name,age)

        new_details=Details(name=name,age=age)
        db.session.add(new_details)
        db.session.commit()

        return  redirect(url_for('details'))

    return  render_template('form.html')


@app.route('/edit/<int:id>',methods=['GET','POST'])
def details_edit(id):

    data=Details.query.get(id)


    if request.method=="POST":
        data.name = request.form["name"]
        data.age = request.form["age"]
        db.session.commit()
        return  redirect(url_for('details'))

    return render_template('edit_form.html',details=data)

@app.route('/')
def home():
    return "Flask MySql App connected"


@app.route('/delete/<int:id>')
def details_delete(id):

    data=Details.query.get(id)
    db.session.delete(data)
    db.session.commit()

    return redirect(url_for('details'))


if __name__=="__main__":
    app.run(debug=True)
