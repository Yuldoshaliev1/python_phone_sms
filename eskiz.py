import os

import requests
from dotenv import load_dotenv

load_dotenv('.env')

SUCCESS = 200
PROCESSING = 102
FAILED = 400
INVALID_NUMBER = 160
MESSAGE_IS_EMPTY = 170
SMS_NOT_FOUND = 404
SMS_SERVICE_NOT_TURNED = 600

ESKIZ_EMAIL = os.getenv('ESKIZ_EMAIL')
ESKIZ_PASSWORD = os.getenv('ESKIZ_PASSWORD')


class SendSmsApiWithEskiz:
    def __init__(self, message, phone, email=ESKIZ_EMAIL, password=ESKIZ_PASSWORD):
        self.message = message
        self.phone = phone
        self.spend = None
        self.email = email
        self.password = password

    def send(self):
        status_code = self.custom_validation()
        if status_code == SUCCESS:
            result = self.calculation_send_sms(self.message)
            if result == SUCCESS:
                return self.send_message(self.message)
            else:
                return result
        return status_code

    def custom_validation(self):
        if len(str(self.phone)) != 9:
            return INVALID_NUMBER
        if self.message == '' or not self.message:
            return MESSAGE_IS_EMPTY
        else:
            self.message = self.clean_message(self.message)
        return SUCCESS

    def authorization(self):
        data = {
            'email': self.email,
            'password': self.password,
        }

        AUTHORIZATION_URL = 'http://notify.eskiz.uz/api/auth/login'

        r = requests.request('POST', AUTHORIZATION_URL, data=data)
        if r.json()['data']['token']:
            return r.json()['data']['token']
        else:
            return FAILED

    def send_message(self, message):
        token = self.authorization()
        if token == FAILED:
            return FAILED

        SEND_SMS_URL = "http://notify.eskiz.uz/api/message/sms/send"

        PAYLOAD = {
            'mobile_phone': '998' + str(self.phone),
            'message': message,
            'from': '4546',
            'callback_url': 'http://afbaf9e5a0a6.ngrok.io/sms-api-result/'}

        FILES = [

        ]
        HEADERS = {
            'Authorization': f'Bearer {token}'
        }
        r = requests.request("POST", SEND_SMS_URL, headers=HEADERS, data=PAYLOAD, files=FILES)
        print(f"Eskiz: {r.json()}")
        return r.status_code

    def get_status(self, id):
        token = self.authorization()

        CHECK_STATUS_URL = 'http://notify.eskiz.uz/api/message/sms/status/' + str(id)

        HEADERS = {
            'Authorization': f'Bearer {token}'
        }

        r = requests.request("GET", CHECK_STATUS_URL, headers=HEADERS)
        if r.json()['status'] == 'success':
            if r.json()['message']['status'] == 'DELIVRD' or r.json()['message']['status'] == 'TRANSMTD':
                return SUCCESS
            elif r.json()['message']['status'] == 'EXPIRED':
                return FAILED
            else:
                return PROCESSING

    def clean_message(self, message):
        print(f"Old message: {message}")
        message = message.replace('??', 'ts').replace('??', 'ch').replace('??',
                                                                        'yu').replace(
            '??', 'a').replace('??', 'b').replace('??', "q").replace('??', "o'").replace('??', "g'").replace('??',
                                                                                                        "h").replace(
            '??',
            "x").replace(
            '??', 'v').replace('??', 'g').replace('??', 'd').replace('??',
                                                                  'e').replace(
            '??', 'yo').replace('??', 'j').replace('??', 'z').replace('??', 'i').replace('??', 'y').replace('??',
                                                                                                       'k').replace(
            '??', 'l').replace('??', 'm').replace('??', 'n').replace('??', 'o').replace('??', 'p').replace('??',
                                                                                                      'r').replace(
            '??', 's').replace('??', 't').replace('??', 'u').replace('??', 'sh').replace('??', 'sh').replace('??',
                                                                                                        'f').replace(
            '??', 'e').replace('??', 'i').replace('??', 'ya').replace('??', "o'").replace('??', "'").replace('??',
                                                                                                        "'").replace(
            '???', "'").replace('???', '"').replace('???', '"').replace(',', ',').replace('.', '.').replace(':', ':')
        # filter upper
        message = message.replace('??', 'Ts').replace('??', 'Ch').replace('??', 'Yu').replace(
            '??', 'A').replace('??', 'B').replace('??', "Q").replace('??', "G'").replace('??', "H").replace('??',
                                                                                                       "X").replace(
            '??', 'V').replace('??', 'G').replace('??', 'D').replace('??',
                                                                  'E').replace(
            '??', 'Yo').replace('??', 'J').replace('??', 'Z').replace('??', 'I').replace('??', 'Y').replace('??',
                                                                                                       'K').replace(
            '??', 'L').replace('??', 'M').replace('??', 'N').replace('??', 'O').replace('??', 'P').replace('??',
                                                                                                      'R').replace(
            '??', 'S').replace('??', 'T').replace('??', 'U').replace('??', 'Sh').replace('??', 'Sh').replace('??',
                                                                                                        'F').replace(
            '??', 'E').replace('??', 'Ya')
        print(f"Cleaned message: {message}")
        return message

    def calculation_send_sms(self, message):
        try:
            length = len(message)
            if length:
                if length >= 0 and length <= 160:
                    self.spend = 1
                elif length > 160 and length <= 306:
                    self.spend = 2
                elif length > 306 and length <= 459:
                    self.spend = 3
                elif length > 459 and length <= 612:
                    self.spend = 4
                elif length > 612 and length <= 765:
                    self.spend = 5
                elif length > 765 and length <= 918:
                    self.spend = 6
                elif length > 918 and length <= 1071:
                    self.spend = 7
                elif length > 1071 and length <= 1224:
                    self.spend = 8
                else:
                    self.spend = 30

                print(f"spend: {self.spend}")

                return SUCCESS
        except Exception as e:
            print(e)
            return FAILED


message = "?????????? ????????"
phone = 900336670
eskiz_api = SendSmsApiWithEskiz(message=message, phone=phone)
r = eskiz_api.send()

print(r)
