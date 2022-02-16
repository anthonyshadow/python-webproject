import web


#Routes for Url to run 
urls = (
    '/(.*)', 'index'
)

#substantiate the app
app = web.application(urls, globals())

class index: 
    def GET(self, name):
        return "<h1>Hello, "+ name + "how are you today?</h1>"

if __name__ == "__main__":
    app.run()