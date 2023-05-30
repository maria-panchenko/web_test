from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

loginlist = []
passwordlist = []

def login1(login):
    for i in loginlist:
        if i == login:
            return login
        else:
            return "Error"


def password1(password):
    for i in passwordlist:
        if i == password:
            return password
        else:
            return "Error"

def morgernshern(login, password):
    if login1(login) and password1(password):
        return render_template('da.html')
    else:
        return "error"

@app.route('/', methods=['post', 'get'])
def form():
    file1 = open("logins.txt","r")
    file2 = open("passwords.txt", "r")
    loginlist = file1.readlines()
    passwordlist = file2.readlines()
    file1.close()
    file2.close()
    if request.method == 'POST':
        str = ""
        login = request.form.get('login')
        password = request.form.get('password')
        morgernshern(login,password)


if __name__ == "__main__":
    app.run(debug=True)