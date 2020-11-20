from twilio.rest import Client 

account_sid = 'AC2755015bb8aaae7e55e52dae20c5fc12' 
auth_token = 'f46c8257bd869cc8bb071743acb67f03' 
client = Client(account_sid, auth_token) 
 

message = client.messages.create( 
                              from_='+13169743125',  
                              body='Sakura!!!',      
                              to='+8618888929705' 
                          ) 
