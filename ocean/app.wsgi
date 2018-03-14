import sys

sys.path.insert(0,"/home/pmukherjee/tools/pythonexamples/ocean")


import bottle
import app


bottle.TEMPLATE_PATH.insert(0, '/home/pmukherjee/tools/pythonexamples/ocean/views')
application = bottle.default_app()

