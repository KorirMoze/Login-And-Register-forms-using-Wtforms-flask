from pyclbr import Class
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from main import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    userName=db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    userImage = db.Column(db.String(20),  nullable=False,default="default.jpg")
    password= db.Column(db.String(60),nullable=False)\

def get_reset_token(self, expires_sec=1800):
    s=Serializer(app.config["SECRET_key"],expires_sec)
    return s.dumps({"user_id":self.id}).decode("utf-8")
def verify_token(token):
    s = Serializer(app.config["SECRET_key"])
    try:
        user_id= s.loads(token)["user_id"]
    except:
        return None
    return User.query.get(user_id)


    def __rep__(self):
        return f"User('{self.userName}','{self.email}','{self.userImage}','{self.password}')"

class product(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    productName= db.Column(db.String(100),unique=True,nullable=False)
    productImage = db.Column(db.LargeBinary, unique=True, nullable=False,default="product.jpg")
    productDescription=db.Column(db.String(800))



    def __rep__(self):
        return f"product('{self.productName}','{self.productDescription}','{self.productImage}')"