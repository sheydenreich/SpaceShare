
from reader import read_google_sheet
from optimize_rideshares import optimize
from write_email import send_emails
import argparse

parser = argparse.ArgumentParser(description='Run the SpaceShare algorithm.')
parser.add_argument('--email_username', type=str, help='The username of the email account to send emails from.')

df = read_google_sheet()
for kind in ["arrival","departure"]:
    df = optimize(df,kind=kind)
df.to_csv("optimized_clustering.csv")
user_input = "n"
while user_input.lower() not in ["y","yes"]:
    user_input = input("The groups have been assigned. Please take a moment to inspect the results in optimized_clustering.csv \n"\
                        +"If you want, you can manually make changes to the document. \n"\
                        +"Do you want to send the emails? (y/n)")
send_emails(df, email_username="svenheydenreich",email_smtp_domain="smtp.gmail.com")