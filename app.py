from flask import Flask
##WSGI APPLICATION
app=Flask(__name__)

@app.route('/')
def welcome():
   return "WELCOME TO MY YOUTUBE CHANNEL..."
@app.route('/members')
def members():
   return "WELCOME TO YOUTUBE CHANNEL MEMBERS"

if __name__=='__main__':
   app.run(debug=True)