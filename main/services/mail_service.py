from app import app
from flask_mail import Mail, Message
from flask import render_template
from threading import Thread

def sendMail(to, subject, template, **kwargs):
    msg = Mail.Message(subject, sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template('mail/' + template + '.txt', **kwargs)
    msg.html = render_template('mail/' + template + '.html', **kwargs)
    thr = Thread(target=mail_sender, args=[app, msg])
    thr.start()  # Iniciar hilo

def mail_sender(app, msg):
    with app.app_context():
        Mail.send(msg)  # send es la que envia el mail

#se que esto no va a aca, pero asi seria el envio de un mensaje
#sendMail('correo@ejemplo.com', 'mensaje', 'nombre del template')
