import requests

url = 'https://raw.githubusercontent.com/Albert-Jonas/pelda_project/Albert_branch/Nevek.txt'
response = requests.get(url)

if response.status_code == 200:
    names = response.text.split('\n')
    for name in names:
        print(name.upper())
else:
    print('Error occurred while fetching data')
