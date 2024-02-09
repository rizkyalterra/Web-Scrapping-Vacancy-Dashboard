from abc import abstractmethod
from pathlib import Path
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import csv
import re
import scrapy
import math
import mysql.connector



class Core(scrapy.Spider):


    db_config = {
        'host': "db4free.net",
        'user': "alterra",
        'password': "alterra123",
        'database': "stock_news",
    }

    resources_id = 0

    result_count_languange_programming = {}
    keyword_languange_programming_tech = [
        "Python",
        "Java",
        "JavaScript",
        # "C",
        "C++",
        "C#",
        "Swift",
        "Objective-C",
        "Kotlin",
        "Ruby",
        "PHP",
        "HTML",
        "CSS",
        "SQL",
        # "R",
        "Go",
        "TypeScript",
        "Dart",
        "Rust",
        "Shell",
        "Scala",
        "Perl",
        "Haskell",
        "Lua",
        "Matlab",
        "Groovy",
        "Assembly",
        "VB.NET",
        ".NET",
        "Node.js",
        "React",
        "Angular",
        "Vue.js",
        "Express.js",
        "Django",
        "Flask",
        "Spring",
        "Laravel",
        "ASP.NET",
        "Firebase",
        "MongoDB",
        "MySQL",
        "PostgreSQL",
        "SQLite",
        "AWS",
        "Azure",
        "Docker",
        "Kubernetes",
        "Git",
        "GitHub",
        "Bitbucket",
        "Jenkins",
        "Travis CI",
        "JIRA",
    ]

    dataCSV = [
        ["Id", "Title", "Url", "Graduation", "Salary", "Description"],
    ]
    dataId = 0
    iterationMain = 1
    search = "search"
    detail = "detail"
    saveJob = "saveJob"
    type = search
    total_count_job = 0
    count_page_job = 0
    page = 0
    tempDetailPage = []
    
    def parse(self, response, _callback = None):
        print("Core Handler")
        if self.type == self.search and self.dataId == 0 :
            self.total_count_job = response.css("div.js-search-result-title").attrib["data-vacancies-count"]
            self.count_page_job = math.ceil(int(self.total_count_job) / 18) - 1
            self.tempDetailPage = response.css("div.js-job-postings article")
            url = "https://www.ausbildung.de"+self.tempDetailPage[0].css("a").attrib["href"]
            self.type = self.saveJob
            if _callback:
                print("Callback")
                _callback(url)
            # yield scrapy.Request(url=url, callback=self.parse, meta={'url' : url})
        # elif self.type == self.search:
        #     self.tempDetailPage = response.css("div.js-job-postings article")
        #     url = "https://www.ausbildung.de"+self.tempDetailPage[0].css("a").attrib["href"]
        #     self.type = self.saveJob
        #     yield scrapy.Request(url=url, callback=self.parse, meta={'url' : url})
        elif self.type == self.saveJob:
            self.dataId = self.dataId + 1
            url = response.meta.get('url')
            title = response.css("html head title::text").get()
            education = response.css("html body div.l-wrapper main div div.ab-container div.ab-grid div.vacancy-grid div.vacancy-grid__b div.jp-facts div.facts-list ul.facts-list__facts li.facts-list__fact")[2].css("li div div span::text")[1].get()
            description = response.css("html body div.l-wrapper main div div.ab-container div.ab-grid div.vacancy-grid div.vacancy-grid__c").get()
            salary = "-"
            if response.css('html body div.l-wrapper main div div.ab-container div.ab-grid div.vacancy-grid div.vacancy-grid__c div.jp-salary'):
                for salary_item in response.css("html body div.l-wrapper main div div.ab-container div.ab-grid div.vacancy-grid div.vacancy-grid__c div.jp-salary div.facts-list ul.facts-list__facts li.facts-list__fact"):
                    salary = salary + salary_item.css("li.facts-list__fact div.fact__content span::text")[0].get() + " => " + salary_item.css("li.facts-list__fact div.fact__content span::text")[1].get() + "; "

            description_clean = re.sub('<.*?>', '', description)
            description_clean = description_clean.replace(';', '')
            description_clean = ' '.join(description_clean.split())
            
            title = GoogleTranslator(source='de', target='en').translate(title)
            education = GoogleTranslator(source='de', target='en').translate(education)
            if len(description_clean) > 5000:
                description_clean = description_clean[:4900]  
            description_clean = GoogleTranslator(source='de', target='en').translate(description_clean)
            salary = GoogleTranslator(source='de', target='en').translate(salary)
            
            dataTempItemCSV = []
            dataTempItemCSV.append(self.dataId)
            dataTempItemCSV.append(title)
            dataTempItemCSV.append(url)
            dataTempItemCSV.append(education)
            dataTempItemCSV.append(salary)
            dataTempItemCSV.append(description_clean)
            self.dataCSV.append(dataTempItemCSV)

            # if len(self.tempDetailPage) > 1:
            #     self.tempDetailPage.pop(0)
            #     url = "https://www.ausbildung.de"+self.tempDetailPage[0].css("a").attrib["href"]
            #     yield scrapy.Request(url=url, callback=self.parse, meta={'url' : url})
            # elif self.count_page_job > 0:
            #     self.page = self.page + 18
            #     self.type = self.search
            #     self.count_page_job = self.count_page_job - 1
            #     yield scrapy.Request(url=url, callback=self.parse)

    # def insertDB(self):
        # conn_db = mysql.connector.connect(**self.db_config)
        # cursor_db = conn_db.cursor()
        # for index, data in enumerate(self.dataCSV):
        #     query = """INSERT INTO data (resources_id, title, url, graduation, salary, description) 
        #     VALUES (%s, %s, %s, %s, %s, %s"""
        #     cursor_db.execute(query, (self.resources_id, data[1], data[2], data[3], data[4], data[5]))
        #     conn_db.commit()
        # cursor_db.close()
        # conn_db.close()
        # with open(self.file_name_csv, 'w', newline='') as file_csv:
        #     writer = csv.writer(file_csv, delimiter=';', lineterminator='\n')
        #     writer.writerows(self.dataCSV)
    