from flask import Flask, request
import json

app = Flask(__name__)




@app.route('/')
@app.route('/index', methods=['GET','POST'])  # create a route for webhook
def index():
    args = request.json
    args1 = args['queryResult']['queryText']
    print('payload -->%s', args)
    print('text -->%s', args1)

    File_object = open("/home/dell/Desktop/request_store.txt","a")
    File_object.write("Agent : "+ args1 + "\n\n")
    File_object.close()

    res = 'Now Dialogflow gets default responce'
    res_phone = 'This is Default telephony responce'
 #   dictionay = {'fulfillmentText': res,
 #                'fulfillmentMessages': [{"platform": "TELEPHONY", "telephonySynthesizeSpeech": {"text": res_phone}}]}

    dictionay = {'fulfillmentText': res,
                    "fulfillmentMessages": [{
                                "platform": "TELEPHONY",
                                "telephonySynthesizeSpeech": {
                                    "text": "Whatever message you want to say to the caller. This is Default telephony responce <break time=0.5s />Goodbye</speak>"
                                }
                            }, {
                                "platform": "TELEPHONY",
                                "telephonyTransferCall": {
                                    "phoneNumber": "+18667817957"
                                                        }
                                },
                        { "text":
                              { "text": [
                                  "This is Default telephony responce"
                                        ]
                              }
                        }
                    ]
                }
    dictionay_json = json.dumps(dictionay)

    return dictionay_json


if __name__ == '__main__':
    app.run(port=8000, debug=True)
