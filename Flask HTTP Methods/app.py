from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm'] 
      print('Hi')
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
    #   Here, args is dictionary object containing a list of pairs of form parameter and its corresponding value.
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run(debug = True)