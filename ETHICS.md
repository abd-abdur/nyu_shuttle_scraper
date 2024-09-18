ETHICS.md

Purpose of Data Collection:
I am collecting shuttle schedules and service dates from the NYU Transportation webpage. The goal is to provide users with convenient access to transportation schedules for the Fall 2024 semester making it easier for students and staff to plan their travel.

Data Sources and robots.txt
The data is scraped from a publicly available webpage on the NYU website:
https://www.nyu.edu/life/travel-and-transportation/university-transportation/routes-and-schedules.html.

Respect for robots.txt:
I have reviewed the robots.txt file at https://www.nyu.edu/robots.txt and confirmed that this page is not disallowed for scraping. All the scraping activities adhere to the site's terms and policies. No restricted or disallowed areas are accessed.

Collection Practices:
To minimize server load, I implemented a 3-second delay between requests using time.sleep(3) in the script. This helps to ensure that the scraper is polite and does not overload the website.

No Bypassing Password Protection:
I am only scraping publicly available data and am not bypassing any authentication mechanisms or password-protected areas.

Data Handling and Privacy:
The script strictly scrapes public information related to shuttle schedules. I do not collect any user data or personally identifiable information (PII).

Secure Data Storage:
Any scraped data is securely stored within the project repository. Sensitive data is excluded from the repository using a  gitignore file to ensure privacy and security.

Data Usage:
This project is solely for educational purposes as part of a web scraping class assignment. The scraped data is not being used for commercial purposes or distributed to any third parties. The project’s aim is to demonstrate web scraping techniques in a responsible and ethical manner.
