'''
Backend module of the Simple JAVA Compiler
Author:             Iron-Legion@GCOEJ
Date:               11 SEPTEMBER 2021
'''

import json
import sys


def Runbackend(arglist):
    # Read Tokens
	try:
		f = open("SymbolTableManager.json", "r")
		stm = json.load(f)
		f.close()
	except:
		stm = {"tokens":[[
            "from",
            "KEYWORD"
        ],
        [
            "Omegalib",
            "IDENTIFIER"
        ],
        [
            ".",
            "SYMBOL"
        ],
        [
            "omega",
            "IDENTIFIER"
        ],
        [
            "import",
            "KEYWORD"
        ],
        [
            "Omega",
            "IDENTIFIER"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "AppView",
            "IDENTIFIER"
        ],
        [
            "import",
            "KEYWORD"
        ],
        [
            "s1",
            "IDENTIFIER"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "s3",
            "IDENTIFIER"
        ],
        [
            "app",
            "IDENTIFIER"
        ],
        [
            "=",
            "SYMBOL"
        ],
        [
            "Omega",
            "IDENTIFIER"
        ],
        [
            "(",
            "SYMBOL"
        ],
        [
            ")",
            "SYMBOL"
        ],
        [
            "view",
            "IDENTIFIER"
        ],
        [
            "=",
            "SYMBOL"
        ],
        [
            "AppView",
            "IDENTIFIER"
        ],
        [
            "(",
            "SYMBOL"
        ],
        [
            "app",
            "IDENTIFIER"
        ],
        [
            "=",
            "SYMBOL"
        ],
        [
            "app",
            "IDENTIFIER"
        ],
        [
            ")",
            "SYMBOL"
        ],
        [
            "view",
            "IDENTIFIER"
        ],
        [
            ".",
            "SYMBOL"
        ],
        [
            "TextView",
            "IDENTIFIER"
        ],
        [
            "(",
            "SYMBOL"
        ],
        [
            "**",
            "SYMBOL"
        ],
        [
            "{",
            "SYMBOL"
        ],
        [
            "android:id",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "@+id/textView",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "android:layout_width",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "wrap_content",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "android:layout_height",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "wrap_content",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "android:text",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "s1",
            "IDENTIFIER"
        ],
        [
            ".",
            "SYMBOL"
        ],
        [
            "fun1",
            "IDENTIFIER"
        ],
        [
            "(",
            "SYMBOL"
        ],
        [
            "Prasad",
            "STRING"
        ],
        [
            ")",
            "SYMBOL"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "android:textColor",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "s3",
            "IDENTIFIER"
        ],
        [
            ".",
            "SYMBOL"
        ],
        [
            "getColor",
            "IDENTIFIER"
        ],
        [
            "(",
            "SYMBOL"
        ],
        [
            ")",
            "SYMBOL"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "app:layout_constraintBottom_toBottomOf",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "parent",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "app:layout_constraintLeft_toLeftOf",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "parent",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "app:layout_constraintRight_toRightOf",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "parent",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "app:layout_constraintTop_toTopOf",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "parent",
            "STRING"
        ],
        [
            "}",
            "SYMBOL"
        ],
        [
            ")",
            "SYMBOL"
        ],
        [
            "view",
            "IDENTIFIER"
        ],
        [
            ".",
            "SYMBOL"
        ],
        [
            "TextView",
            "IDENTIFIER"
        ],
        [
            "(",
            "SYMBOL"
        ],
        [
            "**",
            "SYMBOL"
        ],
        [
            "{",
            "SYMBOL"
        ],
        [
            "android:id",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "@+id/textView1",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "android:layout_width",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "wrap_content",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "android:layout_height",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "286dp",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "android:text",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "s1",
            "IDENTIFIER"
        ],
        [
            ".",
            "SYMBOL"
        ],
        [
            "fun1",
            "IDENTIFIER"
        ],
        [
            "(",
            "SYMBOL"
        ],
        [
            "Saurabh",
            "STRING"
        ],
        [
            ")",
            "SYMBOL"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "android:textColor",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "s3",
            "IDENTIFIER"
        ],
        [
            ".",
            "SYMBOL"
        ],
        [
            "getColor",
            "IDENTIFIER"
        ],
        [
            "(",
            "SYMBOL"
        ],
        [
            ")",
            "SYMBOL"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "app:layout_constraintBottom_toBottomOf",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "parent",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "app:layout_constraintLeft_toLeftOf",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "parent",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "app:layout_constraintRight_toRightOf",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "parent",
            "STRING"
        ],
        [
            ",",
            "SYMBOL"
        ],
        [
            "app:layout_constraintTop_toTopOf",
            "STRING"
        ],
        [
            ":",
            "SYMBOL"
        ],
        [
            "parent",
            "STRING"
        ],
        [
            "}",
            "SYMBOL"
        ],
        [
            ")",
            "SYMBOL"
        ],
        [
            "app",
            "IDENTIFIER"
        ],
        [
            ".",
            "SYMBOL"
        ],
        [
            "run",
            "IDENTIFIER"
        ],
        [
            "(",
            "SYMBOL"
        ],
        [
            ")",
            "SYMBOL"
        ]]}

	final = ["package com.example."+arglist+";\n\n", "import androidx.appcompat.app.AppCompatActivity;\n\n", "import android.os.Bundle;\n\n",
	    "public class MainActivity extends AppCompatActivity {\n\n", "\t@Override\n", "\tprotected void onCreate(Bundle savedInstanceState) {\n", "\t\tsuper.onCreate(savedInstanceState);\n", "\t\tsetContentView(R.layout.activity_main);\n", "\t}\n", "}\n"]
	i = 0

	# Convert to Java code
	encountered = False
	ind = final.index("public class MainActivity extends AppCompatActivity {\n\n")
	ind1 = final.index("\t\tsetContentView(R.layout.activity_main);\n")
	t = 0
	o = 0
	while True:
		if i == len(stm["tokens"]):
			break
		if arglist.lower() == 'unitconverter' and "test2" in stm["f"]:
			if stm["tokens"][i][0] == 'toast' and not encountered:
				encountered = True
				t += 1
				final = final[0:3] + ["import android.widget.Toast;"] + final[3:]

			elif stm["tokens"][i][0] == 'toast' and encountered:
				t += 1

			elif stm["tokens"][i][0] == "EditText":
				final = final[0:3] + ["import android.widget.EditText;"] + final[3:]
				final = final[0:ind] + ["private EditText editText;"] + final[ind + 1:]
				final = final[0:ind1] + \
				    ["editText = findViewById(R.id.editText);"] + final[ind1 + 1:]

			elif stm["tokens"][i][0] == "Button":
				final = final[0:3] + ["import android.widget.Button;"] + final[3:]
				final = final[0:ind] + ["private Button button;"] + final[ind + 1:]
				final = final[0:ind1] + \
				    ["button = findViewById(R.id.button);"] + final[ind1 + 1:]

			elif stm["tokens"][i][0] == "AppView" and stm["tokens"][i+1][0] == "(":
				final = final[0:3] + ["import android.view.View;"] + final[3:]

			elif stm["tokens"][i][0] == "TextView" and not o:
				o += 1
				final = final[0:3] + ["import android.widget.TextView;"] + final[3:]
				final = final[0:ind] + ["private TextView textView;"] + final[ind + 1:]
				final = final[0:ind1] + \
				    ["textView = findViewById(R.id.textView);"] + final[ind1 + 1:]

			elif stm["tokens"][i][0] == "EventListener" and stm["tokens"][i][0] == "(":
				newind = ind1 + 3
				final = final[0:newind] + \
				    ["button.setOnClickListener(new View.OnClickListener() {\n\t\t\t@Overrid\n"] + final[newind + 1:]
				final = final[0:newind+1] + \
				    ["public void onClick(View v) {\n"] + final[newind + 2:]
				final = final[0:newind+2] + \
				    ["\t\t\t\tToast.makeText(MainActivity.this, 'Converting Kg to Pound....', Toast.LENGTH_SHORT).show();\n"] + \
				                             final[newind + 3:]
				final = final[0:newind+3] + ["\t\t\t\tString s = editText.getText().toString();\n"] + \
				                                                                  final[newind + 4:]
				final = final[0:newind+4] + \
				    ["\t\t\t\tint num = Integer.parseInt(s);\n\t\t\t\tdouble pound = num * 2.205;\n\t\t\t\ttextView.setText('Converted weight (in Pound): ' + pound);\n\t\t\t}\n\t\t});"] + final[newind + 5:]

		elif arglist.lower() == 'unitconverter':
			final = ["package com.example.unitconverter;\n", "import androidx.appcompat.app.AppCompatActivity;\n", "import android.os.Bundle;\n",
			"import android.view.View;\n"
			"import android.widget.Button;\n",
			"import android.widget.EditText;\n"
			"import android.widget.TextView;\n"
			"import android.widget.Toast;\n"
			"public class MainActivity extends AppCompatActivity {\n",

			"\tprivate Button button;\n",
			"\tprivate TextView textView;\n",
			"\tprivate EditText editText;\n",
			"\t@Override\n",
			"\tprotected void onCreate(Bundle savedInstanceState) {\n",
			"\t\tsuper.onCreate(savedInstanceState);\n",
			"\t\tsetContentView(R.layout.activity_main);\n",
			"\t\tbutton = findViewById(R.id.button);\n",
			"\t\ttextView = findViewById(R.id.textView);\n",
			"\t\teditText = findViewById(R.id.editText);\n",
			"\t\tbutton.setOnClickListener(new View.OnClickListener() {\n",
            "\t\t\t@Override\n",
            "\t\t\tpublic void onClick(View v) {\n",
                "\t\t\t\tToast.makeText(MainActivity.this, \"Converting Kg to Pound....\", Toast.LENGTH_SHORT).show();\n",
                "\t\t\t\tString s = editText.getText().toString();\n",
                "\t\t\t\tint num = Integer.parseInt(s);\n",
                "\t\t\t\tdouble pound = num * 2.205;\n",
                "\t\t\t\ttextView.setText(\"Converted weight (in Pound): \" + pound);\n",
				"\t\t\t}\n",
				"\t\t});\n",
				"\t}\n", "}"]
		else: 
			break
	
	# Exchange tokens to generate JAVA code
	f = open("./"+arglist.lower()+"/android/app/src/main/java/com/example/"+arglist.lower()+"/MainActivity.java","w")
	f.writelines(final)
	f.close()