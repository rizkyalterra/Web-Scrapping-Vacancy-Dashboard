from pathlib import Path
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import csv
import re
import scrapy


class ArrQuotesSpider(scrapy.Spider):
    name = "quotes"
    file_name_csv = 'data.csv'

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
        ["Id", "Judul", "Url", "Lulusan", "Description", "Gaji"],
    ]
    dataId = 0

    def start_requests(self):
        urls = [
            "https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=5124db82f6497b75b3000009&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]=0&form_main_search[size]=18&form_main_search[jobs_on_page_count]=0&form_main_search[vacancies_count]=0",
            # "https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=5124db82f6497b75b3000009&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]=18&form_main_search[size]=18&form_main_search[jobs_on_page_count]=18&form_main_search[vacancies_count]=0",
            # "https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=5124db82f6497b75b3000009&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]=36&form_main_search[size]=18&form_main_search[jobs_on_page_count]=36&form_main_search[vacancies_count]=0"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)
        # print("HASIL TEKNOL")
        # for kunci, nilai in self.result_count_languange_programming.items():
        #     print(f"{kunci}: {nilai}")


    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f"page-{page}.html"
        # Path(filename).write_bytes(response.body)
        # self.log(f"Saved file {filename}")
        # self.parse_detail_page(response)
        # print("Mulai Page Home")
        total_count_job = response.css("div.js-search-result-title").attrib["data-vacancies-count"]
        count_page_job = int(int(total_count_job) / 18)
        page = 0
        print("Mulai Awal")
        for i in range(count_page_job):
            url = f"https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=5124db82f6497b75b3000009&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]={page}&form_main_search[size]=18&form_main_search[jobs_on_page_count]={page}&form_main_search[vacancies_count]=0"
            page = page + 18
            print(i)
            if i == 0:
                yield scrapy.Request(url=url, callback=self.parse_detail_page, priority=page, dont_filter=True)
            else:
                yield scrapy.Request(url=url, callback=self.parse_detail_page, priority=page)
            # break

    def parse_detail_page(self, response):
        # print("Mulai Detail Page Home")
        for quote in response.css("div.js-job-postings article"):
            url = "https://www.ausbildung.de"+quote.css("a").attrib["href"]
            yield scrapy.Request(url="https://www.ausbildung.de"+quote.css("a").attrib["href"], callback=self.parse_detail_posting_job, meta={'url' : url})
            # break
            # print(quote.css("a.job-posting-cluster-cards__link div.job-posting-cluster-cards__wrapper div.job-posting-cluster-cards__body h3::text").get())
            # print(quote.css("a.job-posting-cluster-cards__link div.job-posting-cluster-cards__wrapper div.job-posting-cluster-cards__body h3::text").get())

    def parse_detail_posting_job(self, response):
        # page = response.url.split("/")[-2]
        # filename = f"detail-{page}.html"
        # Path(filename).write_bytes(response.body)
        
        data = []
        self.dataId = self.dataId + 1
        url = response.meta.get('url')
        title = response.css("html head title::text").get()
        education = response.css("html body div.l-wrapper main div div.ab-container div.ab-grid div.vacancy-grid div.vacancy-grid__b div.jp-facts div.facts-list ul.facts-list__facts li.facts-list__fact")[2].css("li div div span::text")[1].get()
        description = response.css("html body div.l-wrapper main div div.ab-container div.ab-grid div.vacancy-grid div.vacancy-grid__c").get()
        salary = "-"
        if response.css('html body div.l-wrapper main div div.ab-container div.ab-grid div.vacancy-grid div.vacancy-grid__c div.jp-salary'):
            for salary_item in response.css("html body div.l-wrapper main div div.ab-container div.ab-grid div.vacancy-grid div.vacancy-grid__c div.jp-salary div.facts-list ul.facts-list__facts li.facts-list__fact"):
                salary = salary + salary_item.css("li.facts-list__fact div.fact__content span::text")[0].get() + " => " + salary_item.css("li.facts-list__fact div.fact__content span::text")[1].get() + "; "

        # soup = BeautifulSoup(description, 'html.parser')
        # description_clean = soup.get_text()
        description_clean = re.sub('<.*?>', '', description)
        description_clean = description_clean.replace(';', '')
        # description_clean = description_clean.replace('\n', ' ')
        description_clean = ' '.join(description_clean.split())
        # title_id = GoogleTranslator(source='de', target='en').translate(title)
        # education_id = GoogleTranslator(source='de', target='en').translate(education)
        # description_id = GoogleTranslator(source='de', target='en').translate(description_clean)
        
        dataTempItemCSV = []
        dataTempItemCSV.append(self.dataId)
        dataTempItemCSV.append(url)
        dataTempItemCSV.append(title)
        dataTempItemCSV.append(education)
        dataTempItemCSV.append(description_clean)
        dataTempItemCSV.append(salary)
        self.dataCSV.append(dataTempItemCSV)


        # euro_pola_salary = r'\b€(\w+)\b'
        # salary_split = re.findall(euro_pola_salary, description)
        # salary_result = [item for item in salary_split]
        # dataTempItemCSV.append(salary_result)
        # self.dataCSV.append(dataTempItemCSV)

        # print("Mulai Detail")
        # print("Judul : " + title)
        # print("Pendidikan : " + education)
       
        # print("Deskripsi : " + descJob)
        # descJob = descJob.lower()
        # for keyword in self.keyword_languange_programming_tech:
        #     jumlah_kemunculan = descJob.count(keyword.lower())
        #     self.result_count_languange_programming[keyword] = jumlah_kemunculan
       
        # return self.result_count_languange_programming
    
    def closed(self, reason):
        # Metode ini akan dipanggil ketika spider selesai
        # print("HASIL TEKNOL")
        # print(self.result_count_languange_programming)

        # for kunci, nilai in self.result_count_languange_programming.items():
        #     print(f"{kunci}: {nilai}")
        with open(self.file_name_csv, 'w', newline='') as file_csv:
            writer = csv.writer(file_csv, delimiter=';', lineterminator='\n')
            writer.writerows(self.dataCSV)
    
    def hapus_tag_html(teks_html):
        soup = BeautifulSoup(teks_html, 'html.parser')
        teks_bersih = soup.get_text()
        return teks_bersih