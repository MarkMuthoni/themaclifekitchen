from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kje@3fv3n3ij4ew43hi4fb878ct67g67g54h4we5bh'

from Kitchen import routes
