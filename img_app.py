# from image_processing import *
import web, db, hashlib, datetime

web.config.debug = True
urls = (
    '/', 'Index',
   '/login/', 'Login',
    '/logout/', 'Logout',
    '/home/', 'Home'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('session'))
globals = {'session':session}
render = web.template.render('templates/', globals=globals, base='base')
renderNoBase = web.template.render('templates/', globals=globals)

class Index:
    def GET(self):
        if session.get('username'):
            raise web.seeother('/home/')
        else:
            return render.index()
class Home:
    def GET(self):
        if session.get('username'):
            return render.home()
        else:
            raise web.seeother('/')

class Logout:
    def GET(self):
        if session:
            session.kill()

        raise web.seeother('/')

class Login:
    def GET(self):
        raise web.seeother('/')

    def POST(self):
        inputData = web.input()
        print(inputData)
        if db.isUserExists(inputData.username, inputData.password):
            session.loginMessage = None
            print("-----------------------------")
            print(inputData.username)
            session.username = inputData.username
            raise web.seeother('/home/')
        else:
            session.loginMessage = 'User / Password combination not found!'
            raise web.seeother('/')


if __name__ == "__main__":
    app.run()
