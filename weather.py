import requests
import takeCommand as tc 
import speak_Function as sf


def watherreporter():   
 api_address="http://api.openweathermap.org/data/2.5/weather?appid=cab78fa8a9c1d1cc50d6b98ae4efaa3d&q="
 sf.speak("Please Tell me city name") 
 city = tc.TakeCommand().lower()
 #city='noida'
 URL=api_address+city
 jonson_Data=requests.get(URL).json()
 tamp=((jonson_Data['main']['temp'])-273.15)
 weather_dec=jonson_Data['weather'][0]['description']
 hmdy1=jonson_Data['main']['humidity']
 hmdy="{}".format(hmdy1)
 wind_speed1=jonson_Data['wind']['speed']
 wind_speed = "{}".format(wind_speed1)

 print(" Dear sushma Temperature is :  {:.2f} deg C" .format(tamp))
 print("Current Weather description is : ",weather_dec)
 print("Current Humidity is :",hmdy , "%")   
 print("Current wind speed is :",wind_speed,"KPH")
 sf.speak("weather Report of "+city+"is")
 sf.speak(" Dear sushma     Temperature is :  {:.2f} degrees celsius" .format(tamp))
 sf.speak("Humidity is :" + hmdy + "%")   
 sf.speak(" wind speed are :" +(wind_speed)+ "kilometers per hour")
 sf.speak(" weather description is :  " +(weather_dec))
 sf.speak("What is next command")

if __name__ == "__main__":
    watherreporter()