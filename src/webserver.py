import tinyweb
import lights
import display
# Create web server application
app = tinyweb.webserver()


# Index page
@app.route('/')
@app.route('/index.html')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.send_file('wwwroot/index.html')


@app.route('/css/<fn>')
async def images(req, resp, fn):
    # Send picture. Filename - in parameter
    await resp.send_file('wwwroot/css/{}'.format(fn),
                         content_type='text/css')


class All():
    def put(self, data):
        print(data)
        lights.all((data[0], data[1], data[2]))
        return {'message': 'changed'}


class Light():
    def put(self, data):
        print(data)
        lights.light(int(data['nr']), (data['rgb'][0],
                                       data['rgb'][1], data['rgb'][2]))
        return {'message': 'changed'}


def start(ip):
    app.add_resource(All, '/all')
    app.add_resource(Light, '/light')
    display.printip(ip)
    app.run(host=ip, port=80)
