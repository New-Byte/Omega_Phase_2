'''
Omegalib library to design the layout for android application
Author:             Iron-Legion@GCOEJ
Date:               14 SEPTEMBER 2021
'''

from xml.dom.minidom import Document
import os

def toast(text):
    pass

def link(to,frm):
    pass

class Omega():
    def __init__(self,layout_width="match_parent",layout_height="match_parent"):
        # Create root/parent tag
        self.root = Document()
        self.xml = self.root.createElement('androidx.constraintlayout.widget.ConstraintLayout')
        self.xml.setAttributeNS("xmlns","xmlns:android","http://schemas.android.com/apk/res/android")
        self.xml.setAttributeNS("xmlns","xmlns:app","http://schemas.android.com/apk/res-auto")
        self.xml.setAttributeNS("xmlns","xmlns:tools","http://schemas.android.com/tools")
        self.xml.setAttributeNS("android","android:layout_width",layout_width)
        self.xml.setAttributeNS("android","android:layout_height",layout_height)
        self.xml.setAttributeNS("tools","tools:context",".MainActivity")
        self.root.appendChild(self.xml)

    def run(self):
        xml_str = self.root.toprettyxml(indent ="\n\t")
        save_path_file = "activity_main.xml"
        with open(save_path_file, "w") as f:
            f.write(xml_str)


# The code for all the views.
class AppView():

    def __init__(self,app):
        self.xml = app.xml
        self.root = app.root

    def settext(self, id_, text):
        pass

    def RecycleView(self,**kwargs):
        recycleView_child = self.root.createElement('RecycleView')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            recycleView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(recycleView_child)

    def Switch(self,**kwargs):
        switch_child = self.root.createElement('switch_child')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            switch_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(switch_child)

    def ImageView(self, **kwargs):
        ImageView_child = self.root.createElement('ImageView')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            ImageView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(ImageView_child)


    def TextView(self,**kwargs):
        TextView_child = self.root.createElement('TextView')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            TextView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(TextView_child)

    def View(self,**kwargs):
        View_child = self.root.createElement('View')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            View_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(View_child)

    def ScrollView(self,**kwargs):
        root1 = Document()
        ScrollView_child = root1.createElement('ScrollView')
        ll1 = list(kwargs.items())
        for key, value in ll1[:4]:
            keyword = key.split(":")[0]
            ScrollView_child.setAttributeNS(keyword,key,value)
        LLC = root1.createElement('LinearLayout')
        for key, value in ll1[4:]:
            keyword = key.split(":")[0]
            LLC.setAttributeNS(keyword,key,value)
        ScrollView_child.appendChild(LLC)
        self.root.appendChild(ScrollView_child)

# The code for all the buttons
class Buttons():
    def __init__(self,app):
        self.xml = app.xml
        self.root = app.root

    def ChipGroup(self,**kwargs):
        chipGroup_child = self.root.createElement('ChipGroup')
        for key , value in kwargs.items():
            keyword = key.split(":")[0]
            chipGroup_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(chipGroup_child)

    def Chip(self,**kwargs):
        Chip_child = self.root.createElement('Chip')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            Chip_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(Chip_child)

    def RadioGroup(self,**kwargs):
        RadioGroup_child = self.root.createElement('RadioGroup')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            RadioGroup_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(RadioGroup_child)

    def RadioButton(self,**kwargs):
        RadioButton_child = self.root.createElement('RadioButton')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            RadioButton_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(RadioButton_child)

    def Button(self,**kwargs):
        Button_child = self.root.createElement('Button')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            Button_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(Button_child)

    def ImageButton(self,**kwargs):
        # Button_child = self.root.createElement('Button')
        ImageButton_child = self.root.createElement('ImageButton')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            ImageButton_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(ImageButton_child)
        
    def checkBox(self,**kwargs):
        checkBox_child = self.root.createElement('checkBox')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            checkBox_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(checkBox_child)

    def ToggleButton(self,**kwargs):
        ToggleButton_child = self.root.createElement('ToggleButton')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            ToggleButton_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(ToggleButton_child)

# Code for all the containers.
class Containers():
    def __init__(self,app):
        self.xml = app.xml
        self.root = app.root
        
    def CardView(self,**kwargs):
        CardView_child = self.root.createElement('CardView')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            CardView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(CardView_child)

    def ViewPager2(self,**kwargs):
        ViewPager2_child = self.root.createElement('ViewPager2')
        for key , value in kwargs.items():
            keyword = key.split(":")[0]
            ViewPager2_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(ViewPager2_child)

    def NavigationView(self,**kwargs):
        NavigationView_child = self.root.createElement('NavigationView')
        for key,value in kwargs.items():
            keyword = key.split(":")[0]
            NavigationView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(NavigationView_child)

    def BottamNavigationView(self,**kwargs):
        BottamNavigationView_child = self.root.createElement("BottamNavigationView")
        for key,value in kwargs.items():
            keyword = key.split(":")[0]
            BottamNavigationView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(BottamNavigationView_child)

    def BottamAppBar(self,**kwargs):
        BottamAppBar_child = self.root.createElement("BottamAppBar")
        for key,value in kwargs.items():
            keyword = key.split(":")[0]
            BottamAppBar_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(BottamAppBar_child)

    def ToolBar(self,**kwargs):
        ToolBar_child = self.root.createElement("ToolBar")
        for key,value in kwargs.items():
            keyword = key.split(":")[0]
            ToolBar_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(ToolBar_child)

    def ViewStub(self,**kwargs):
        ViewStub_child = self.root.createElement("ViewStub")
        for key,value in kwargs.items():
            keyword = key.split(":")[0]
            ToolBar_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(ViewStub_child)

    def Spinner(self,**kwargs):
        Spinner_child = self.root.createElement('Spinner')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            Spinner_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(Spinner_child)




# Code for all the widgets like scroll bar, tool bar, etc.
class BarWidget():
    def __init__(self,app):
        self.xml = app.xml
        self.root = app.root

    def Toolbar(self,**kwargs):
        Toolbar_child = self.root.createElement('android.support.v7.widget.Toolbar')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            Toolbar_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(Toolbar_child)
    
# Code for all the TextFields (Input Fileds). 
class TextField():
    def __init__(self,app):
        self.xml = app.xml
        self.root = app.root

    def read(self):
        pass

    def EditText(self,**kwargs): 
        TextInputEditText_child = self.root.createElement('EditText')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            TextInputEditText_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(TextInputEditText_child)

class Widgets():
    def __init__(self,app):
        self.xml = app.xml
        self.root = app.root

    def View(self, **kwargs):
        View_child = self.root.createElement('View')
        for key, value in kwargs.items():
            keyword = key.split(":")[0]
            View_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(View_child)

    def WebView(self,**kwargs):
        WebView_child = self.root.createElement('WebView')
        for key, value in kwargs.item():
            keyword = key.split(":")[0]
            WebView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(WebView_child)

    def VideoView(self,**kwargs):
        VideoView_child = self.root.createElement('VideoView')
        for key, value in kwargs.item():
            keyword = key.split(":")[0]
            VideoView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(VideoView_child)

    def CalenderView(self,**kwargs):
        CalenderView_child = self.root.createElement('CalenderView')
        for key, value in kwargs.item():
            keyword = key.split(":")[0]
            CalenderView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(CalenderView_child)

    # Circular Progress bar
    def ProgressBar(self,**kwargs):
        ProgressBar_child = self.root.createElement('ProgressBar')
        for key,value in kwargs.item():
            keyword = key.split(":")[0]
            ProgressBar_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(ProgressBar_child)

    def SeekBar(self,**kwargs):
        SeekBar_child = self.root.createElement('SeekBar')
        for key,value in kwargs.item():
            keyword = key.split(":")[0]
            SeekBar_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(SeekBar_child)

    def RatingBar(self,**kwargs):
        RatingBar_child = self.root.createElement('RatingBar')
        for key,value in kwargs.item():
            keyword = key.split(":")[0]
            RatingBar_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(RatingBar_child)

    def SearchView(self,**kwargs):
        SearchView_child = self.root.createElement('SearchView')
        for key,value in kwargs.item():
            keyword = key.split(":")[0]
            SearchView_child.setAttributeNS(keyword, key,value)
        self.xml.appendChild(SearchView_child)

class legacy():
    def __int__(self):
        self.xml = app.xml
        self.root = app.root

    def ListView(self,**kwargs):
        ListView_child = self.root.createElement('ListView')
        for key, value in kwargs.item():
            keyword = key.split(":")[0]
            ListView_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(ListView_child)

    def Relative_layout(self,**kwargs):
        Relative_layout_child = self.root.createElement('Relative_layout')
        for key,value in kwargs.item():
            keyword = key.split(":")[0]
            Relative_layout_child.setAttributeNS(keyword,key,value)
        self.xml.appendChild(Relative_layout_child)

class EventListener():
    def onclick(self, id_):
        #call this function in backend to read value
        pass
