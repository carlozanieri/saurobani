import loader
from cherrypy import request
import cherrypy
import os.path
import configparser
import urllib
from urllib.request import urlopen
from jinja2 import Environment, FileSystemLoader
from  Connect import Connect
env = Environment(loader=FileSystemLoader('templates'))
class HelloWorld():
    @cherrypy.expose
    def index( self,pag):
        
        if cherrypy.url() == 'http://carlozanieri.it/?pag=master':
            tmpl = env.get_template('mytemplate.html')

            page= tmpl.render(pag="blog",blogs=Connect.blog(""), target='World',  menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "index"),  luogo = "index")
        elif cherrypy.url() == 'http://carlozanieri.it/?pag=blog':
            tmpl = env.get_template('mytemplate.html')

            page= tmpl.render(blogs=Connect.blog(""),pag=codice, target='World',  menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "index"),  luogo = "index")   
        
        elif cherrypy.url() == 'http://blog.carlozanieri.it/':
            tmpl = env.get_template('carlozanieriblog.html')
                
        elif cherrypy.url() == 'http://web.carlozanieri.it/':
            tmpl = env.get_template('carlozanieriweb.html')

            page= tmpl.render( blogs=Connect.blog(""), target='World',  menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "index"),  luogo = "index")   
        
        elif cherrypy.url() == 'http://linuxmugello.net/' :
            tmpl = env.get_template('mytemplate.html')
            page = tmpl.render( blogs=Connect.blog(""), target='World',  menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "mugello"),  luogo = "mugello", urlx=cherrypy.url())
        elif cherrypy.url() == 'http://localhost/' :
            tmpl = env.get_template('mytemplate.html')
            
            page = tmpl.render(pag=pag,blogs=Connect.blog(""), target='World',  manifestazione="blog", menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "mugello"),  luogo = "mugello", urlx=cherrypy.url())
        
        elif cherrypy.url() == 'http://localhost/?pag=blog' :
            tmpl = env.get_template('mytemplate.html')
            par="blog"
            page = tmpl.render(pag="blog",blogs=Connect.blog(""), target='World',  manifestazione="blog", menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "mugello"),  luogo = "mugello", urlx=cherrypy.url())
        
        elif cherrypy.url() == 'http://carlozanieri.it/?pag=blog' :
            tmpl = env.get_template('mytemplate.html')
            page = tmpl.render(pag="blog",blogs=Connect.blog(""), target='World',  manifestazione="blog", menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "mugello"),  luogo = "mugello", urlx=cherrypy.url())
        
        elif cherrypy.url() == 'http://0.0.0.0/' :
            tmpl = env.get_template('index.html')
            page = tmpl.render(blogs=Connect.blog(""), target='World',  menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "mugello"),  luogo = "mugello", urlx=cherrypy.url())
        
        else:
            tmpl = env.get_template('mytemplate.html')
            pag="blog"
            page = tmpl.render(pag="blog",blogs=Connect.blog(""), target='World',  menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "sanpiero"),  luogo = "sanpiero", news=Connect.news(""),urlx=cherrypy.url())
                 

        return page
    @cherrypy.expose
    def test(self):
        return "Test Controller"
    
    @cherrypy.expose
    def submit(self, cancel =False,**value):
        if cherrypy.request.method=='POST':
            if cancel:
                raisecherrypy.HTTPRedirect('/')# to cancel the action
                link=Link(**value)
                self.data[link.id]= link
                raisecherrypy.HTTPRedirect('/submit')
        tmp=env.get_template('submit.html')
        streamValue=tmp.generate()
        return tmp.render(salutation='Hello', target='World')
    
    @cherrypy.expose
    def menu(self):
        tmp=env.get_template('menu5.html')
        streamValue=tmp.generate()
        return tmp.render(salutation='Menu', target='World',menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "index"), renderer='json')
        

    @cherrypy.expose
    def slide(self, luogo):
        tmp=env.get_template('nivo.html')
        streamValue=tmp.generate()
        
        #luogo = request.params[0]

        return tmp.render(luogo = "sanpiero", slider=Connect.slider("", luogo), renderer="json")


    
    @cherrypy.expose
    def news_one(request,titolo,id):
        #titolo=request.POST['titolo']
        tmp=env.get_template('news_one.html')
        #id=request.POST['id']
        return tmp.render(pagina=Connect.body("", "sanpiero"), manifestazione="Blog", news=Connect.news_one("",titolo, id))
    
    @cherrypy.expose
    def blogs_one(request,titolo,id):
        #titolo=request.POST['titolo']
        tmp=env.get_template('blogs_one.html')
        #id=request.POST['id']
        return tmp.render(pagina=Connect.body("", "sanpiero"), manifestazione="Blog", blogs=Connect.blogs_one("",titolo, id))
    @cherrypy.expose
    def sanpiero(self):
        tmpl = env.get_template('mytemplate.html')
        return tmpl.render(salutation='Hello', target='World',  menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "sanpiero"),  luogo = "sanpiero")

    @cherrypy.expose
    def mugello(self):
        tmpl = env.get_template('mytemplate.html')
        return tmpl.render(salutation='Hello', target='World',  menu=Connect.menu(""), submenu=Connect.submnu(""),pagina=Connect.body("", "mugello"),  luogo = "mugello")

    @cherrypy.expose
    def newss(self,*url_parts, **params):
                
        tmp=env.get_template('news.html')
        return tmp.render( pagina=Connect.body("", "sanpiero"), manifestazione="news", news=Connect.news(""), urlx="by Carlo Zanieri")
        
        
    @cherrypy.expose
    def store_mp3_view(request):
            # ``filename`` contains the name of the file in string format.
            #
            # WARNING: Internet Explorer is known to send an absolute file
            # *path* as the filename.  This example is naive; it trusts
            # user input.
        filename = request.POST['file'].filename
        dirname = request.POST['dir']

        # ``input_file`` contains the actual file data which needs to be
        # stored somewhere.
        input_file = request.POST['file'].file

        # Using the filename like this without cleaning it is very
        # insecure so please keep that in mind when writing your own
            # file handling.
        file_path = os.path.join(dirname, filename)
        with open(file_path, 'wb') as output_file:
            shutil.copyfileobj(input_file, output_file)

        tmp=env.get_template('upload_form.html')
        return tmp.render( pagina=Connect.body("", "sanpiero"), manifestazione="news", news=Connect.news(""))
        return Response(' File  ' + filename + '  salvato correttamente' )
    
    
    @cherrypy.expose
    def blog(self, path=None):
        #cherrypy.HTTPRedirect("localhost?pag=blog")       
        #tmp=env.get_template('mytemplate.html')
        #return tmp.render( pag="blog", pagina=Connect.body("", "sanpiero"), manifestazione="blog", blogs=Connect.blog(""), urlx="by Carlo Zanieri", luogo = "blog")
        if not path:
          raise cherrypy.HTTPRedirect("http://localhost/?pag=blog") 
        return path
    @cherrypy.expose
    def blogs(self):
                
        tmp=env.get_template('blogs.html')
        return tmp.render( pagina=Connect.body("", "sanpiero"), manifestazione="blog", blogs=Connect.blog(""), urlx="by Carlo Zanieri", luogo = "blog")
    
    
    
    @cherrypy.expose
    def upload_form(self, file, dir, tipo, titolo, descrizione, dirdb):
        # Either save the file to the directory where server.py is
        # or save the file to a given path:
        # upload_path = '/path/to/project/data/'
        upload_path = dir

        # Save the file to a predefined filename
        # or use the filename sent by the client:
        # upload_filename = ufile.filename
        upload_filename = file.filename
        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))
        size = 0
        
        with open(upload_file, 'wb') as out:
            while True:
                data = file.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
            if tipo == "manifestazioni" :
                Connect.ins_manifesta("",dirdb, file.filename, titolo, descrizione)
            elif tipo == "news" :
                Connect.ins_news("",dirdb, file.filename, titolo, descrizione, tipo)
        out = '''
        
File received.
Filename: {}
Length: {}
Mime-type: {}
''' .format(upload_path + "/" + file.filename, size, file.content_type, data)
        return out

    @cherrypy.expose
    def ins_manifesta(self, file, dir, titolo, descrizione, dirdb):
        # Either save the file to the directory where server.py is
        # or save the file to a given path:
        # upload_path = '/path/to/project/data/'
        upload_path = os.path.dirname(dir)

        # Save the file to a predefined filename
        # or use the filename sent by the client:
        # upload_filename = ufile.filename
        upload_filename = file.filename
        upload_file = os.path.normpath(
            os.path.join(upload_path, upload_filename))
        size = 0
        
        with open(upload_file, 'wb') as out:
            while True:
                data = file.file.read(8192)
                if not data:
                    break
                out.write(data)
                size += len(data)
            Connect.ins_manifesta("",upload_path, file.filename, titolo, descrizione)
        out = '''
        
File received.
Filename: {}
Length: {}
Mime-type: {}
''' .format(upload_path + "/" + file.filename, size, file.content_type, data)
        return out

    
    @cherrypy.expose
    def upload(request):
       
        tmp=env.get_template('upload_form.html')
        return tmp.render( pagina=Connect.body("", "sanpiero"), manifestazione="news", news=Connect.news(""))

    @cherrypy.expose
    def ins_manifestazioni(request):
       
        tmp=env.get_template('inserimenti.html')
        return tmp.render( pagina=Connect.body("", "sanpiero"), manifestazione="news", news=Connect.news(""), directory="./static/manifestazioni/img/" , dirdb="/manifestazioni/img/",tipo="manifestazioni")

    @cherrypy.expose
    def ins_news(request):
       
        tmp=env.get_template('inserimenti.html')
        return tmp.render( pagina=Connect.body("", "sanpiero"), manifestazione="news", news=Connect.news(""), directory="./static/news/img/",dirdb="/news/img/" ,tipo="news")


    @cherrypy.expose
    def manifesta(request):
       
        tmp=env.get_template('ins_manifesta.html')
        return tmp.render( pagina=Connect.body("", "sanpiero"), manifestazione="news", news=Connect.news(""))
configfile=os.path.join(os.path.dirname(__file__),'./server.conf')
cherrypy.quickstart(HelloWorld(), config=configfile)