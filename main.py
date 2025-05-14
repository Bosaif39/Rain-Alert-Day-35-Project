import requests  
import os        
from twilio.rest import Client  
from twilio.http.http_client import TwilioHttpClient  

# OpenWeatherMap API endpoint for getting hourly weather data
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# Load API keys from environment variables for security
api_key = os.environ.get("OWM_API_KEY")  # OpenWeatherMap API key
account_sid = "YOUR ACCOUNT SID"  # Twilio Account SID (replace with your actual SID)
auth_token = os.environ.get("AUTH_TOKEN")  # Twilio Auth Token (store securely in environment variables)

# Define parameters for the weather API request
weather_params = {
    "lat": "YOUR LATITUDE",  
    "lon": "YOUR LONGITUDE",  
    "appid": api_key,  
    "exclude": "current,minutely,daily"  
}


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()  


weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

# Loop through each hour's weather data
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]  
    # Weather codes less than 700 typically indicate precipitation (rain, snow, etc.)
    if int(condition_code) < 700:
        will_rain = True  

# If rain is expected, send an SMS alert
if will_rain:
    # Set up Twilio client with proxy (necessary for some environments)
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}  # Use system proxy settings if needed

    # Initialize Twilio client
    client = Client(account_sid, auth_token, http_client=proxy_client)
    
    # Send the SMS alert
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",  
        from_="YOUR TWILIO VIRTUAL NUMBER",  
        to="YOUR TWILIO VERIFIED REAL NUMBER"  
    )

    print(message.status)
