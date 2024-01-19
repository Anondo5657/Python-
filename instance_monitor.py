import json
import requests
webhook_url= "https://hooks.slack.com/services/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"
slack_channel = "#aws-resource-monitor"
#client = boto3.client('ec2')
headers={'Accept': 'application/json' }


def lambda_handler(event, context):
 main(event, context)


def main(event='',context=''):
 print event
 print event["detail"]
 print event["region"]
 print event["account"]
 print event["detail"]["state"]
 print event["detail"]["instance-id"]
 print event["account"]
 if event["detail"]["state"] == "pending" or event["detail"]["state"] == "stopping" or event["detail"]["state"] == "shutting-down" :
  payload = json.dumps({'channel' : slack_channel,'username':'Instance States', 'attachments':[{'color': '#6ecadc','text' : "\n*InstanceID*: " +event["detail"]["instance-id"] + "\n*Region*:" +event["region"]  + "\n*State*:" +event["detail"]["state"]  + "\n*AccountID*:" +str(event ["account"])}]})
  request=requests.post(webhook_url,headers=headers, data=payload)

if __name__=="__main__": main() 
 

        
 
 
