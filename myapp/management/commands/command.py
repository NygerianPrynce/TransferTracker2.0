# myapp/management/commands/my_custom_command.py
from django.core.management.base import BaseCommand
from ...runner import findSearchedItemz
from ...runner import findDailyTransferz
import csv
from twilio.rest import Client
from django.core.mail import send_mail
import logging
import requests

class Command(BaseCommand):
    help = 'Run a daily view at 7 am'

    def handle(self, *args, **options):
        # Configure logging
        logging.basicConfig(filename='logfile.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        # Log the execution of the command
        logging.info("Custom management command started")
        logging.shutdown()
        
        csv_file_path ='/home/ubuntu/TransferTracker2.0/myapp/static/' + "info.csv" 

        with open(csv_file_path, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='|')

            # Skip the header row if it exists
            next(csv_reader, None)

            for row in csv_reader:
                # Access the values in the specified columns for the current row
                second_column_value = row[1]
                third_column_value = row[2]
                seventh_column_value = row[5].split(",")
                eighth_column_value = row[6].split(",")
                ninth_column_value = row[7].split(",")
                # Process the values for the current row
                print("Values in the 2nd column:", second_column_value)
                print("Values in the 7th column:", seventh_column_value)
                print("Values in the 8th column:", eighth_column_value)
                print("Values in the 9th column:", ninth_column_value)

                
                
                num = 0
                if(seventh_column_value ==  eighth_column_value and eighth_column_value == ninth_column_value):
                    print("breaking")
                    continue
                maxi = findDailyTransferz(seventh_column_value, eighth_column_value, ninth_column_value)
                if(maxi):
                    num = len(maxi)
                
                if(num > 0):
                    text = "Hello! " + str(num) + " transfers happened TODAY that you wanted to watch out for! Check the website to see specifics."
                    print(text)
                    
                    subject = 'Transfer Tracker - You Have Transfers!'
                    message = text
                    from_email = 'transfertrackerofficial@gmail.com'
                    recipient_list = [second_column_value]

                    send_mail(subject, message, from_email, recipient_list)
                    
                    resp = requests.post('https://textbelt.com/text', {
                    'phone': third_column_value,
                    'message': text,
                    'key': '97c1acfbac413e75b926f1ef6f6c3acb52bfee2dAwHVQh4OZ3RiQrp6ZyxbnhtHX',
                    })
                    print(resp.json())


                # Break the loop to process just one row
                
        
        
        
        
        # Call your view from views.py

