import web
from time import strftime

urls = (
  '/(\d\d?)', 'Hora'
)

class Hora:        
    def GET(self, fmt):
        if fmt == '12':
            visor = '%I:%M:%S %p'
        else:
            visor = '%H:%M:%S'
        print '<h1>%s</h1>' % strftime(visor)

web.run(urls, globals())

