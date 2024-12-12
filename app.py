import  os


from flask import  Flask,render_template,redirect,request,Response
from models import User,Education,Contact,db
from  werkzeug.utils import secure_filename

secret_key = os.urandom(32)
app = Flask(__name__)
def create_app():
 app = Flask(__name__)

 app.config['SQLALCHEMY_DATABASE_URI']=('sqlite://users.db')
 app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
 app.config['SECRET_KEY']= secret_key

 with app.app_context():
  db.create_all()

 return app


@app.route("/")
def index():
 return  render_template("index.html")

@app.route("/create")
def create():
    return  render_template("create.html")
if __name__ == "__main__":
    app.run(debug=True)
