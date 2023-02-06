import cherrypy
import os.path
import configparser
import json

class Server(object):
  def __init__(self):
        self.response_json_objectresponse_json_object=''
        with open('./response.json') as f:
            self.response_json_object = json.load(f)

  @cherrypy.expose()
  @cherrypy.tools.json_in()
  @cherrypy.tools.json_out()
  def context(self):
        return self.response_json_object

configfile=os.path.join(os.path.dirname(__file__),'./server.conf')
cherrypy.quickstart(Server(),'/scheda', config=configfile)