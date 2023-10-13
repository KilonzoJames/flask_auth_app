from project import db, create_app

# Create the Flask app instance
app = create_app()

# Create the database tables
with app.app_context():
    db.create_all()
