from flask import Flask, render_template
from flask_migrate import Migrate
from database import db
from diario import Diario
from flask import jsonify
from flask.cli import with_appcontext
import click


app = Flask(__name__)
app.config['SECRET_KEY'] = 'snowy'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///diario.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



db.init_app(app)

migrate = Migrate(app, db)

@app.cli.command("testing")

@with_appcontext

def hello():
    click.echo("tudo joia")

@app.route('/')

def index():
      return render_template('diarios.html')

if __name__ == '__main__':
       app.run(debug=True)

