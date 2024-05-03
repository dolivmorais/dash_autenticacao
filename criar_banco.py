from dashapp import server , database
from dashapp.model import Usuario


with server.app_context():
    database.create_all()
