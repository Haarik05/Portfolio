from flask import Flask,render_template,url_for,request,redirect
import smtplib 
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sendemail/',methods=['POST'])
def sendemail():
    if request.method=="POST":
        name = request.form['username']
        email = request.form['email']
        text = request.form['text']
        mymailid = 'haarik05@gmail.com'
        mypassword = 'nxqhncolkeducoic'

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(mymailid,mypassword)

        msg = EmailMessage()
        msg.set_content('Hey you\'ve got a new visitor in portfolio\n'+'\nFrom: '+str(name) +'\n\n'+'Mail ID: '+ str(email)+'\n\n'+str(text))
        msg['to'] = "harish.g.2k1@gmail.com"


        try:
            server.send_message(msg)
            server.quit()
            print("success")
        except:
            print("email failed")
    return  redirect('/')   
if __name__=='__main__':
    app.run(debug=True)