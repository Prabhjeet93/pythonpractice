import webbrowser
# open form.html file in write-only mode
# it will automatically create the file
# if it is not exist
file = open("form.html", "w")
# write the html code
html_code = """<!DOCTYPE html>
<!--   COMMENT IN HTML File -->
NEW FORM 
<head>      
<title>Log In form</title> <!-- Title of the form -->
<link rel="stylesheet", href="style.css">
</head>
<body>  <!-- Start Body -->
<form action="action_page.php" method="post">
  <div class="container">
    <img src="images/logo_img.png"" alt="log" class="logo">
  </div>
  <div class="container">
    <label for="uname"><b>Username:</b></label>
    <input type="text" placeholder="Enter your username" name="uname" required>
    <br>
    <label for="pswdd"><b>Password:</b></label>
    <input type="password" placeholder="Enter your password" name="passwd" required>
    <br>
    <label>
      <input type="checkbox" name="remember"> Remember me
    </label>
    <br>
    <button type="submit">Login</button>
    <br>
    <span class="pswd">Forgot <a href="#">password?</a></span>
  </div>
</form>
</body>
</html>"""
file1 = open("style.css", "w")
# write the css code
css_code = """
form {
  border: 3px solid black;
}
input[type=text], input[type=password] {
  width: 40%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}
button {
  background-color: #4CAF50;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 18%;
}
button:hover {
  opacity: 0.8;
}
.container {
  text-align: center;
  margin: 24px 0 12px 0;
}
img.logo {
  width: 22%;
  border-radius: 50%;
}
.container {
  padding: 16px;
}
}
"""
# write the html code in form.html file
file.write(html_code)
# write the css code in form.html file
file1.write(css_code)
# close the files
file.close()
file1.close()
#open the form in new tab of browser
webbrowser.open_new_tab("form.html")
