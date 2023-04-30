import os
from src.app import create_app

# create a Flask app instance
app = create_app()

# when ran as script
if __name__ == "__main__":
    os.environ.setdefault("FLASK_ENV", "development")
    os.environ.setdefault("FLASK_DEBUG", "1")

# when ran by flask
if __name__ == '__main__':
    # run the Flask app
    app.run()
