### Data project Module 1
# Country Job analysis 

![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

## Alejandra Matías Martín

Bootcamp: Ironhack - Data Analytics Part Time Nov 2020

Data project Module 1
---

	

## Datasources

There are 3 different datasources involved:

- <strong>Tables (.db): </strong> the main dataset.

- <strong>API:</strong> from the Open Skilss Project <http://dataatwork.org/data/>.

- <strong>Web Scraping: </strong> It is required to retrieve information about country codes from Eurostat website <https://ec.europa.eu/eurostat/statistics-explained/index.php/Glossary:Country_codes>


## :clipboard: Instructions

In this project we are going to create a Data Pipeline that retrieves the following table:

| Country       | Job Title      | Gender | Quantity | Percentage |
| :-----------: |:-------------: | :-----:| :-------:| :---------:|
| Spain         | Data Scientist | Female | 25       | 5%         | 
| Spain         | Data Scientist | Male   | 25       | 5%         |

In order to achieve this, we are going to follow these steps: 
- [x] Create repository
- [x] README.md
- [x] Connection to database (.db)
- [x] Cleaning data
- [x] Connection to API
- [x] Web scrapping
- [x] Merge dataframes
- [ ] Provide two options to the final user to select when executing: get the table of all countries/specify one.
- [x] Create csv files containing the dataframes
___
### :computer: **Technology stack**
- Python
- Pandas
- Sqlalchemy
- BeautifulSoup


## :file_folder: Folder structure
```
└── project
    ├── __trash__
    ├── .gitignore
    ├── .env
    ├── README.md
    ├── main_script.py
    ├── cleaning_raw.ipynb
    |
    ├── p_acquisition
    │   ├── m_acquisition.py
    │   └── __init__.py
    |
    |── p_wrangling
    |    ├── m_wrangling.py
    |    ├── __init__.py
    |   
    ├── p_analysis
    │   ├── m_analysis.py
    │   └── __init__-py
    ├── p_reporting
    │   ├── m_analysis.py
    │   └── __init__.py
    |__ results
    |
    └── data
        ├── raw
        ├── processed
    
```
	
---

## :love_letter: Contact
> Email: <alejandramatias32@gmail.com>
> Teléfono: 626118167
