from background_task import background
import requests

@background(schedule=60)
def notify_email(email_id):
    # sent user we had received their submission


@background(schedule=60)
def send_reply(email_id):
    # lookup user by email and send them a message
	html_design = '<html><head><meta charset="UTF-8"><link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet"><title>Simple, flat contact form</title></head><body style="background-color: #f6f6f6;"><section class="container" style="font-family: \'Open Sans\', sans-serif;position: relative;text-align: center;background: white;padding: 13px;height: 300px;width: 80%;margin: 20px auto 5px auto;"><section class="header" style="font-family: \'Open Sans\', sans-serif;position: relative;text-align: left;font-size: 150%;margin: 5px 10% 0 10%;"><p>ENQUIRES : '+ name + '</p><p>EMAIL    : '+email+ '</p><p>ENQUIRE CONTENT: </p></section><p class="content" style="font-size: 120%;color: #353535;"> '+content+'</p></section></body></html>'
