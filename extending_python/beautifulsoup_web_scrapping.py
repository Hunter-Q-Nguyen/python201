import requests

page = requests.get("https://247ctf.com/scoreboard")
#print(page.text) # This will print the HTML content of the page


### Using BeautifulSoup to parse the HTML content
from bs4 import BeautifulSoup

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.text)
# print(soup.title.name) # This will print the name of the title tag
# print(soup.title.string) # This will print the content of the title tag
# print(soup.find("a")) # This will find the first anchor tag in the HTML content

for line in soup.find_all("a"):
    print(line)
    print(line.get("href")) # This will print the href attribute of the anchor tag

# print(50*"-")
# print(soup.find(id="fetch-error")) # This will find the element with id "fetch-error"
# print(soup.find(class_="nav-link")) # This will find the first element with class "nav-link"
# print(soup.find("a", class_="nav-link")) # This will find the first anchor tag with class "nav-link"

### Extract specific ranking from the scoreboard
print(50*"-")
table = soup.find("table")
table_body = table.find("tbody")
fows = table_body.find_all("tr")

for row in fows:
    print("---")
    # print(row)
    cols = [x.text.strip() for x in row.find_all("td")]
    # print(cols)
    print("{} is in {} place with {}.".format(cols[2], cols[0], cols[4]))
