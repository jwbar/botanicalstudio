from flask import Flask, render_template, request, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

app = Flask(__name__)
app.secret_key = 'replace from key file'  # Change this to a secure value

@app.route('/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        topic = request.form.get('topic')
        message = request.form.get('message')

        # Create the email content
        email_content = f"Name: {name}\nEmail: {email}\nTopic: {topic}\nMessage:\n{message}"
        
        # Construct the SendGrid email message
        msg = Mail(
            from_email='fresh@katari.farm',  # Sender's email address
            to_emails='botanicalstudiolab@gmail.com',  # Recipient's email address
            subject=f"Contact Form Submission: {topic}",
            plain_text_content=email_content
        )

        try:
            # Send the email
            sg = SendGridAPIClient('replace with SG key from file')
            response = sg.send(msg)
            app.logger.info(f"Response Status Code: {response.status_code}")
            app.logger.info(f"Response Body: {response.body}")
            app.logger.info(f"Response Headers: {response.headers}")
            flash('Message sent successfully.', 'success')
        except Exception as e:
            app.logger.error(f"Failed to send message. Error: {str(e)}")
            flash(f'Failed to send message. Error: {str(e)}', 'error')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
