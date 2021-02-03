from flask import Flask, render_template, request, redirect
import json
import requests
app = Flask(__name__)

app.debug = True
app.secret_key = 'qsfqsdfsdf'

appSecret = "270125d7-f65c-4238-86bf-dc2c85632900"
appPublic = "4bc20c76-9df5-41ee-a63a-90914072b393"

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/paymentS')
def paymentS():
    return render_template('paymentS.html')


@app.route('/paymentF')
def paymentF():
    return render_template('paymentF.html')

@app.route('/handle_payment', methods=['POST'])
def handle_data():
    token = request.form['payment_id']
    code = request.form['flouci_otp']
    r = requests.post('https://developers.flouci.com/api/accept',json={'app_secret': appSecret,'app_token': appPublic,'flouci_otp' : code,'payment_id': token, "amount": "1000"}, verify=False)
    response = json.loads(r.text)
    print (response)
    if (response['code'] == 0):
        if (response['result']['status'] == 'SUCCESS'):
            return redirect("/paymentS", code=302)
    return redirect("/paymentF", code=302)

@app.route('/handle_payment2', methods=['POST'])
def handle_data2():
    token = request.form['payment_id']
    code = request.form['flouci_otp']
    print({'app_secret': appSecret, 'app_token': appPublic, 'flouci_otp': code, 'payment_id': token, "amount": "7000"})
    r = requests.post('https://developers.flouci.com/api/accept',json={'app_secret': appSecret,'app_token': appPublic,'flouci_otp' : code,'payment_id': token, "amount": "7000"}, verify=False)
    response = json.loads(r.text)
    print (response)
    if (response['code'] == 0):
        if (response['result']['status'] == 'SUCCESS'):
            return redirect("/paymentS", code=302)
    return redirect("/paymentF", code=302)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
