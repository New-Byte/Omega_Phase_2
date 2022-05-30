from omega import Omega,AppView

app = Omega()
view = AppView(app=app)

view.TextView(text="Hello,Prasad Joshi")
app.run()