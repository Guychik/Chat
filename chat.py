from flask import *
app = Flask(__name__)
app.secret_key = "super secret key"
import websockets 

@app.route('/', methods=['GET', 'POST']) 
def login(): 
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == "a" and password == "a":
            return redirect(url_for('chatroom'))
        else:
            flash('Please sign up before!')
            return redirect(url_for('signup'))

    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup(): 
    return render_template('signup.html')

@app.route('/chatroom', methods=['GET', 'POST']) 
def chatroom(): 
    if request.method == 'POST':
        input = request.form.get('input')
        websocket = websockets.connect("ws://localhost:800")
        websocket.send(input)

    # create public key
    return render_template('chatroom.html')

if __name__ == "__main__":
    app.run()
    

    
    
    