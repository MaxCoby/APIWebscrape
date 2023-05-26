import requests
from bs4 import BeautifulSoup
import re

names = []
grades = []
genders = []
days_until_birthday = []
birthdays = []
days_until_birthday_sorted = []
cities = {}

url = "https://knightbook.menloschool.org"

human_headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                 "accept-language": "en-US,en;q=0.9",
                 "accept-encoding": "gzip, deflate, br",
                 "upgrade-insecure-requests": "1",
                 "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.183 Safari/537.36 Vivaldi/1.96.1147.64"
                 }

session = requests.Session()

response = session.get(url, headers=human_headers)

# print(response.text)

response_bs = BeautifulSoup(response.text, "html.parser")

login_page = response_bs.form['action']
# print(login_page)

login_method = response_bs.form['method']
# print(login_method)

inputList = response_bs.findAll('input')
# print(inputList)

login_inputs = {}
for tag in inputList:
    if 'name' in tag.attrs:
        login_inputs[tag['name']] = tag.get('value', '')
# print(tag.attrs)
# print(login_inputs)

login_inputs['username'] = 'redacted'
login_inputs['password'] = 'redacted'

# print(response.headers)
# print(response.status_code)
# print(response.history)
# print(response.history[0].headers)
# print(response.history[0].headers['Location'])
location = response.history[0].headers['Location']

server = re.match("^(https://\w+\.\w+\.\w{1,3}:?\d*)[/a-zA-Z]*", location).group(1)

kb = session.post(server + login_page, data=login_inputs)
bsObj = BeautifulSoup(kb.text, "html.parser")

information = bsObj.findAll("div", {"class" : "student-box"})

for i in range(0, len(information)):
    names.append(information[i]["data-name"])
    grades.append(information[i]["data-grade"])
    genders.append(information[i]["data-gender"])
    days_until_birthday.append(int(information[i]["data-days-until-birthday"]))

    html = session.get("https://knightbook.menloschool.org/get_student_info.php?lookup=student_detail&id=" + information[i]["data-rid"])
    bsObj = BeautifulSoup(html.text, "html.parser")

    match = re.compile(r"(?<=<br/>).*(?=,)")
    city = match.search(str(bsObj))[0]
    if city in cities:
        cities[city] += 1
    else:
        cities[city] = 1

    birthdays.append(bsObj.findAll("div")[-1].text)

days_until_birthday_sorted = [b[0] for b in sorted(enumerate(days_until_birthday),key=lambda i:i[1])]
cities = sorted(cities.items(), key=lambda x: int(x[1]), reverse=True)

for i in range(0, 10):
    index = days_until_birthday_sorted[i]
    name = names[index]
    grade = grades[index]
    gender = genders[index]
    birthday = birthdays[index]
    print ("Name: " + name + "\nGrade Level: " + grade + "\nGender: " + gender + "\nBirthday: " + birthday + "\n")

for city in cities:
    print ("Number of students from " + city[0] + ": " + str(city[1]))