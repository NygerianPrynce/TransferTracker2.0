# myapp/management/commands/my_custom_command.py
from django.core.management.base import BaseCommand
from ...runner import findSearchedItemz
from ...runner import findDailyTransferz
import csv
from twilio.rest import Client
from django.core.mail import send_mail




class Command(BaseCommand):
    help = 'Run a daily view at 7 am'

    def handle(self, *args, **options):
        csv_file_path ='/Users/nygerianprynce/Documents/CS/NewTransferTracker/myproject/myapp/static/' + "info.csv" 

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
                if(seventh_column_value ==  eighth_column_value and eighth_column_value == ninth_column_value):
                    print("breaking")
                    continue
                num = len(findDailyTransferz(seventh_column_value, eighth_column_value, ninth_column_value))
                if(num > 0):
                    text = "Hello! " + str(num) + " transfers happened TODAY that you wanted to watch out for! Check the website to see specifics."
                    print(text)
                    
                    subject = 'Transfer Tracker - You Have Transfers!'
                    message = text
                    from_email = 'transfertrackerofficial@gmail.com'
                    recipient_list = [second_column_value]

                    send_mail(subject, message, from_email, recipient_list)
                    
                    account_sid = 'ACfa592fc49890a5c404e6c175d31ca1f4'
                    auth_token = 'f9da00fb013a4a6bab5e4fc52a3a6a19'

                    # Create a Twilio client
                    client = Client(account_sid, auth_token)

                    # Send an SMS message
                    message = client.messages.create(
                        body=text,
                        from_='+18442342185',
                        to=third_column_value
                    )

                    if message.sid:
                        self.stdout.write(self.style.SUCCESS(f"SMS sent with SID: {message.sid}"))
                    else:
                        self.stderr.write(self.style.ERROR("Failed to send SMS"))
                
                


                # Break the loop to process just one row
                
        
        
        
        
        # Call your view from views.py

