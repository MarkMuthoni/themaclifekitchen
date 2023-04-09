from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, DateField, TimeField
from wtforms.validators import DataRequired, Length, Email, Regexp, NumberRange, ValidationError
from datetime import time, datetime, timedelta
from flask import flash


class BookingForm(FlaskForm):
    name = StringField('Name*',
                       validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email*',
                        validators=[DataRequired(), Email()],
                        render_kw={'placeholder': 'bookatable@email.com'})
    mobile = StringField('Phone No*',
                         validators=[DataRequired(), Length(min=10, max=10),
                                     Regexp(r'(07|01)\d{8}$',
                                            message='Enter a valid phone number')],
                         render_kw={'placeholder': '07******** or 01********'})
    date = DateField('Date*', validators=[DataRequired()])
    time = TimeField('Time*', validators=[DataRequired()])
    people = IntegerField('No. of People*',
                          validators=[DataRequired(), NumberRange(min=1, max=6,
                                                                  message='Maximum of five people per table')])
    requests = TextAreaField('Additional Dietary Requirements/Other request?')
    submit = SubmitField('Reserve Table')

    def validate_date(self, field):
        if field.data < datetime.today().date():
            flash('Date cannot be in the past')
            raise ValidationError('Date cannot be in the past.')
        if field.data > datetime.today().date() + timedelta(days=14):
            flash('Date cannot be more than 14 days in the future')
            raise ValidationError('Date cannot be more than 14 days in the future.')

    def validate_time(self, field):
        datetime_obj = datetime.combine(self.date.data, self.time.data)
        if not (time(10, 0) <= datetime_obj.time() <= time(20, 0)):
            flash('We are closed at this hour, We are open between 10:00am-22:00pm;'
                  'latest reservation is received at least two hours before closing hour')
            raise ValidationError('Time must be between 10:00 and 23:00.')
