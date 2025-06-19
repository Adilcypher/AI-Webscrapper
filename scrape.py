import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time 
from bs4 import BeautifulSoup

def scrape_website(website):
    print('Launching Web browser..')

    driver_path = "chromedriver.exe"
    #Setting rules in the way we want to access the chrome driver 
    #eg:while scrapping ignore the images etc...
    options = webdriver.ChromeOptions()
    #Setting the actual driver in this case google chorme
    #Services: Path to the driver for scrapping 
    #options: Follows the rule for scrapping 
    driver = webdriver.Chrome(service = Service(driver_path),options= options)


    try:
        driver.get(website)
        print('Page Loaded...')
        html = driver.page_source
        time.sleep(10)
        return html 
    
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,'html.parser')
    #takes the <body></body> tag
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""

#This function will clean the text
#Cleans: unnecessary scripts,style,backspaces,tab etc so that we only reterive
#the important information 
def clean_body_content(body_content):
    #Will help to perform DOM 
    soup = BeautifulSoup(body_content,'html.parser')
    
    for script_or_style in soup(['script','style']):
        script_or_style.extract()
    #adding new line after the text is retreated 
    cleaned_content = soup.get_text(separator='\n')
    #.splitlines(): create a list of lines from the content
    #.strip(): removing trailing and forward whitespaces
    #.split(): filter the spaces in between
    #\n.join: While just tiddy everthing up and join the lines 
    cleaned_content = '\n'.join(line.strip() for line in cleaned_content.splitlines() if line.split())

    return cleaned_content


def split_dom_content(dom_content,max_length = 6000):

    return [
        dom_content[i: i + max_length] for i in range(0,len(dom_content),max_length)
    ]

