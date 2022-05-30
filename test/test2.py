# import Modules
from Omegalib.omega import Omega,AppView,Buttons,TextField
import Omegalib.omega as ol

# Create Front-end
''' 
Create application
'''
app = Omega()

# Create TextField to take input
edittext = TextField(app=app)
edittext.EditText(**{"android:id":"@+id/editText","android:layout_width":"wrap_content","android:layout_height":"wrap_content","android:ems":"10","android:inputType":"number","android:text":"","app:layout_constraintBottom_toBottomOf":"parent","app:layout_constraintEnd_toEndOf":"parent","app:layout_constraintHorizontal_bias":"0.497","app:layout_constraintStart_toStartOf":"parent","app:layout_constraintTop_toTopOf":"parent","app:layout_constraintVertical_bias":"0.228"})
num = edittext.read()

# Create Button
button = Buttons(app=app)
button.Button(**{"android:id":"@+id/button","android:layout_width":"wrap_content","android:layout_height":"wrap_content","android:layout_marginTop":"80dp","android:background":"#6215EC","android:text":"Convert","android:textColor":"#FFFFFF","android:textColorLink":"#171616","android:textSize":"14sp","app:layout_constraintBottom_toBottomOf":"parent","app:layout_constraintEnd_toEndOf":"parent","app:layout_constraintHorizontal_bias":"0.526","app:layout_constraintStart_toStartOf":"parent","app:layout_constraintTop_toBottomOf":"@+id/editText","app:layout_constraintVertical_bias":"0.024"})

# Create view
view = AppView(app=app)

view.TextView(**{"android:id":"@+id/textView2","android:layout_width":"wrap_content","android:layout_height":"wrap_content","android:text":"Enter the weight (in Kg)","android:textColor":"#0C0C0C","android:textSize":"24sp","android:textStyle":"bold","app:layout_constraintBottom_toTopOf":"@+id/editText","app:layout_constraintEnd_toEndOf":"parent","app:layout_constraintHorizontal_bias":"0.498","app:layout_constraintStart_toStartOf":"parent","app:layout_constraintTop_toTopOf":"parent"})

view.TextView(**{"android:id":"@+id/textView","android:layout_width":"wrap_content","android:layout_height":"wrap_content","android:text":"","android:textColor":"#060350","android:textSize":"20sp","app:layout_constraintBottom_toTopOf":"@+id/button","app:layout_constraintEnd_toEndOf":"parent","app:layout_constraintStart_toStartOf":"parent","app:layout_constraintTop_toBottomOf":"@+id/editText"})

# Add Logo
ol.link('drawable','./image1.png')
view.ImageView(**{"android:id":"@+id/imageView","android:layout_width":"259dp","android:layout_height":"307dp","app:layout_constraintBottom_toBottomOf":"parent","app:layout_constraintEnd_toEndOf":"parent","app:layout_constraintStart_toStartOf":"parent","app:layout_constraintTop_toBottomOf":"@+id/button","app:layout_constraintVertical_bias":"0.811","app:srcCompat":"@drawable/image1"})

event = ol.EventListener()

# Backend Function
def convert(num, view):
	event.onclick("button")
	ol.toast("Converting Kg to Pound....")
	return view.settext("textView","Converted weight (in Pound):  " + str(num * 2.205))

app.run()