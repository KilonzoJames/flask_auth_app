from project import db, create_app

# Create the Flask app instance
app = create_app()

# Initialize the app with the Flask-SQLAlchemy extension
db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()
