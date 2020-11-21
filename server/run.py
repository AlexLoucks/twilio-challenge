from src.app import createApp()
import os

app = createApp()

if __name__ == '__main__':
    flask_port = app.config.geto('FLASK_PORT')
    flask_host = app.config.geto('FLASK_HOST')
    app.run(debug=True, host=flask_host, port=flask_port)
