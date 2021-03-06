"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""

from app import app
import datetime
from flask import render_template, request, redirect, url_for, flash


###
# Routing for your application.
###

def format_date_joined(date):
    return "Joined "  + date.strftime("%B, %Y")

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")


@app.route('/profile/')
def profile():
    """Render the website's profile page."""
    return render_template('profile.html', name="Mary Jane",
    username="maryjane",
    address="Kingston,Jamaica",
    joined=format_date_joined(datetime.datetime.now()),
    abt="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas rutrum, enim ac egestas malesuada, purus tortor accumsan neque, sit amet aliquam odio erat vel lectus. Praesent leo velit, egestas maximus mauris eu, porta varius nibh. Nam vel scelerisque justo. Curabitur in ligula id mi accumsan dignissim sed a dolor. Quisque et felis quis ante rhoncus fringilla eget luctus ante. Cras eu aliquet nunc. Mauris feugiat ipsum eget vehicula aliquet. Nullam dapibus neque dignissim neque lobortis, vitae iaculis tellus pulvinar. Etiam lacinia placerat feugiat. Aliquam non pharetra quam. Nullam enim ipsum, dignissim id lacus ac, molestie ultricies ante. Aenean luctus, eros et elementum consectetur, mauris nunc consequat leo, at tempor urna turpis eget neque. ",
    posts="7",
    followers="100",
    following="250",
    source= url_for("static", filename="girl.png"))


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
