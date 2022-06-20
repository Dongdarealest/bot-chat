import requests
import os
OKGREEN = '\033[92m'
ENDC = '\033[0m'
os.system("clear")
while True:
 nd = str(input("Tao: "))
 ssm = requests.get("https://api.simsimi.net/v2/?text="+nd+"&lc=vn").json()
 ph = ssm["success"]
 if ph == "T\u00f4i kh\u00f4ng bi\u1ebft b\u1ea1n \u0111ang n\u00f3i g\u00ec. H\u00e3y d\u1ea1y t\u00f4i" :
  print(OKGREEN + "simsimi: Nói tiếng người đi mày" + ENDC)
 else:
  print(OKGREEN+"simsimi: "+ ph + ENDC)
