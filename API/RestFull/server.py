#Parte del codigo fue reescrito y adapatado de los videos
# https://www.youtube.com/watch?v=s105UdO6nVQ
# https://www.youtube.com/watch?v=m2NRZimOIWg

#La parte de la autenticacion fue adapatada de aqui:
#https://gist.github.com/dragermrb/108158f5a284b5fba806#file-server-py-L20



from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

# import CRUD Operations ##
from database_setup import Base, CyclingTeam, Cyclist
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json
import base64

# Create session and connect to DB ##
engine = create_engine('sqlite:///franceTour.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):

    def do_OPTIONS(self): #CORS HEADERS
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
        self.send_header("Access-Control-Allow-Headers", "x-api-key")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Access-Control-Allow-Headers", "Authorization")
        self.end_headers()

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header(
            'WWW-Authenticate', 'Basic realm="Demo Realm"')
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        key = self.get_auth_key()
        try:
            if self.headers.get('Authorization') == None:
                self.do_AUTHHEAD()

                response = {
                    'success': False,
                    'error': 'No auth header received'
                }

                self.wfile.write(bytes(json.dumps(response), 'utf-8'))

            elif self.headers.get('Authorization') == 'Basic ' + str(key):
                if self.path.endswith("/cycling_teams/new"):
                    print(">> New!!!")
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output = ""
                    output += "<html><body>"
                    output += "<h1>Make a New Cycling Team</h1>"
                    output += "<form method = 'POST' enctype='multipart/form-data' action = '/cycling_teams/new'>"
                    output += "<input name = 'newCyclingTeamName' type = 'text' placeholder = 'New Cycling Team Name' required ><br/><br/> "
                    output += "<input name = 'newCyclingTeamVictories' type = 'number' placeholder = 'New Cycling Team Victories' required ><br/><br/> "
                    output += "<input type='submit' value='Create'>"
                    output += "</form></html></body>"
                    self.wfile.write(bytes(output, "utf-8"))
                    return
                if self.path.endswith("/edit"):
                    cyclingTeamIDPath = self.path.split("/")[2]
                    myCyclingTeamQuery = session.query(CyclingTeam).filter_by(
                        id=cyclingTeamIDPath).one()
                    if myCyclingTeamQuery:
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        output = "<html><body>"
                        output += "<h1>"
                        output += myCyclingTeamQuery.name
                        output += "</h1>"
                        output += "<form method='POST' enctype='multipart/form-data' action = '/cycling_teams/%s/edit' >" % cyclingTeamIDPath
                        output += "<input name = 'newCyclingTeamName' type='text' value = '%s' required>" % myCyclingTeamQuery.name
                        output += "<input name = 'newCyclingTeamVictories' type = 'number' value = '%d' required><br/><br/> " % myCyclingTeamQuery.victories
                        output += "<input type = 'submit' value = 'Rename'>"
                        output += "</form>"
                        output += "</body></html>"
                        self.wfile.write(bytes(output, "utf-8"))

                if self.path.endswith("/delete"):
                    cyclingTeamIDPath = self.path.split("/")[2]

                    myCyclingTeamQuery = session.query(CyclingTeam).filter_by(
                        id=cyclingTeamIDPath).one()
                    if myCyclingTeamQuery:
                        self.send_response(200)
                        self.send_header('Content-type', 'text/html')
                        self.end_headers()
                        output = ""
                        output += "<html><body>"
                        output += "<h1>Are you sure you want to delete %s?" % myCyclingTeamQuery.name
                        output += "<form method='POST' enctype = 'multipart/form-data' action = '/cycling_teams/%s/delete'>" % cyclingTeamIDPath
                        output += "<input type = 'submit' value = 'Delete'>"
                        output += "</form>"
                        output += "</body></html>"
                        self.wfile.write(bytes(output, "utf-8"))

                if self.path.endswith("/cycling_teams"):
                    teams = session.query(CyclingTeam).all()
                    print("%%%%%%%%%")
                    output = ""
                    output += "<a href = '/cycling_teams/new'> Make a New Cycling Team Here </a></br></br>"
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    output += "<html><body>"
                    for team in teams:
                        output += team.name
                        output += "</br>"
                        output += "<a href ='/cycling_teams/%s/edit' >Edit </a> " % team.id
                        output += "</br>"
                        output += "<a href ='/cycling_teams/%s/delete'> Delete </a>" % team.id
                        output += "</br></br></br>"
                    output += "</body></html>"
                    self.wfile.write(bytes(output, "utf-8"))
                    return 

        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


    def do_POST(self):
        key = self.get_auth_key()
        try:
            if self.headers.get('Authorization') == None:
                self.do_AUTHHEAD()

                response = {
                    'success': False,
                    'error': 'No auth header received'
                }

                self.wfile.write(bytes(json.dumps(response), 'utf-8'))

            elif self.headers.get('Authorization') == 'Basic ' + str(key):
                if self.path.endswith("/delete"):
                    cyclingTeamIDPath = self.path.split("/")[2]
                    myCyclingTeamQuery = session.query(CyclingTeam).filter_by(
                        id=cyclingTeamIDPath).one()
                    if myCyclingTeamQuery != []:
                        session.delete(myCyclingTeamQuery)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/cycling_teams')
                        self.end_headers()

                if self.path.endswith("/edit"):
                    ctype, pdict = cgi.parse_header(self.headers.get('content-type'))                
                    pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                    pdict['CONTENT-LENGTH'] = int(self.headers['Content-Length'])
                    if ctype == 'multipart/form-data':
                        fields = cgi.parse_multipart(self.rfile, pdict)
                        name = fields.get('newCyclingTeamName')
                        victories = fields.get('newCyclingTeamVictories')
                        cyclingTeamIDPath = self.path.split("/")[2]

                        myCyclingTeamQuery = session.query(CyclingTeam).filter_by(
                            id=cyclingTeamIDPath).one()
                        if myCyclingTeamQuery != []:
                            myCyclingTeamQuery.name = name[0]
                            myCyclingTeamQuery.victories = victories[0]
                            session.add(myCyclingTeamQuery)
                            session.commit()
                            self.send_response(301)
                            self.send_header('Content-type', 'text/html')
                            self.send_header('Location', '/cycling_teams')
                            self.end_headers()


                if self.path.endswith("/cycling_teams/new"):
                    print(">> POST NEW")
                    ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
                    pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
                    pdict['CONTENT-LENGTH'] = int(self.headers['Content-Length'])
                    if ctype == 'multipart/form-data':
                        fields = cgi.parse_multipart(self.rfile, pdict)
                        name = fields.get('newCyclingTeamName')
                        victories = fields.get('newCyclingTeamVictories')
                        newCyclingTeam = CyclingTeam(name=name[0], victories=victories[0])
                        session.add(newCyclingTeam)
                        session.commit()
                        self.send_response(301)
                        self.send_header('Content-type', 'text/html')
                        self.send_header('Location', '/cycling_teams')
                        self.end_headers()

        except:
            pass

    def get_auth_key(self):
        return self.server.key


def set_auth(username, password):
        key = base64.b64encode(
            bytes('%s:%s' % (username, password), 'utf-8')).decode('ascii')
        return key

def main():
    try:
        server = HTTPServer(('', 8080), webServerHandler)
        print ('Web server running...open localhost:8080/cycling_teams in your browser')
        server.key = set_auth('sebas', 'Sebas')
        server.serve_forever()
    except KeyboardInterrupt:
        print ('^C received, shutting down server')
        server.socket.close()

if __name__ == '__main__':
    main()