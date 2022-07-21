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
    '/imageprocess/','ImageProcess',
    '/results/','Results'

)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('session'))
globals = {'session': session}
render = web.template.render('webUI/', globals=globals, base='base')

class Results:
    def GET(self):
        return render.results()
class ImageProcess:

    def cookDic(self,position_and_data_Dic,chip_coord_and_ROI_idx_dic):
        new_position_and_data_Dic = {}
        for position,data in position_and_data_Dic.items():
            position_idx = position.split('_')[1]
            position_name = position.split('_')[0]
            ROI_list = chip_coord_and_ROI_idx_dic[position_name]
            print("-=-=-=ROI_list-=-=-=-=")
            print(ROI_list)
            if int(position_idx) in ROI_list:
                new_position = position + '_T'
            else:
                new_position = position + '_F'

            new_position_and_data_Dic[new_position] = position_and_data_Dic[position]
        print("-=-=-=-=-=-=-=")
        print(new_position_and_data_Dic)
        return new_position_and_data_Dic
    def GET(self):
        inputData = web.input()
        print('----inputData--1-')
        print(inputData)
        if inputData.get('imageprocess') == 'start':
            print("----------------------------------------------------------")

            imageProcessApp = ImageProcessApp("C:/Users/Vibrant/Desktop/Scanned Plate/CVTG80010001000072/TileScan 1/","C:/Users/Vibrant/Desktop/openCV/anti_clockwise_rotate/img0.tif")
            position_and_data_Dic,chip_coord_and_ROI_idx_dic = imageProcessApp.run()
            position_and_data_Dic = self.cookDic(position_and_data_Dic,chip_coord_and_ROI_idx_dic)

        return render.results(True,position_and_data_Dic)
    
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