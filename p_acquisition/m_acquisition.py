import pandas as pd
from sqlalchemy import create_engine
from functools import reduce
import requests
from bs4 import BeautifulSoup as bs

# Importing database

def get_data():

    # Connecting to database

    print('Connecting to database...')
    path = "data/raw_data_project_m1.db"
    conn_str = f'sqlite:///{path}'
    engine = create_engine(conn_str)

    # Getting tables
    data_personal = pd.read_sql('SELECT * FROM personal_info', engine)
    data_country = pd.read_sql('SELECT * FROM country_info', engine)
    data_career = pd.read_sql('SELECT * FROM career_info', engine)
    data_poll = pd.read_sql('SELECT * FROM poll_info', engine)

    # Merging datatables
    data_list = [data_personal, data_country, data_career, data_poll]
    data_merged = reduce(lambda left, right: pd.merge(left, right, on='uuid'), data_list)
    print('Connected to the data base.')
    return data_merged

# Getting the unique job codes by transform them into a set
def get_jobs_id(data_merged):
    job_code_unique = set(data_merged['normalized_job_code'])
    print('Unique job codes obtained')
    return job_code_unique

# Connecting to the API
def get_jobs_api(data_merged, job_code_unique):
    print('Connecting to API...')
    jobs_list = []
    for code in job_code_unique:
        response = requests.get(f'http://api.dataatwork.org/v1/jobs/{code}').json()
        jobs_list.append(response)
    print('Creating dict job titles')
    uuid_job_list = []
    for x in jobs_list:
        try:
            uuid_job_list.append(x['uuid'])
        except:
            pass
    title_job_list = []
    for y in jobs_list:
        try:
            title_job_list.append(y['title'])
        except:
            pass
    dict_job_titles = dict(zip(uuid_job_list, title_job_list))
    print('Adding the data from the API to data_merged')
    data_merged['Job Title'] = data_merged['normalized_job_code']
    for uuid, title in dict_job_titles.items():
        data_merged.loc[data_merged['normalized_job_code'] == uuid, 'Job Title'] = title
    data_merged['Job Title'] = data_merged['Job Title'].fillna('Not working')
    print('Jobs from API obtained')
    return data_merged

# Web Scraping

def get_country_codes():
    print('Starting web scraping...')
    url = 'https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes'
    html = requests.get(url).content
    soup = bs(html, 'html.parser')
    table = soup.find('table')
    df_country_codes = pd.DataFrame(table)
    print('df_countries_codes created')
    fixed_df_country = []
    table_rows = table.find_all("tr")
    for tr in table_rows:
        datum = tr.find_all("td")
        for td in datum:
            fixed_df_country.append(td.text)
    print('Tds transformed into a list')
    fixed_df_country2 = []
    for i in fixed_df_country:
        m = i.replace('\n', '').replace('(', '').replace(')', '')
        fixed_df_country2.append(m)
    print('td list fixed')
    country_codes = []
    country_names = []
    for x in fixed_df_country2:
        if (len(x)) < 3:
            country_codes.append(x)
        else:
            country_names.append(x)
    dict_countries = dict(zip(country_names, country_codes))
    dict_countries['Great Britain'] = 'GB'
    dict_countries['Greece'] = 'GR'
    countries_df = pd.DataFrame(([key, dict_countries[key]] for key in dict_countries.keys()),
                             columns=['Country', 'country_code'])
    return countries_df


