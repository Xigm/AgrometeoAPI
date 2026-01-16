import requests, datetime, hashlib

# open .env to get your api key and shared secret
with open(".env", "r") as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith("API_KEY="):
            my_api_key = line.strip().split("=")[1]
        elif line.startswith("SHARED_SECRET="):
            my_shared_secret = line.strip().split("=")[1]

host= "https://www.vitimeteo.ch/" # or: vitimeteo.de, vitimeteo.fr, ...
my_api_key=my_api_key
my_shared_secret=my_shared_secret

req_time = datetime.datetime.timestamp(datetime.datetime.now())
sig = hashlib.md5(bytes("api_key=%s&secret=%s&time=%s" %(my_api_key, my_shared_secret, req_time), 'utf-8')).hexdigest()

#you have to send x-auth and x-req-ts headers
headers={"Content-type":"application/x-www-form-urlencoded", "Accept":"text/plain", "User-Agent":"python","x-auth":my_api_key+":"+sig, "x-req-ts":str(req_time)}
api_endpoint = "api/v3/"
# response = requests.get(host + api_endpoint , headers = headers)
# print(response.content)

url = host + api_endpoint
# get the list of available stations with names and IDs:
stationslist = requests.get(url+'stations', headers=headers).json()
print(stationslist)

# get the info for station ID 1:
station = requests.get(url+'stations/1', headers=headers).json()
print(station)

# get the full info for station ID 1: 
stationinfo = requests.get(url+'stationinfo/1', headers=headers).json() 
print(stationinfo)


# get weatherdata for station ID 1 for the last 3 days
daysback = 3
endDate = datetime.date.today()
startDate = endDate - datetime.timedelta(days=daysback)
sensor_list = [1, 4, 6] # Sensor=idDatatype. 1=Air Temperature, 4=relative Humidity, 6=Precipitations

# as json:
params = 'stations/1/weatherdata.json?startdate={}&enddate={}&sen_list={}'.format(startDate, endDate, sensor_list)
weatherdata = requests.get(url+params, headers=headers).json()
print(weatherdata)