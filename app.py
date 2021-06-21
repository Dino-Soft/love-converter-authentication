from main import create_app
from main.extensions.instances import db
from main.models import UserModel

# Creating Flask app instance
app = create_app()

# Loading app context
app.app_context().push()


if __name__ == '__main__':

    db.Base.metadata.create_all(db.engine)
    app.run(host='0.0.0.0', port=5000)
