# We import necessary libraries 
from getpass import getpass
import smtplib
from email.message import EmailMessage
from datetime import time, timedelta, datetime
import sys

# This class handles the process of sending emails
class EmailHandler():
    
    # The initializer function, sets up SMTP server and logs in
    def __init__(self, email_username, email_domain="smtp.gmail.com", port=587, password=None, verbose=False):
        """Initializes the EmailHandler class.

        Args:
            email_username (str): The username of the email.
            email_domain (str, optional): The email domain. Defaults to 'smtp.gmail.com'.
            port (int, optional): The port to use. Defaults to 587.
            password (str, optional): The email password. If not provided, the user will be prompted for it. 
            verbose (bool, optional): If set to True, login attempts will be printed. Defaults to False.
        """
        
        if password is None:
            self.password = getpass()  # Get the password securely if not provided
        else:
            self.password = password
        self.username = email_username
        self.domain = email_domain
        self.verbose = verbose
        self.port = port
        if self.verbose:
            print("Trying login...")
        # Create an SMTP server instance and log in
        with smtplib.SMTP(self.domain, self.port) as server:
            server.starttls()  # Upgrade the connection to a secure one using TLS
            server.login(self.username, self.password)
        if self.verbose:
            print("... success!")

    # Function to write and send an email
    def write_email(self, email_address, subject, content, from_address=None):
        """Writes and sends an email.

        Args:
            email_address (list): The email addresses to send to.
            subject (str): The subject of the email.
            content (str): The content of the email.
            from_address (str, optional): The from address. If not provided, it defaults to the username provided when initializing the class.
        """
        
        msg = EmailMessage()
        msg.set_content(content)

        if from_address is None:
            msg['From'] = self.username + "@" + self.domain
        else:
            msg['From'] = from_address
        msg['To'] = email_address
        msg['Subject'] = subject
        # Send the email
        with smtplib.SMTP(self.domain, self.port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.send_message(msg)
        return 0
    
    # Function to read and format content from a text file
    def read_content_from_textfile(self, textfile, sender_name, recipient_name):
        """Reads a text file and replaces placeholders with sender and recipient names.

        Args:
            textfile (str): The path to the text file.
            sender_name (str): The name of the sender.
            recipient_name (str): The name of the recipient.

        Returns:
            str: The content of the text file with placeholders replaced.
        """
        
        with open(textfile) as fp:
            # Read the file and replace placeholder names
            content = fp.read().replace("YOURNAME", sender_name).replace("RECIPIENTNAME", recipient_name)
        return content


if __name__ == "__main__":
    # Initialize an EmailHandler object and send a test email
    eh = EmailHandler("svenheydenreich", "smtp.gmail.com", verbose=True)
    eh.write_email(["svenheydenreich@gmail.com","sheydenr@ucsc.edu"], subject="Test", content="TEST")
