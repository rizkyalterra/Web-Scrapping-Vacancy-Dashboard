from pathlib import Path
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import csv
import re
import scrapy
import math



class GermanSpider(scrapy.Spider):
    name = "german"
    file_name_csv = 'data.csv'
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

    def start_requests(self):
        urls = [
            # "https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=5124db82f6497b75b3000009&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]=0&form_main_search[size]=18&form_main_search[jobs_on_page_count]=0&form_main_search[vacancies_count]=0",
            # "https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=522d9870f6497b2d39000016&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]=0&form_main_search[size]=18&form_main_search[jobs_on_page_count]=0&form_main_search[vacancies_count]=0",
            # "https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=2d085ee5-244a-49fa-b326-418c2758fef9&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]=0&form_main_search[size]=18&form_main_search[jobs_on_page_count]=0&form_main_search[vacancies_count]=0",
            # "https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=522d879af6497bfe6b00002b&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]=0&form_main_search[size]=18&form_main_search[jobs_on_page_count]=0&form_main_search[vacancies_count]=0",
            "https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=5c5cd3b2-9fb0-413b-b2a8-63737d64e543&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]=0&form_main_search[size]=18&form_main_search[jobs_on_page_count]=0&form_main_search[vacancies_count]=0",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        if self.type == self.search and self.dataId == 0 :
            self.total_count_job = response.css("div.js-search-result-title").attrib["data-vacancies-count"]
            self.count_page_job = math.ceil(int(self.total_count_job) / 18) - 1
            self.tempDetailPage = response.css("div.js-job-postings article")
            url = "https://www.ausbildung.de"+self.tempDetailPage[0].css("a").attrib["href"]
            self.type = self.saveJob
            yield scrapy.Request(url=url, callback=self.parse, meta={'url' : url})
        elif self.type == self.search:
            self.tempDetailPage = response.css("div.js-job-postings article")
            url = "https://www.ausbildung.de"+self.tempDetailPage[0].css("a").attrib["href"]
            self.type = self.saveJob
            yield scrapy.Request(url=url, callback=self.parse, meta={'url' : url})
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

            if len(self.tempDetailPage) > 1:
                self.tempDetailPage.pop(0)
                url = "https://www.ausbildung.de"+self.tempDetailPage[0].css("a").attrib["href"]
                yield scrapy.Request(url=url, callback=self.parse, meta={'url' : url})
            elif self.count_page_job > 0:
                self.page = self.page + 18
                # url = f"https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=5124db82f6497b75b3000009&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]={self.page}&form_main_search[size]=18&form_main_search[jobs_on_page_count]={self.page}&form_main_search[vacancies_count]=0"
                # url = f"https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=522d9870f6497b2d39000016&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]={self.page}&form_main_search[size]=18&form_main_search[jobs_on_page_count]={self.page}&form_main_search[vacancies_count]=0"
                # url = f"https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=2d085ee5-244a-49fa-b326-418c2758fef9&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]={self.page}&form_main_search[size]=18&form_main_search[jobs_on_page_count]={self.page}&form_main_search[vacancies_count]=0"       
                url = f"https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=522d879af6497bfe6b00002b&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]={self.page}&form_main_search[size]=18&form_main_search[jobs_on_page_count]={self.page}&form_main_search[vacancies_count]=0"
                # url = f"https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=5c5cd3b2-9fb0-413b-b2a8-63737d64e543&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]={self.page}&form_main_search[size]=18&form_main_search[jobs_on_page_count]={self.page}&form_main_search[vacancies_count]=0"
                self.type = self.search
                self.count_page_job = self.count_page_job - 1
                yield scrapy.Request(url=url, callback=self.parse)

    def closed(self, reason):
        # conn_db = initDB()
        # cursor_db = conn_db.cursor()
        # for index, data in enumerate(self.dataCSV):
        #     query = """INSERT INTO data (resources_id, title, url, graduation, salary, description) 
        #     VALUES (%s, %s, %s, %s, %s, %s"""
        #     cursor_db.execute(query, (self.resources_id, data[1], data[2], data[3], data[4], data[5]))
        #     conn_db.commit()
        # cursor_db.close()
        # conn_db.close()
        with open(self.file_name_csv, 'w', newline='') as file_csv:
            writer = csv.writer(file_csv, delimiter=';', lineterminator='\n')
            writer.writerows(self.dataCSV)
    