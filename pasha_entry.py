from app import app
from pasha_routes import bp as pasha_review_blueprint

# Keep the book-review subsystem isolated from the core application module while
# registering it on the same Flask app and database-backed mastery engine.
if "pasha_review" not in app.blueprints:
    app.register_blueprint(pasha_review_blueprint)
