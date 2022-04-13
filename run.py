from application.app import created_app


if __name__ == '__main__':
    app = created_app()
    app.run(debug=True)
