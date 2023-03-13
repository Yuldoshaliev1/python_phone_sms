<div align="center">
<h1>System integration(Eskiz) send sms in python</h1>
</div>

This repository contains ready-made codes for how you can send SMS to mobile operators.

These codes contain integrations of the following services:

- Eskiz - Hurry up to book your seat online. [Official site](https://eskiz.uz/)
- Playmobile - SMS operator for business. [Official site](https://playmobile.uz/)
- Infobip - Connect worldwide with the leading SMS service. [Official site](https://www.infobip.com/sms)

## Required packages

[Requests](https://requests.readthedocs.io/) -
is an elegant and simple HTTP library for Python built for the people.

## Installation

Clone the project from github

```console
git clone https://github.com/Yuldoshaliev1/python_phone_sms.git
```

## Integration  [Eskiz.uz](https://eskiz.uz/)


To start integrating through the Eskiz service, you will need `ESKIZ_EMAIL` and `ESKIZ_PASSWORD`. You can get this information after the conclusion of [contract with the company](https://eskiz.uz/reseller)


After you have obtained the necessary keys, you must write them down by creating a `.env` file or just copy the prepared template `env.md`
```console
cp env.md .env
```



Fill in `ESKIZ_EMAIL` and `ESKIZ_PASSWORD`


Go to the `eskiz.py` file and put your phone number in the `phone` variable

### Let's start sending the first SMS
```console
python eskiz.py
```
