from dash import Dash
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Dash(__name__)
server = app.server
#app.config.suppress.callback_exceptions = True

server.config.update(
    SQLALCHEMY_DATABASE_URI ="sqlite:///bancodedados.bd",
    SECRET_KEY='njbfjdhbfuirethreiwtjfweoitreg86df4h87st',
    SQLALCHEMY_TRACK_MODIFICATIOS=False
)

database = SQLAlchemy(server)
bcrypt = Bcrypt(server)
login_manager = LoginManager(server)
login_manager.login_view = "/login"

from dashapp import views