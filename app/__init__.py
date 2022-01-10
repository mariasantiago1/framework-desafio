from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    
    with app.app_context():
        from app import errors, logging
        from .controllers import todos, auth

        app.register_blueprint(errors.BLUEPRINT)
        app.register_blueprint(todos.BLUEPRINT)
        app.register_blueprint(auth.BLUEPRINT)
        app.register_blueprint(logging.BLUEPRINT)
        
        auth.jwt.init_app(app)
        
        return app