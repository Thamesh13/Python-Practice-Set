from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

# Application
@app.route('/')
def hello_world():
   return 'Hello World!'

if __name__ == '__main__':
   app.run()
   
#----------------------------------------

# Variable Rules
# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name

# if __name__ == '__main__':
#    app.run(debug = True)
   
# ------------------------------------------------

# URL Binding
# @app.route('/admin')
# def hello_admin():
#    return 'Hello Admin'

# @app.route('/guest/<guest>')
# def hello_guest(guest):
#    return 'Hello %s as Guest' % guest

# @app.route('/user/<name>')
# def hello_user(name):
#    if name =='admin':
#       return redirect(url_for('hello_admin'))
#    else:
#       return redirect(url_for('hello_guest',guest = name))

# if __name__ == '__main__':
#    app.run(debug = True) 

# -----------------------------------------------------------

# Templates 01
# @app.route('/')
# def index():
#    return '<html><body><h1>Hello World</h1></body></html>'

# if __name__ == '__main__':
#    app.run(debug = True)

# -----------------------------------------------------------------------

# Template 02
# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('hello_user.html', name = user)

# if __name__ == '__main__':
#    app.run(debug = True)
   
#  -----------------------------------------------------------------------

# Template 03
# @app.route('/hello/<int:score>')
# def hello_name(score):
#    return render_template('hello.html', marks = score)

# if __name__ == '__main__':
#    app.run(debug = True)

# ------------------------------------------------------------------------

# Template 04
# @app.route('/result')
# def result():
#    dict = {'physics':50,'chemistry':60,'maths':70}
#    return render_template('result.html', result = dict)

# if __name__ == '__main__':
#    app.run(debug = True)
   
# --------------------------------------------------------------------------

# Static
# @app.route("/")
# def index():
#    return render_template("index.html")

# if __name__ == '__main__':
#    app.run(debug = True)

# ---------------------------------------------------------------------------

# sending form to template
# @app.route('/')
# def student():
#    return render_template('student.html')

# @app.route('/result',methods = ['POST', 'GET'])
# def result():
#    # The results() function collects form data present in request.form in a dictionary object and sends it for rendering to result.html.
#    if request.method == 'POST':
#       result = request.form
#       return render_template("result.html",result = result)

# if __name__ == '__main__':
#    app.run(debug = True)