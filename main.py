import os
os.system("pip3 install flask")
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pqc')
def pqc():
    return render_template('pqc.html')

@app.route('/sih23')
def sih23():
    return render_template('sih23.html')

@app.route('/nocaine')
def nocaine():
    return render_template('nocaine.html')

@app.route('/gym_reg')
def gym_reg():
    return render_template('gym_reg.html')

@app.route('/spider-vpn')
def spider_vpn():
    return render_template('spider-vpn.html')

@app.route('/olympus')
def olympus():
    return render_template('olympus.html')

@app.route('/sportsfete')
def sportsfete():
    return render_template('sportsfete.html')

@app.route('/profnitt')
def profnitt():
    return render_template('profnitt.html')

@app.route('/chaosbank')
def chaosbank():
    return render_template('chaosbank.html')

@app.route('/embedded-project')
def embedded_project():
    return render_template('embedded-project.html')

@app.route('/AIML')
def AIML():
    return render_template('AIML.html')

@app.route('/socket-programming')
def socket_programming():
    return render_template('socket-programming.html')

@app.route('/password-manager-web')
def password_manager_web():
    return render_template('password-manager-web.html')

@app.route('/expense-manager')
def expense_manager():
    return render_template('expense-manager.html')

@app.route('/password-manager-cli')
def password_manager_cli():
    return render_template('password-manager-cli.html')

@app.route('/billing-app')
def billing_app():
    return render_template('billing-app.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)