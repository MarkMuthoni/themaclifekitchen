from Kitchen import app
from flask import render_template, flash, url_for, redirect
from .forms import BookingForm
from twilio.rest import Client


@app.route('/')
@app.route('/home')
def home():
    return render_template('../index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/booking', methods=['POST', 'GET'])
def booking():
    form = BookingForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        mobile = form.mobile.data
        date = form.date.data
        time = form.time.data
        people = form.people.data
        requests = form.requests.data

        # Check if the restaurant is open
        if date.weekday() >= 5 or time.hour < 10 or time.hour > 22:
            flash('Sorry! We are closed! Try on open hours!!')
            return render_template('booking.html', form=form)

        # Send the order details to the restaurant owner's whatsapp number using Twilio
        # client = Client('<Your count SID>', '<Your AUTH CODE>')
        # message = f"New table reservation from {name} ({email}) \n {people} people on {date} at {time}.\n" \
        #           f" Contact number: {mobile} extra Table requests: {requests}"
        # client.messages.create(body=message, from_='whatsapp: SENDER',
        #                        to='whatsapp:RECEIVING')
        flash('Reservation requested successfully! '
              'We will contact you through call')
        form.process(obj=None)
        # Return a success message
        return redirect(url_for('home'))

    return render_template('booking.html', form=form)


@app.route('/meals')
def meals():
    return render_template('meals.html')


@app.route('/desserts')
def desserts():
    return render_template('desserts.html')


@app.route('/drinks')
def drinks():
    return render_template('drinks.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact_us.html')
