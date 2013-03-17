import webapp2
from google.appengine.api import users
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class HomePage(webapp2.RequestHandler):
    def get(self):
        
        
        #set stylesheets needed per page 
        specific_urls = """
            <link type="text/css" rel="stylesheet" href="/stylesheets/""" + self.__class__.__name__ + """.css" />
        """
        
        
        myFile = open('Page_Content/main.html', 'r')
        
        #Set the nav depending on login status
        if users.get_current_user():
            url = users.create_logout_url(self.request.uri)
            nav = """
            <nav>
                <ul>
                    <li><a href="/dashboard">Dashboard</a></li>
                    <li><a href="#">Design</a></li>
                    <li><a href="#">About</a></li>
                    <li><a href="%s">Logout</a></li>
                </ul>
            </nav>
            """ % url
        else:
            url = users.create_login_url(self.request.uri + "dashboard")
            nav = """
            <nav>
                <ul style="margin-left:40px;">
                    <li style="padding-right: 20px;"><a href="#">Home</a></li>
                    <li style="padding-right: 20px;"><a href="#">Design</a></li>
                    <li style="padding-right: 20px;"><a href="#">About</a></li>
                    <li style="padding-right: 20px;"><a href="%s">Login</a></li>
                </ul>
            </nav>
            """ % url
            
        template_values = {
            'specific_urls':specific_urls,
            'nav': nav,
            'content':myFile.read()
        }
       
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_values))


app = webapp2.WSGIApplication([('/', HomePage)], debug=True)
