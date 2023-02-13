import json
from flask import Flask, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    response = ""
    if text == "":
        # Main menu options
        response = "CON What would you like to do?\n"
        response += "1. Balance inquiry\n"
        response += "2. Send money\n"
        response += "3. Buy airtime\n"
        response += "4. Exit\n"
    elif text == "1":
        # Balance inquiry option
        response = "END Your current balance is $100."
    elif text == "2":
        # Send money option
        response = "END Send money option."
    elif text == "3":
        # Buy airtime option
        response = "END Buy airtime option."
    elif text == "4":
        # Exit option
        response = "END Goodbye."

    return response


if (__name__ == "__main__"):
    app.run(debug=False, host="0.0.0.0")
