from flask import Flask
from routes.vertex import *
from routes.edge import *
from routes.index import *
from routes.remove import *
from routes.rm_edge import *

app = Flask(__name__, static_folder='public')


edge(app)
index_route(app)
remove(app)
rm_edge(app)
vertex(app)
if __name__ == '__main__':
    app.run(debug=True)
