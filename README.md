
- Use these commands to let your server re-start by itself after every save
    -       export FLASK_ENV=development
            export FLASK_DEBUG=1

            # Everytime you close and restart the venv, you will have to run these commands once.

            # By setting FLASK_ENV to "development", Flask enables debug mode, which provides features like automatic reloading and detailed error messages. Setting FLASK_DEBUG to 1 activates the debug mode.

            # Keep in mind that this approach is specifically intended for development purposes and is not recommended for production deployments. For production environments, using Gunicorn, uWSGI, or a similar application server is the preferred approach.

- Run the Flask development server using the flask run command:
    -       flask run

- To see the detailed error messages and a debugger page if an error occurs:
    -       if __name__ == "__main__":
                app.run(debug=True)
