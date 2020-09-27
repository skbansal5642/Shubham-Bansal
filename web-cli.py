#!/usr/bin/python3

print("content-type:text/html \n")
print("""
	<html>

	<head>
		<title>Don't look at title</title>
	</head>

	<body>

	<form action="/cgi-bin/date.py">
		<h1>Enter the Command:</h1>
		<input type="text" name="command"/>
		<input type="submit" value="Submit">
</form></body></html>
""")
import subprocess as sp
import cgi

form =cgi.FieldStorage()
cmd = form.getvalue("command")

opt = sp.getoutput("sudo " + cmd)

if cmd == "date":
	full_date = list(opt.split())

	print("<h1> Date </h1>")
	print(f"""
	<h3><xmp>
	Day:      {full_date[0]}
	Date:     {full_date[2]}
	Month:    {full_date[1]}
	Year:     {full_date[5]}
	Time:     {full_date[3]}
	Timezome: {full_date[4]}
	</xmp></h3>
	""")
else:
        print(f"<h1> {cmd}: </h1>")
        print(f"""
        <h3><xmp>
{opt}
        </xmp></h3>
        """)

print("""
        <h1> Run Successful </h1>

""")
