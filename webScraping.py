import requests
from bs4 import BeautifulSoup

def scrape_jobs():
    url = "https://www.indeed.com/jobs?q=Python+Developer"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = []
    for job in soup.find_all('div', class_='jobsearch-SerpJobCard'):
        title = job.find('h2', class_='title').text.strip()
        company = job.find('span', class_='company').text.strip()
        location = job.find('div', class_='location').text.strip()
        salary = job.find('span', class_='salaryText')
        salary = salary.text.strip() if salary else 'N/A'
        
        job_listings.append({
            'title': title,
            'company': company,
            'location': location,
            'salary': salary
        })
    
    return job_listings

    jobs = scrape_indeed_jobs("Python Developer", "New York")
    