from src.app import create_app
import os

app = create_app()

if __name__ == '__main__':
    flask_port = app.config.get('FLASK_PORT')
    flask_host = app.config.get('FLASK_HOST')
    debug_mode = app.config.get('DEBUG')
    app.run(debug=debug_mode, host=flask_host, port=flask_port) 
