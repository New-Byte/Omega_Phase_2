# Omega
Android Application developement framework for python
## Getting Started
### Install omegalib for python
1. Download this repository.
```
git clone https://github.com/New-Byte/Omega.git
```
2. Change your directory.
```
cd Omega\Lib\dist
```
3. Install omegalib
```
pip install library_wheel_file_name.whl
```
#### You can delete the repository after installation if you want.

## About Omegalib
Omegalib is the library that we design to develope the layout for android application. Omegalib has vast functionalities to create interactive application frontend. Some of the examples are given below.

##### 1. Create Omega object
```
from Omegalib import omega as og

app = og.Omega()
```

##### 2. Create TextView
```
# Create AppView object
view = og.AppView(app=app)

kwargs = {"android:id":"@+id/textView","android:layout_width":"wrap_content","android:layout_height":"wrap_content","android:text":"Prasad","android:textColor":"#000", "app:layout_constraintBottom_toBottomOf":"parent","app:layout_constraintLeft_toLeftOf":"parent","app:layout_constraintRight_toRightOf":"parent","app:layout_constraintTop_toTopOf":"parent"}

view.TextView(**kwargs)
# Run application
app.run()
```
## About OmegaCompiler
It is a program that will generate a Java code to develope an android application.

## Componants of compiler
### 1. Scanner
It scans the python program and generates the tokens for it using lexical analysis. It removes comments, whitespaces from program. These tokens are then added to symboletablemanager.txt file.
#### Run Scanner
```
cd Omega\OmegaCompiler\modules
```
```
python scanner.py ..\..\test\test.py
```
