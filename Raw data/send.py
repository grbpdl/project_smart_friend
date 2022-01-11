
import smtplib
import os
# from typing import Text
#import username and password from enviroment variables
username=os.environ.get('mygmail')
password=os.environ.get('mypassword')

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()

# start TLS for security
s.starttls()
s.ehlo()

# Authentication
s.login(username, password)


# message to be sent
Crush_name='Mansu'
SUBJECT='Help from Smart Friend'
receiver='ssquare1200@gmail.com'
letter='''My dear {} ,I am not very good at expressing my feelings in words, even though I assure you, I am quite a sensitive person. Somehow, often I get shy and run out of words even before I start talking.
However, I now want to tell you about my feelings.

We have been seeing each other for a while and I realize that the more I see you, the more I want to be with you. You are like a beacon of light in a starless night and I am drawn to you with a powerful pull that I can’t resist.
When I am not with you, I keep thinking about you and my day is rather empty. I find myself looking forward to our next meeting.
Yes, I realize now that I care for you very much and my feelings for you have awakened and are getting stronger and stronger each day.
I am starting to fall in love with you and my heart is fluttering every time I am near you … I just hope you have the same sensations and feelings as I do.

I just wanted to write my thoughts down and secretly send this love letter to you.

I am yours, forever …

PS:Have the guts and be positive,fordward this love mail to your crush!Wishing you best of luck!
-yours Smart Friend'''
TEXT=letter.format(Crush_name)
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
message=message.encode('ascii', 'ignore').decode('ascii')

# sending the mail
s.sendmail(username,receiver,message)

# terminating the session
s.quit()
