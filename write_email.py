# We import necessary libraries 
from getpass import getpass
import smtplib
from email.message import EmailMessage

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
    import pandas as pd
    import numpy as np
    eh = EmailHandler("svenheydenreich", "smtp.gmail.com", verbose=True)
    df = pd.read_csv("optimized_clustering.csv")

    helperstr = {}
    helperstr["arrival"] = """based on your planned arrival times, we suggest that you share a ride from the airport to your hotel.
You have said that you want to leave the airport at the following times"""
    helperstr["departure"] = """based on your planned departure times, we suggest that you share a ride from your hotel to the airport.
You have said that you want to leave the hotel at the following times"""
    colnames = {}
    colnames["arrival"] = "date_time_of_airport_arrival"
    colnames["departure"] = "date_time_of_hotel_departure"
    for kind in ["arrival", "departure"]:
        groups = np.unique(df[f"{kind}_group"])
        for group in groups:
            mask = (df[f"{kind}_group"] == group)
            names = df["Name"][mask].values
            first_names = []
            for name in names:
                first_names.append(name.split(" ")[0]) #only address by first names
            arrival_times = df[colnames[kind]][mask].values
            emails = list(df["Email"][mask].values)
        
            address = ""
            for name in first_names:
                address += name+", "
            
            deptimes = ""
            for x in range(len(first_names)):
                deptimes += "\t"+names[x]+": "+arrival_times[x]+"\n "
            message = f"""
Dear {address}

{helperstr[kind]}:\n{deptimes}
Please contact each other and organize a ride together. If you have any questions, please contact us.

Best regards,
    The code/astro Team
            """
            print("Writing to: ",emails)
            # print(message)
        
    # Compose arrival message
            if np.sum(mask) < 2:
                if(kind == "arrival"):
                    content=f"""Dear {first_names[0]},
We are writing to you because you have indicated that you would like to share a ride from the airport to your hotel.
Unfortunately, we have not been able to find any other participants who would like to share a ride at the same time.
If you would like to share a ride, please contact us and we will try to find a solution.

Best regards,
    The code/astro Team"""
                else:
                    content=f"""Dear {first_names[0]},
We are writing to you because you have indicated that you would like to share a ride from your hotel to the airport.
Unfortunately, we have not been able to find any other participants who would like to share a ride at the same time.
If you would like to share a ride, please contact us and we will try to find a solution.

Best regards,
    The code/astro Team"""
                eh.write_email(emails, subject=f"[code/astro] Rideshare for your {kind}", 
                               content = content)
            else: # more than 2 people in the group
                eh.write_email(emails, subject=f"[code/astro] Rideshare for your {kind}", content=message)
