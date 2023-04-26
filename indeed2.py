import datetime
import time
import pandas as pd
from bs4 import BeautifulSoup
import warnings
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime
dt = str(datetime.now().strftime("%Y_%m_%d___[%I_%M_%S_%p]"))
warnings.filterwarnings("ignore")

def driver_conn():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")      # Make the browser Headless. if you don't want to see the display on chrome just uncomment this
    chrome_options.add_argument("--log-level=3")    # Removes error/warning/info messages displayed on the console
    chrome_options.add_argument("--disable-infobars")  # Disable infobars ""Chrome is being controlled by automated test software"  Although is isn't supported by Chrome anymore
    chrome_options.add_argument("start-maximized")     # Make chrome window full screen
    chrome_options.add_argument('--disable-gpu')       # Disable gmaximizepu (not load pictures fully)
    # chrome_options.add_argument("--incognito")       # If you want to run browser as incognito mode then uncomment it
    chrome_options.add_argument("--disable-notifications")  # Disable notifications
    chrome_options.add_argument("--disable-extensions")     # Will disable developer mode extensions

    # chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    # chrome_options.add_argument('--proxy-server=%s' % PROXY)
    # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)   #we have disabled pictures (so no time is wasted in loading them)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)  # you don't have to download chromedriver it will be downloaded by itself and will be saved in cache
    return driver



# ================================================================================
#                         Getting Links
# ================================================================================
def get_url():
    print('==================== Getting URL ====================')
    all_link = []
    driver = driver_conn()
    # ---------------  Can put your country url by this format  -----------------
    url = "https://uk.indeed.com/jobs?q="
    df = pd.read_csv("input.csv")
    keywords = df['Keyword'].values
    locations = df['Location'].values
    print('Total Input: ' + str(len(keywords)))
    ll = 0
    for i in range(0, len(df)):
        ll += 1
        print('Getting link ' + str(ll) + ' out of ' + str(len(keywords)))
        keyword = keywords[i]
        location = locations[i]
        pag = 0
        check = 0
        while True:
            print(">>>>>>>>>>>>>>>>>>>>>> Page: " + str(pag))
            driver.get(url + str(keyword) + str("&l=") + str(location) + str("&start=") + str(pag))
            time.sleep(3)
            pag += 10
            if check > 3:
                break
            soup = BeautifulSoup(driver.page_source, 'lxml')
            try:
                lis = soup.find('ul', {'class': 'jobsearch-ResultsList'}).find_all('div', {'class': 'cardOutline'})
            except:
                lis = ''
            print("Listing here: ", len(lis))
            if len(lis) < 1:
                break
            for li in lis:
                link = ''
                name = ''
                address = ''
                company = ''
                salary = ''
                date = ''
                try:
                    f_url = str(url).split('/jobs?q=')[0]
                    link = str(f_url) + li.find('h2', {'class': 'jobTitle'}).find('a')['href']
                except:
                    pass
                try:
                    name = li.find('h2', {'class': 'jobTitle'}).text.replace('\n', '').strip()
                except:
                    pass
                try:
                    address = li.find('div', {'class': 'companyLocation'}).text.replace('\n', '').strip()
                except:
                    pass
                try:
                    company = li.find('span', {'class': 'companyName'}).text.replace('\n', '').strip()
                except:
                    pass
                try:
                    salary = li.find('div', {'class': 'salary-snippet-container'}).text.replace('\n', '').strip()
                except:
                    pass
                try:
                    date = li.find('span', {'class': 'date'}).text.replace('\n', '').replace('Posted', '').replace('Employer', '').strip()
                except:
                    pass
                data = {
                    'links': link,
                    'Name': name,
                    'Address': address,
                    'Company': company,
                    'Salary': salary,
                    'Date': date,
                }
                # print("Link length", len(link))
                if data not in all_link:
                    all_link.append(data)
                    df = pd.DataFrame(all_link)
                    df = df.rename_axis("Index")
                    df.to_csv('url.csv', encoding='utf-8-sig')
                else:
                    check += 1
            df = pd.DataFrame(all_link)
            df = df.rename_axis("Index")
            df.to_csv('url.csv', encoding='utf-8-sig')
    driver.close()



def get_data():
    print('=================== Data Scraping Started ===================')
    all_data = []
    driver = driver_conn()
    df = pd.read_csv("url.csv")
    links = df['links'].values
    names = df['Name'].values
    addresss = df['Address'].values
    companies = df['Company'].values
    salaries = df['Salary'].values
    dates = df['Date'].values
    print('Total link: ' + str(len(links)))
    d = 0
    for i in range(0, len(df)):
        d += 1
        print('Getting Data: ' + str(d) + ' out of ' + str(len(links)))
        link = links[i]
        name = names[i]
        address = addresss[i]
        company = companies[i]
        salary = salaries[i]
        date = dates[i]

        driver.get(link)
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        description = ''
        try:
            description = soup.find('div', {'id': 'jobDescriptionText'}).text.strip()
        except:
            pass
        data = {
            'links': link,
            'Name': name,
            'Address': address,
            'Company': company,
            'Salary': salary,
            'Date': date,
            'Description': description,
        }
        all_data.append(data)
        df = pd.DataFrame(all_data)
        df = df.rename_axis("Index")
        df.to_csv('Data___(' + dt + ').csv', encoding='utf-8-sig')
    df = pd.DataFrame(all_data)
    df = df.rename_axis("Index")
    df.to_csv('Data___(' + dt + ').csv', encoding='utf-8-sig')
    driver.close()


if __name__ == '__main__':
    get_url()
    get_data()