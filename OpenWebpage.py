import codecs
import webbrowser
NewPage = open('gfg.html','w')

html_template = """
                "<html> " 
                "<head> </head>
<body>
<p> we are in python class</p>
<p> Canada to USA </p>
</body>
</html>
"""


NewPage.write(html_template)
NewPage.close()
file = codecs.open('demo.html','r','utf-8')
print(file.read())
webbrowser.open_new_tab('demo.html')
