import web

urls = (
  '/(.*)', 'BomDia'
)

class BomDia:        
    def GET(self, nome):
        params = web.input(vezes=1)
        if nome: 
            msg = 'Bom dia, %s!' % nome
        else:
            msg = 'Bom dia!'
        for i in range(int(params.vezes)):
            print '<h1>%s</h1>' % msg

web.run(urls, globals())

