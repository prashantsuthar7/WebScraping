import re
import requests

#https://searchenginesmarketer.com/company/resources/university-college-list/

def extract_email_addresses(urls):
  email_pattern = r'[\w\.-]+@[\w\.-]+'
  phones_pattern = r'\(?\d{3}\)?[\s-]?\d{3}[\s-]?\d{4}'
  for url in urls:
    response = requests.get(url)
    emails = re.findall(email_pattern, response.text)
    phones = re.findall(phones_pattern, response.text)
    for email in emails:
      #print(email)
      for phone in phones:
        print(url,email, phone)

#Example usage
extract_email_addresses(['https://www.arapahoe.edu/','http://uafs.edu/', 'http://artinstitutes.edu/'])

