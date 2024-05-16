import requests
import json
import os
import time  # Import the time module for adding delay

# Define the Google Maps API key
api_key = "AIzaSyC9hDsxtzOagIDuNPbH8SCgA01jNlq5tNc"

# Example JSON array data
json_data = [
 {
  "LOCATION": "A'dam Noord",
  "Address": "Dorpsstraat 42A, 1121 BX Landsmeer (Studio van Hout)"
 },
 {
  "LOCATION": "Alkmaar",
  "Address": "Van der Kaaijstraat 64, 1815 VM Alkmaar"
 },
 {
  "LOCATION": "Almelo",
  "Address": "Bedrijvenpark Twente 305, 7602 KL Almelo"
 },
 {
  "LOCATION": "Almere",
  "Address": "Markerkant 13-10, 1314 AN Almere"
 },
 {
  "LOCATION": "Alphen ad Rijn",
  "Address": "Leidse Schouw 2,  2408 AE Alphen aan den Rijn"
 },
 {
  "LOCATION": "Amersfoort",
  "Address": "Arnhemseweg 6, 1e verdieping, 3817 CH Amersfoort"
 },
 {
  "LOCATION": "Amstelveen",
  "Address": "Orion 3, 1188 AM Amstelveen"
 },
 {
  "LOCATION": "Amsterdam West",
  "Address": "Willem de Zwijgerlaan 69, 1056 JG Amsterdam"
 },
 {
  "LOCATION": "Amsterdam Zuid",
  "Address": "Pietersbergweg 291, 1105 BM Amsterdam"
 },
 {
  "LOCATION": "Apeldoorn",
  "Address": "Het Rietveld 55, 7321 CT Apeldoorn"
 },
 {
  "LOCATION": "Arnhem",
  "Address": "Van Nispenstraat 139, 6814 JA Arnhem"
 },
 {
  "LOCATION": "Assen",
  "Address": "Overcingellaan 17, 9401 LA Assen"
 },
 {
  "LOCATION": "Baarn",
  "Address": "Baarnsche dijk 4D, 3741 LR Baarn"
 },
 {
  "LOCATION": "Barendrecht",
  "Address": "Middenbaan 111, 2991 CS Barendrecht."
 },
 {
  "LOCATION": "Barneveld",
  "Address": "Zonnebloemstraat 31, 3772 GR Barneveld."
 },
 {
  "LOCATION": "Bergen op Zoom",
  "Address": "Zuidzijdehaven 39 A, 4611 HC Bergen op Zoom"
 },
 {
  "LOCATION": "Beverwijk",
  "Address": "Gaasterland 8, 1948 RG Beverwijk"
 },
 {
  "LOCATION": "Breda",
  "Address": "Lijndonk 4, 4825 BG Breda"
 },
 {
  "LOCATION": "Capelle ad IJssel",
  "Address": "Kanaalweg 33, 2903 LR Capelle aan den IJssel"
 },
 {
  "LOCATION": "Castricum",
  "Address": "Overtoom 15, 1901 EW Castricum"
 },
 {
  "LOCATION": "Coevorden",
  "Address": "Rabenhauptstraat 1, 7741 EN Coevorden"
 },
 {
  "LOCATION": "Delft",
  "Address": "Van Beresteynstraat 99, 2614 HE Delft"
 },
 {
  "LOCATION": "Delfzijl",
  "Address": "Ruif 1, 9932 BS Delfzijl"
 },
 {
  "LOCATION": "Den Bosch",
  "Address": "Daviottenweg 40, 5222 BH Den Bosch"
 },
 {
  "LOCATION": "Den Haag",
  "Address": "Platinaweg 25, 2544 EZ Den Haag"
 },
 {
  "LOCATION": "Den Haag Zaterdag",
  "Address": "Binkhorstlaan 36, 2516 BE Den Haag"
 },
 {
  "LOCATION": "Den Helder",
  "Address": "Geulstraat 7, 1784 DH, Den Helder"
 },
 {
  "LOCATION": "Denekamp",
  "Address": "Oranjestraat 21, 7591 GA Denekamp"
 },
 {
  "LOCATION": "Deventer",
  "Address": "Bruynssteeg 28, 7411 LT Deventer"
 },
 {
  "LOCATION": "Deventer",
  "Address": "Bruynssteeg 28, 7411 LT Deventer"
 },
 {
  "LOCATION": "Doetinchem",
  "Address": "Hanzestraat 1, 7006 RH Doetinchem"
 },
 {
  "LOCATION": "Dokkum",
  "Address": "Oranjewal 28, 9101 JV Dokkum"
 },
 {
  "LOCATION": "Dordrecht",
  "Address": "Vissersdijk Beneden 70 (Business Point), 3319 GW Dordrecht"
 },
 {
  "LOCATION": "Drachten",
  "Address": "Morrapark 2, 9204 KH Drachten"
 },
 {
  "LOCATION": "Dronten",
  "Address": "De Rede 80, 8251 EX Dronten"
 },
 {
  "LOCATION": "Ede",
  "Address": "Galvanistraat 1, 6716 AE Ede"
 },
 {
  "LOCATION": "Eindhoven",
  "Address": "Noord Brabantlaan 265, 5652 LD Eindhoven"
 },
 {
  "LOCATION": "Emmeloord",
  "Address": "Randweg 25, 8304 AS Emmeloord"
 },
 {
  "LOCATION": "Emmen",
  "Address": "De Bukakkers 20, 7811 KZ Emmen"
 },
 {
  "LOCATION": "Enschede",
  "Address": "Wethouder Beverstraat 185, 7543 BK Enschede"
 },
 {
  "LOCATION": "Epe",
  "Address": "Stationsstraat 25, 8161 EP Epe"
 },
 {
  "LOCATION": "Ettenleur",
  "Address": "Bredaseweg 185, 4872 LA"
 },
 {
  "LOCATION": "Goes",
  "Address": "Van Dusseldorpstraat 40, 4461 ND Goes"
 },
 {
  "LOCATION": "Gorinchem",
  "Address": "Edisonweg 30, 4207 HG Gorinchem"
 },
 {
  "LOCATION": "Gouda",
  "Address": "Oosthaven 12, 2801 PB Gouda "
 },
 {
  "LOCATION": "Groningen",
  "Address": "Paterswoldseweg 806, 9728 BM Groningen"
 },
 {
  "LOCATION": "Haarlem",
  "Address": "A. Hofmanweg 5a, 2031 BH Haarlem"
 },
 {
  "LOCATION": "Hardenberg",
  "Address": "Nijverheidsstraat 7, 7772 TP Hardenberg"
 },
 {
  "LOCATION": "Harderwijk",
  "Address": "Middelste Wei 4, 3844 HT Harderwijk"
 },
 {
  "LOCATION": "Harlingen",
  "Address": "Pr Irenestraat 2, 8862 TL Harlingen"
 },
 {
  "LOCATION": "Heemskerk",
  "Address": "Twaalfmaat 3 – 1967 PV Heemskerk"
 },
 {
  "LOCATION": "Heerenveen",
  "Address": "Weegbree 72, 8446 SC Heerenveen"
 },
 {
  "LOCATION": "Heerhugowaard",
  "Address": "Amatist 13, 1703 AP Heerhugowaard"
 },
 {
  "LOCATION": "Heerlen",
  "Address": "Snellius 1, 6422 RM Heerlen"
 },
 {
  "LOCATION": "Hellevoetsluis",
  "Address": "De Eik 68, 3224 TD Hellevoetsluis"
 },
 {
  "LOCATION": "Helmond",
  "Address": "Steenovenweg 5, 5708 HN Helmond"
 },
 {
  "LOCATION": "Hengelo",
  "Address": "Lansinkesweg 4, 7553 AE Hengelo"
 },
 {
  "LOCATION": "Hilversum",
  "Address": "Olympia 2D, 1213 NT Hilversum"
 },
 {
  "LOCATION": "Hoofddorp",
  "Address": "Saturnusstraat 46-62, 2132 HB Hoofddorp"
 },
 {
  "LOCATION": "Hoogeveen",
  "Address": "De Vos van Steenwijklaan 75, 7902 NP Hoogeveen"
 },
 {
  "LOCATION": "Hoogezand",
  "Address": "Pleiaden 21, 9602 KD Hoogezand"
 },
 {
  "LOCATION": "Hoorn",
  "Address": "Grote Beer 3, 1622 NS Hoorn"
 },
 {
  "LOCATION": "Houten",
  "Address": "Zonnehout 36, 3991 MX Houten. In het Wijkcentrum Schoneveld."
 },
 {
  "LOCATION": "Hulst",
  "Address": "Broodmarkt 8, 4561 CC Hulst"
 },
 {
  "LOCATION": "IJmuiden",
  "Address": "Oranjestraat 98, 1975 DD IJmuiden"
 },
 {
  "LOCATION": "Kampen",
  "Address": "Reijersdijk 2, 8262 CN Kampen"
 },
 {
  "LOCATION": "Leeuwarden",
  "Address": "Polluxweg 20, 8938 AZ, Leeuwarden"
 },
 {
  "LOCATION": "Leiden",
  "Address": "Schipholweg 103, 2316 XC Leiden"
 },
 {
  "LOCATION": "Lelystad",
  "Address": "Koningsbergenstraat 201, 8232 DC Lelystad"
 },
 {
  "LOCATION": "Lichtenvoorde",
  "Address": "Johannes Vermeerstraat 50, 7131 HD Lichtenvoorde. 06-83718263"
 },
 {
  "LOCATION": "Lisse",
  "Address": "Vivaldistraat 4, 2162 AA Lisse"
 },
 {
  "LOCATION": "Maarssen",
  "Address": "Langegracht 51, 3601 AK Maarssen"
 },
 {
  "LOCATION": "Maastricht",
  "Address": "Stationsplein 8K, 6221 BT Maastricht"
 },
 {
  "LOCATION": "Meppel",
  "Address": "Rembrandtplein 83, 7944 GC Meppel"
 },
 {
  "LOCATION": "Middelburg",
  "Address": "Johan van Reigersbergstraat 2, 4336 XA Middelburg"
 },
 {
  "LOCATION": "Middelharnis",
  "Address": "Voorstraat 15, 3241 EE Middelharnis"
 },
 {
  "LOCATION": "Mijdrecht",
  "Address": "Communicatieweg 9-3, 3641 SG Mijdrecht (sleutel ophalen bij nr 9-1)"
 },
 {
  "LOCATION": "Naaldwijk",
  "Address": "Bachlaan 1, 2671 TJ Naaldwijk"
 },
 {
  "LOCATION": "Nieuwegein",
  "Address": "Nevelgaarde 8, 3436 ZZ Nieuwegein"
 },
 {
  "LOCATION": "Nijmegen",
  "Address": "Groenestraat 294, 6531 JC Nijmegen"
 },
 {
  "LOCATION": "Noordwijk",
  "Address": "Achterzeeweg 1, 2201 BS Noordwijk"
 },
 {
  "LOCATION": "Oegstgeest",
  "Address": "Lijtweg 9, 2341 HA Oegstgeest"
 },
 {
  "LOCATION": "Ommen",
  "Address": "Ommerkanaal West 22, 7731 XR Ommen"
 },
 {
  "LOCATION": "Oosterhout",
  "Address": "Arkendonk 90, 4907 XP Oosterhout"
 },
 {
  "LOCATION": "Oss",
  "Address": "Wijkcentrum Schadewijk, Leeuwerikstraat 2, 5348 XA Oss"
 },
 {
  "LOCATION": "Purmerend",
  "Address": "Overlanderstraat 650, 1445 CW Purmerend"
 },
 {
  "LOCATION": "Raalte",
  "Address": "Boeierstraat 10, 8102 HS Raalte (Bedrijvencentrum Boei10)"
 },
 {
  "LOCATION": "Ridderkerk",
  "Address": "Sint Jorisstraat 6-8, 2981 GA Ridderkerk"
 },
 {
  "LOCATION": "Rijswijk",
  "Address": "Einsteinlaan 28, Rijswijk, 2289 CC"
 },
 {
  "LOCATION": "Roermond",
  "Address": "Prins Bernhardstraat 1, 6043 BG Roermond"
 },
 {
  "LOCATION": "Roosendaal",
  "Address": "Keijenburg 70, 4702 CG Roosendaal"
 },
 {
  "LOCATION": "Roosendaal Zaterdag",
  "Address": "Markt 54A, 4701 PH Roosendaal"
 },
 {
  "LOCATION": "Rotterdam West",
  "Address": "Tidemanstraat 80, 3022 SM Rotterdam"
 },
 {
  "LOCATION": "Rotterdam Zuid",
  "Address": "Clemensstraat 111, 3082 CE Rotterdam"
 },
 {
  "LOCATION": "Schagen",
  "Address": "Laan 21, 1741 EA Schagen"
 },
 {
  "LOCATION": "Sittard",
  "Address": "Stationsplein 1, 6131 AS Sittard"
 },
 {
  "LOCATION": "Sneek",
  "Address": "Koperslagersstraat 76, 8601 WP Sneek"
 },
 {
  "LOCATION": "Soest",
  "Address": "Willaertstraat 49, 3766 CP Soest"
 },
 {
  "LOCATION": "Spijkenisse",
  "Address": "Lenteakker 5A, 3206 TB Spijkenisse"
 },
 {
  "LOCATION": "Stadskanaal",
  "Address": "Scheepswerfstraat 5, 9501 NP Stadskanaal"
 },
 {
  "LOCATION": "Steenwijk",
  "Address": "De Vesting 11, 8332 GL Steenwijk"
 },
 {
  "LOCATION": "Terneuzen",
  "Address": "Stadhuisplein 3, 4531 RJ Terneuzen"
 },
 {
  "LOCATION": "Tiel",
  "Address": "Scheeringlaan 2, 4001 WJ Tiel"
 },
 {
  "LOCATION": "Tilburg",
  "Address": "Hart van Brabantlaan 12-14, Het Laken,, Tilburg, 5038 JL"
 },
 {
  "LOCATION": "Uden",
  "Address": "E27 Lichtfabriek, Frontstraat 2, 5405 PB Uden"
 },
 {
  "LOCATION": "Utrecht",
  "Address": "Herculesplein 221, 3584 AA Utrecht"
 },
 {
  "LOCATION": "Veenendaal",
  "Address": "Zonnebloemstraat 1, 3905 ZC Veenendaal"
 },
 {
  "LOCATION": "Veghel",
  "Address": "Middegaal 25, 5461 XB Veghel"
 },
 {
  "LOCATION": "Velp",
  "Address": "Den Heuvel 64, 6881 VE Velp"
 },
 {
  "LOCATION": "Velsen-Noord",
  "Address": "Heirweg 2, 1951 CD Velsen-Noord"
 },
 {
  "LOCATION": "Venlo",
  "Address": "Kaldenkerkerweg 20, 5913 AE Venlo"
 },
 {
  "LOCATION": "Venray",
  "Address": "Kiosk 5, 5802 NP Venray"
 },
 {
  "LOCATION": "Vlaardingen",
  "Address": "Rotterdamseweg 176, 3135 PT Vlaardingen"
 },
 {
  "LOCATION": "Vlissingen",
  "Address": "Industrieweg 1-3, 4382 NA Vlissingen"
 },
 {
  "LOCATION": "Weert",
  "Address": "Nieuwstraat 11, 6001 TV Weert"
 },
 {
  "LOCATION": "Winschoten",
  "Address": "Het Boschplein 2, 9671 GB Winschoten"
 },
 {
  "LOCATION": "Winterswijk",
  "Address": "Beatrixpark 22 7101 BN"
 },
 {
  "LOCATION": "Woerden",
  "Address": "Beneluxlaan 3, 3446 GS WOERDEN."
 },
 {
  "LOCATION": "Zaandam",
  "Address": "Klampersstraat 1, 1502 VP Zaandam"
 },
 {
  "LOCATION": "Zeist",
  "Address": "Stichting MeanderOmnium WSP Noord, Johan van Oldenbarneveltlaan 103, 3705 HD Zeist"
 },
 {
  "LOCATION": "Zierikzee",
  "Address": "Miereweg 3, 4301 SJ Zierikzee"
 },
 {
  "LOCATION": "Zoetermeer",
  "Address": "Boerhaavelaan 40, 2713 HX Zoetermeer"
 },
 {
  "LOCATION": "Zutphen",
  "Address": "Piet Heinstraat 11, 7204 JN Zutphen"
 },
 {
  "LOCATION": "Zwijndrecht",
  "Address": "Zwaluwstraat 1, 3334 XN Zwijndrecht"
 },
 {
  "LOCATION": "Zwolle",
  "Address": "Grote voort 293 A, 8041 BL Zwolle"
 }
]

# Function to get latitude and longitude using Google Maps Geocoding API
def get_lat_long(address, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None

# List to store the HTML list items
location_list_items = []

# Iterate through the JSON data and generate the HTML list items
for index, item in enumerate(json_data):
    address = item["Address"]
    location_name = item["LOCATION"]
    latitude, longitude = get_lat_long(address, api_key)
    print (address,location_name, latitude, longitude)
    if latitude is not None and longitude is not None:
        list_item = f'<li data-address="{address}" data-longitude="{longitude:.4f}" data-latitude="{latitude:.4f}" data-value="{index + 1}">{location_name} ({address})</li>'
        location_list_items.append(list_item)
    else:
        print(f"Could not geocode address: {address}")
    
    # Add a 2-second delay between each request
    time.sleep(2)

# Define the path to the Downloads folder
downloads_folder = os.path.expanduser('~/Downloads/')
output_file_path = os.path.join(downloads_folder, 'location_list.html')

# Write the generated list items to an HTML file
with open(output_file_path, 'w') as file:
    for item in location_list_items:
        file.write(f'{item}\n')

# Print the first few generated list items as a sample
for item in location_list_items[:5]:
    print(item)
