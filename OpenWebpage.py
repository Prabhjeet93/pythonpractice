import codecs
import webbrowser
NewPage = open('gfg.html','w')

# html_template = """
#                 <!DOCTYPE html>
# <!--   COMMENT IN HTML File -->
# NEW FORM 
# <head>      
# <title>Log In form</title> <!-- Title of the form -->
# <link rel="stylesheet", href="style.css">
# </head>
# <body>  <!-- Start Body -->
# <form action="action_page.php" method="post">
#   <div class="container">
#     <img src="images/logo_img.png"" alt="log" class="logo">
#   </div>
#   <div class="container">
#     <label for="uname"><b>Username:</b></label>
#     <input type="text" placeholder="Enter your username" name="uname" required>
#     <br>
#     <label for="pswdd"><b>Password:</b></label>
#     <input type="password" placeholder="Enter your password" name="passwd" required>
#     <br>
#     <label>
#       <input type="checkbox" name="remember"> Remember me
#     </label>
#     <br>
#     <button type="submit">Login</button>
#     <br>
#     <span class="pswd">Forgot <a href="#">password?</a></span>
#   </div>
# </form>
# </body>
# </html>
# """


NewPage.write(html_template)
NewPage.close()
file = codecs.open('form.html','r','utf-8')
print(file.read())
webbrowser.open_new_tab('form.html')
