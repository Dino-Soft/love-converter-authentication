from main import create_app
from main.extensions.instances import db

# Creating Flask app instance
app = create_app()

# Loading app context
app.app_context().push()


if __name__ == '__main__':

    db.create_all()
    app.run(host='0.0.0.0', port=5000)
