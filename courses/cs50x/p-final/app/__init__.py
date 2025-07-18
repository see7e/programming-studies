from flask import Flask

app = Flask(__name__,template_folder='template')

from app.controllers import default