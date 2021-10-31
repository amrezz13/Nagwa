from bs4 import BeautifulSoup
import requests
import pandas as pd



'''
    function to scrape table returning data frame
'''


def scrapper(url):
    page = requests.get(url)  # request html
    soup = BeautifulSoup(page.text, 'html.parser')  # soup object to go throw html

    table = soup.find('table', {'class': 'wikitable'})  # search for tag table which class is BLA BLA

    df = pd.read_html(str(table))
    # convert list to dataframe
    df = pd.DataFrame(df[0])

    df = df.drop(["الرواية", "البلد", "الترتيب"], axis=1)
    df = df.rename(columns={"الاسم": "name", "المؤلف": "author"})

    links = []
    for name in df['name']:
        for data in table.find_all('td'):
            row_data = [td.text.strip() for td in data]
            row_data = data.text.strip()    # don't delete it
            if row_data == name:
                for a in data.find_all('a', href=True):
                    link = a['href']
                    links.append('https://www.marefa.org'+link)
    df['link'] = links

    return df
