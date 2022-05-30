@echo off
set var=%1
set app_name=%2
if [%var%]==[] (echo run omega --help) else (
		if "%var%"=="--help" (echo Create the project using "omega createapp app_name" and then run "omega manage.py --help") else (
				if "%var%"=="version" (echo 0.0.6) else (
							if "%var%"=="createapp" (
								git clone https://github.com/New-Byte/Android_Template.git
								cd ./Android_Template/
								python ./manage.py create %app_name%
								cd ..
								ren Android_Template %app_name%
								) else (echo Enter a valid command)
					)
			)
	)