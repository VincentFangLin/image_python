import web
import dbLogic
from ImageProcessApp import ImageProcessApp
web.config.debug = False
urls = (
    '/', 'Home',
    '/login/', 'Login',
    '/logout/', 'Logout',
    '/registration/', 'Registration',
    '/mainmenu/', 'MainMenu',
    '/imageprocess/','ImageProcess'
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('session'))
globals = {'session': session}
render = web.template.render('webUI/', globals=globals, base='base')

class ImageProcess:
    def GET(self):
        inputData = web.input()
        print('----inputData--1-')
        print(inputData)
        if inputData.get('imageprocess') == 'start':
            print("----------------------------------------------------------")

            imageProcessApp = ImageProcessApp("C:/Users/Vibrant/Desktop/Scanned Plate/CVTG80010001000072/TileScan 1/","C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif")
            imageProcessApp.run()
        raise web.seeother('/mainmenu/')
    
    def POST(self):
        inputData = web.input()
        print('----inputData--2-')
        print(inputData)

class Home:
    def GET(self):
        if session.get('username'):
            raise web.seeother('/mainmenu/')
        else:
            return render.login()
class MainMenu:
    def GET(self):
        if session.get('username'):
            first_name, last_name, nickname = dbLogic.getUserNames(session.username)
            return render.mainmenu( first_name, last_name, nickname)
        else:
            raise render.login()

class Login:
    def GET(self):
        raise web.seeother('/')

    def POST(self):
        inputData = web.input()

        if dbLogic.isUser(inputData.username, inputData.password):
            session.loginMessage = 'Login Succeeds!'
            results = dbLogic.emailOrNickname(inputData.username)
            session.username, session.nickname = results
            print(results)
            raise web.seeother('/mainmenu/')
        else:
            session.loginMessage = 'User or Password Not Found!'
            raise web.seeother('/login/')


class Logout:
    def GET(self):
        if session:
            session.kill()
        raise web.seeother('/login/')
          
class Registration:
    def GET(self):
        return render.registration()

    def POST(self):
        inputData = web.input()
        if dbLogic.emailExists(inputData.email) or dbLogic.nicknameExists(inputData.nickname):
            session.registrationMessage = 'Email or Nickname Exists'
            raise web.seeother('/registration/')
        elif dbLogic.insertUser(inputData.email,
                                inputData.firstname,
                                inputData.lastname,
                                inputData.password,
                                inputData.nickname):
            session.registrationMessage = 'Registration is successful!'
            session.username = inputData.email
            raise web.seeother('/mainmenu/')
        else:
            session.registrationMessage = 'Registration is not Successful!'
            raise web.seeother('/registration/')
if __name__ == "__main__":
    app.run()