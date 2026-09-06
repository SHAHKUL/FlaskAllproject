from flask_sqlalchemy import  SQLAlchemy
from sqlalchemy.engine import default

db=SQLAlchemy()


class Details(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    age=db.Column(db.Integer)


    # username=db.Column(db.String(100),unique=True,nullable=True)
    # description=db.Column(db.Text)
    # dob=db.Column(db.Date)
    # student=db.Column(db.Boolean,default=True)
    # average=db.Column(db.Float,default=0.0)
    #
    # def __repr__(self):
    #     return self.name
