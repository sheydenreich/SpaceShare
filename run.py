
from reader import read_google_sheet
from optimize_rideshares import optimize
from write_email import send_emails
import pandas as pd
import configparser

# Read the config file
config = configparser.ConfigParser()

def run(config_file = "default.cfg"):
    
    config.read(config_file)
    email_username = config["EMAIL"]["username"].replace(" ","")
    email_password = config.get("EMAIL","password",fallback=None).replace(" ","")
    email_smtp_domain = config["EMAIL"]["smtp_domain"].replace(" ","")
    email_smtp_port = int(config["EMAIL"]["smtp_port"])

    


    df = read_google_sheet()
    for kind in ["arrival","departure"]:
        df = optimize(df,kind=kind)
    df.to_csv("optimized_clustering.csv")
    user_input = "n"
    while user_input.lower() not in ["y","yes"]:
        user_input = input("The groups have been assigned. Please take a moment to inspect the results in optimized_clustering.csv \n"\
                            +"If you want, you can manually make changes to the document. \n"\
                            +"Do you want to send the emails? (y/n)")

    df = pd.read_csv("optimized_clustering.csv")
    send_emails(df, email_username=email_username,email_smtp_domain=email_smtp_domain,
                email_password=email_password,email_smtp_port=email_smtp_port)