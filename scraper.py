import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://realpython.github.io/fake-jobs/"

# Send request to website
response = requests.get(url)

# Read website HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all job cards
jobs = soup.find_all("div", class_="card-content")

# Empty list to store jobs
job_data = []

# Loop through each job
for job in jobs:

    # Get title
    title = job.find("h2", class_="title").text.strip()

    # Get company
    company = job.find("h3", class_="company").text.strip()

    # Get location
    location = job.find("p", class_="location").text.strip()

    # Get link
    link = job.find_all("a")[1]["href"]

    # Store data
    job_data.append({
        "Title": title,
        "Company": company,
        "Location": location,
        "Link": link
    })

# Convert to table
df = pd.DataFrame(job_data)

# Print output
print(df)

# Save CSV file
df.to_csv("jobs.csv", index=False)

print("CSV file saved successfully!")
