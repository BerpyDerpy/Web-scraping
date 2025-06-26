import requests
from bs4 import BeautifulSoup          #
import csv

URL = "https://github.com/trending"

response = requests.get(URL)
if response.status_code != 200:
    raise Exception("Failed to load page")

soup = BeautifulSoup(response.text, "html.parser")

# find all repo entries

repos = soup.find_all("article", class_="Box-row")
topRepos = []

for repo in repos[:5]:
    header = repo.find("h2")
    link = header.find("a")

    repoName = link.get_text(strip=True) #remove whitespace
    relative_URL = link["href"]
    repo_URL = "https://github.com" + relative_URL

    topRepos.append((repoName,repo_URL))

with open("github_scrape.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Repo Name", "link"])
    for name, link in topRepos:
        writer.writerow([name,link])

print("Saved")
