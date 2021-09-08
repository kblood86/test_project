from flask import Flask, render_template, jsonify


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home2.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/background')
def background():
    return render_template('background.html')


@app.route('/application')
def application():
    return render_template('application.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/api/feature_names')
def feature_names():
    return jsonify(column_names)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':

    # Run this when running on LOCAL server...
    app.run(debug=True)

    # ...OR run this when PRODUCTION server.
    # app.run(debug=False)