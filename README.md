# Rain Alert

## **Overview**

This is the Day 35 project from the course "100 Days of Code: The Complete Python Pro Bootcamp". 

This project is designed to send a rain alert via SMS if the weather forecast predicts rain in the next 12 hours.

## **How It Works**

1. The script fetches weather data from the OpenWeatherMap API for your specified location.
2. It checks the forecast for the next 12 hours to see if any of the weather conditions indicate rain (e.g., weather codes < 700).
3. If rain is forecasted, the script sends an SMS notification via Twilio to remind you to bring an umbrella.

## **Instructions**

### 1. Set Up Environment Variables

Before running the script, you will need to configure environment variables to securely store your API keys and sensitive data. Follow these steps to create the `.env` file:

#### a. Create a `.env` File:
- Create a file named `.env` in the same directory as the script.

#### b. Add Your API Keys and Configuration:
- Inside the `.env` file, add the following lines and replace the placeholders with your actual values:

```plaintext
OWM_API_KEY=your_openweathermap_api_key
AUTH_TOKEN=your_twilio_auth_token
https_proxy=your_proxy_url (optional, only if you're behind a proxy)
````

* **OWM\_API\_KEY**: Get this key from [OpenWeatherMap](https://openweathermap.org/). You will need to sign up and create a free account to obtain the key.
* **AUTH\_TOKEN**: Get this from your [Twilio account](https://www.twilio.com/). Sign up for an account and create a new project to get your Auth Token.
* **https\_proxy**: This is only needed if you're working behind a proxy server. You can leave it out if it's not required.

### 2. Install Dependencies

You will need to install the required libraries. Run the following commands in your terminal:

```bash
pip install requests
pip install twilio
```

### 3. Update the Script

In the `rain_alert.py` script, you'll need to replace the following placeholders with your own values:

* **"YOUR ACCOUNT SID"**: Your Twilio account SID (can be found in your Twilio console).
* **"YOUR LATITUDE"**: The latitude of your location (e.g., 37.7749 for San Francisco).
* **"YOUR LONGITUDE"**: The longitude of your location (e.g., -122.4194 for San Francisco).
* **"YOUR TWILIO VIRTUAL NUMBER"**: Your Twilio virtual phone number (you'll get this when you set up your Twilio account).
* **"YOUR TWILIO VERIFIED REAL NUMBER"**: Your own phone number (the one you want to receive SMS alerts on).

### 4. Run the Script

Once everything is set up, simply run the script from the terminal:

```bash
python rain_alert.py
```

If the weather forecast predicts rain in the next 12 hours, you will receive an SMS alert with the message:

**"It's going to rain today. Remember to bring an ☔️"**

## **Requirements**

* Python 3.x
* `requests` library for API calls (`pip install requests`)
* `twilio` library for SMS notifications (`pip install twilio`)


