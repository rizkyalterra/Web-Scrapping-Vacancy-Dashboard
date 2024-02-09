from pathlib import Path
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import csv
import re
import scrapy
import math

from appscrap.spiders.core import Core

class FachinformatikerSpider(Core):
    name = "fachinformatiker"
    url_format = "https://www.ausbildung.de/ajax/main_search/?form_main_search%5Brlon%5D=9.481544&form_main_search%5Brlat%5D=51.312801&form_main_search%5Bvideo_application_on%5D=&form_main_search%5Bshow_integrated_degree_programs%5D=0&form_main_search%5Bshow_educational_trainings%5D=0&form_main_search%5Bshow_qualifications%5D=0&form_main_search%5Bshow_regular_apprenticeships%5D=1&form_main_search%5Bshow_inhouse_trainings%5D=0&form_main_search%5Bshow_educational_trainings_and_regular_apprenticeships%5D=0&form_main_search%5Bshow_training_programs%5D=0&form_main_search%5Bradius%5D=1000&form_main_search%5Bmin_radius%5D=0&form_main_search%5Bprofession_public_id%5D=522d879af6497bfe6b00002b&form_main_search%5Bprofession_topic_public_id%5D=&form_main_search%5Bindustry_public_id%5D=&form_main_search%5Bexpected_graduation%5D=&form_main_search%5Bstarts_no_earlier_than%5D=&form_main_search%5Bsort_order%5D=relevance&form_main_search%5Bbreaker_tile%5D=true&form_main_search%5Bcorporation_promote_foreign_applications%5D=false&form_main_search%5Bwhat%5D=&form_main_search%5Bwhere%5D=&t_search_type=main&t_what=&t_where=&form_main_search[from]={page}&form_main_search[size]=18&form_main_search[jobs_on_page_count]={page}&form_main_search[vacancies_count]=0"
        
    def start_requests(self):
        self.url = self.url_format
        url_value = f"{self.url_format.format(page=self.page)}"
        yield scrapy.Request(url=url_value, callback=self.parse)

    def request(self, url):
        print("Hy Callback")
        print(url)
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        super().parse(response, self.request)

 
    # def close(self, reason):
    #     print(f"Closing spider due to: {reason}")
    #     super().close(reason)
    # def closed(self):
    #     self.insertDB()
    