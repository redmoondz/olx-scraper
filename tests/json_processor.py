import json

with open("graphql_respons202511080700.json") as f:
   response = json.load(f)

core_path = response["data"]["clientCompatibleObservedAds"]["data"][0]

category = core_path["category"]["type"]
contact = core_path["contact"]["name"]
created_time = core_path["created_time"]
description = core_path["description"]
last_refresh_time = core_path["last_refresh_time"]
city = core_path["location"]["city"]["name"]
district = core_path["location"]["district"]["name"]
region = core_path["location"]["region"]["name"]
price = core_path["params"][0]["value"]["value"]
currency = core_path["params"][0]["value"]["currency"]
build_type = core_path["params"][1]["value"]["label"]
floor = core_path["params"][2]["value"]["label"]
total_floors = core_path["params"][3]["value"]["label"]
total_area = core_path["params"][4]["value"]["label"]
kitchen_area = core_path["params"][5]["value"]["label"]
house_type = core_path["params"][6]["value"]["label"]
number_of_rooms_string = core_path["params"][7]["value"]["label"]
layout = core_path["params"][8]["value"]["label"]
bathroom = core_path["params"][9]["value"]["label"]
heating = core_path["params"][10]["value"]["label"]
repair = core_path["params"][11]["value"]["label"]
furnish = core_path["params"][12]["value"]["label"]
# photos = core_path["photos"]
photos_raw = core_path["photos"]
photos = list(map(lambda photo: photo["link"].format(width=photo["width"], height=photo["height"]), photos_raw))


print(f"""
      Category: {category}
      Contact: {contact}
      Created Time: {created_time}
      Description: {description}
      Last Refresh Time: {last_refresh_time}
      City: {city}
      District: {district}
      Region: {region}
      Price: {price} {currency}
      Build Type: {build_type}
      Floor: {floor}
      Total Floors: {total_floors}
      Total Area: {total_area}
      Kitchen Area: {kitchen_area}
      House Type: {house_type}
      Number of Rooms: {number_of_rooms_string}
      Layout: {layout}
      Bathroom: {bathroom}
      Heating: {heating}
      Repair: {repair}
      Furnish: {furnish}
      Photos: {photos}
""")