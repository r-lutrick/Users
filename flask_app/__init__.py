from flask import Flask
app = Flask(__name__)
app.secret_key = "No secrets here..."

# GLOBAL VARIABLES
DATABASE = "users_schema"
