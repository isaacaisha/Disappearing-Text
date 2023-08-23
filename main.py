from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, validators
import time
from datetime import datetime

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"

# ------------------------------------------------------ VARIABLES ----------------------------------------------------#
time_sec = time.localtime()
current_year = time_sec.tm_year
# getting the current date and time
current_datetime = datetime.now()
# getting the time from the current date and time in the given format
current_time = current_datetime.strftime("%a %d %B")


# -------------------------------------------------------- CLASS ------------------------------------------------------#
class TextAreaForm(FlaskForm):
    writing_text = TextAreaField('Start Writing', [validators.InputRequired(message="Please enter text.")])
    submit = SubmitField()


# ------------------------------------------------------- FUNCTION ----------------------------------------------------#
@app.route('/', methods=['GET', 'POST'])
def home():
    writing_text_form = TextAreaForm()
    error_message = None  # Initialize an error message variable

    if writing_text_form.validate_on_submit():
        writing_text_data = request.form['writing_text']  # Get the input from the textarea
        print(writing_text_data)
    else:
        writing_text_data = None  # Initialize it to None if the form is not submitted

    return render_template('index.html', year=current_year, date=current_time,
                           writing_text_form=writing_text_form,
                           writing_text_data=writing_text_data,  # Pass the data to the template
                           error_message=error_message)  # Pass the error message if needed


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
