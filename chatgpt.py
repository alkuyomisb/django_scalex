import requests
from bs4 import BeautifulSoup

url = "https://www.ooredoo.om/Personal/Mobile/Hala(Prepaid).aspx"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Send a request to the webpage with headers
response = requests.get(url, headers=headers, verify=False)

# Parse the HTML content of the webpage using BeautifulSoup with lxml or html5lib parser
soup = BeautifulSoup(response.content, "lxml")

# Find the table containing the data packages
table = soup.find("table", {"class": "plans-table"})

# Extract the package details from the table rows
package_details = []
for row in table.find_all("tr")[1:]:  # skip the header row
    columns = row.find_all("td")
    package_name = columns[0].text.strip()
    package_data = columns[1].text.strip()
    package_price = columns[2].text.strip()
    package_validity = columns[3].text.strip()
    package_details.append(
        (package_name, package_data, package_price, package_validity))

# Print the package details
for package in package_details:
    print("Package Name: ", package[0])
    print("Package Data: ", package[1])
    print("Package Price: ", package[2])
    print("Package Validity: ", package[3])
    print("---------------------")
