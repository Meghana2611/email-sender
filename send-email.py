import smtplib 
import ssl
from email.message import EmailMessage

# Define email sender and receiver
email_sender = 'meghana_thota@srmap.edu.in'
email_password = 'jvom apxb hvsd oigq'       
email_receiver = 'meghanathota2605@gmail.com'

# Set the subject and body of the email
subject = 'Check out the new job opening in linkedin'
body = """
Data analyst- openings 2 at Novogo
SDE - at CRED
"""

em = EmailMessage()
em['From'] = email_sender 
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# Add SSL (layer of security)
context = ssl.create_default_context()

# Log in and send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

print("Email sent successfully..Check your mail!! ")


#brief explanation on what is what 

#smtplib:
#Full Form: Simple Mail Transfer Protocol Library
#Purpose: This module in Python defines an SMTP client session object that can be used to send email to any internet machine with an SMTP or ESMTP (Extended SMTP) listener daemon. SMTP is the protocol used for sending emails across the Internet.

#ssl:
#Full Form: Secure Sockets Layer
#Purpose: SSL is a standard security technology for establishing an encrypted link between a server and a client—typically a web server (website) and a browser, or a mail server and a mail client. It ensures that all data passed between them remains private and secure.

#email.message.EmailMessage:
#Purpose: The EmailMessage class is part of the email module in Python and provides a way to create and manipulate email messages. It allows you to set the headers, subject, body, and attachments for an email in a structured way.

#EmailMessage():
#Purpose: This creates a new instance of an email message object, which is then used to set the details of the email such as sender, receiver, subject, and body.

#Purpose: This sets the subject of the email, which is the topic or title of the email message.
#em.set_content(body):

#Purpose: This sets the main content of the email, which in this case is plain text. The body of the email is what the recipient will read in the email message.

#ssl.create_default_context():
#Purpose: This function creates a default SSL context, which is a set of configurations for secure communication. The SSL context ensures that the connection to the email server is encrypted and secure, protecting the data being sent.

#smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context):

#SMTP:
#Full Form: Simple Mail Transfer Protocol
#Purpose: This initiates a connection to Gmail's SMTP server using SSL encryption on port 465. SSL is required by Gmail to ensure the connection is secure.
#'smtp.gmail.com': This is the domain name of Gmail's SMTP server.
#Port 465: This is the port number used by Gmail's SMTP server for SSL connections.

#with:
#Purpose: This is a context manager in Python, which ensures that the SMTP connection is properly opened and closed. If an error occurs during the connection, the with statement ensures that resources are properly cleaned up.

#smtp.sendmail(email_sender, email_receiver, em.as_string()):
#Purpose: This method sends the email from the sender to the receiver. The em.as_string() method converts the EmailMessage object into a string format that can be transmitted over the network.