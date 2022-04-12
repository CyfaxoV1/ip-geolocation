import requests 

ip_address = input("Masukan IP Address : ")

url = f"http://ip-api.com/json/{ip_address}"

reg = requests.get(url)
if reg.status_code == 200:
	res = reg.json()
	for k in res:
		print(f"{k.upper()} : {res[k]}")
		if k == "lon":
			map_zoom = 9
			map_url = f"https://www.google.com/maps/@{res['lat']},{res['lon']},{map_zoom}z"
			print(map_url)