from Omegalib import omega as og

app = og.Omega()
view = og.AppView(app=app)
view.TextView(text="Prasad Joshi")
app.run()

'''
Some paragraph
'''
#for loop starts here...
for i in range(10):
	print(i + 1)
print("Done")