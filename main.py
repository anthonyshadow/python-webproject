import web


#Routes for Url to run 
urls = (
    '/(.*)/(.*)', 'index'
)

#where to find templates
render = web.template.render("resources/")

#substantiate the app
app = web.application(urls, globals())

class index: 
    def GET(self, name, age):
        return render.main(name, age)

if __name__ == "__main__":
    app.run()