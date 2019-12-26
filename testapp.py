
import requests

url = "https://apidojo-booking-v1.p.rapidapi.com/properties/list"

querystring = {"price_filter_currencycode":"USD","travel_purpose":"leisure","categories_filter":"price%3A%3A9-40%2Cfree_cancellation%3A%3A1%2Cclass%3A%3A1%2Cclass%3A%3A0%2Cclass%3A%3A2","search_id":"none","order_by":"popularity","children_qty":"2","languagecode":"en-us","children_age":"5%2C7","search_type":"city","offset":"0","dest_ids":"-3712125","guest_qty":"1","arrival_date":"2020-03-13","departure_date":"2020-03-15","room_qty":"1"}

headers = {
    'x-rapidapi-host': "apidojo-booking-v1.p.rapidapi.com",
    'x-rapidapi-key': "8db0766d39mshd989c285041be77p1d6fadjsn8c1a6aa2a263"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)