import requests
import os

original_directory = os.getcwd()
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

base_url = "https://randomuser.me/api/portraits/{gender}/{num}.jpg"
base_file_name = "pics/{gender}/{num}.jpg"

for i in range(99):
    for gender in ["men", "women"]:
        r = requests.get(base_url.format(gender=gender, num=i))
        with open(base_file_name.format(gender=gender, num=i), "wb") as f:
            f.write(r.content)

os.chdir(original_directory)