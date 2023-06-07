from flask import Flask, render_template, url_for, request
import requests
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/ip", methods=['GET', 'POST'])
def ip():
    if request.method == 'POST':
        ip_address = request.form["ipAddress"]

        url = "https://ip-intel.aws.us.pangea.cloud/v1/reputation"
        headers = {'Content-Type': 'application/json'}
        data = {'ip': ip_address}
        response = requests.post(url, json=data, headers=headers)

        if response.status_code == 200:
            reputation = response.json()
            return render_template('ip.html', reputation=reputation)
        else:
            error_message = 'Error: Failed to retrieve reputation score'
            return render_template('error.html', error_message=error_message)
    return render_template('index.html')


@app.route("/domain")
def getDomain():
    url = "https://ip-intel.aws.eu.pangea.cloud/v1/domain"
    data = {
        "ip": "192.168.2.16"
    }
    response = requests.post(url, json=data)
    return "Displays Domain name"


@app.route("/location")
def getLocation():
    return "Displays Location"

if __name__ == "__main__":
    app.run(debug = True)