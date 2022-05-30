# import Modules
from Omegalib.omega import Omega,AppView
import s1, s3

''' 
Create application
'''
app = Omega()

# Create view
view = AppView(app=app)

view.TextView(**{"android:id":"@+id/textView1","android:layout_width":"wrap_content","android:layout_height":"286dp","android:text":s1.fun1("UnitConverter"),"android:textColor":s3.getColor(), "app:layout_constraintBottom_toBottomOf":"parent","app:layout_constraintLeft_toLeftOf":"parent","app:layout_constraintRight_toRightOf":"parent","app:layout_constraintTop_toTopOf":"parent"})

app.run()