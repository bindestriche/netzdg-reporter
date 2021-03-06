# -*- coding: utf-8 -*-
!pip install webdriver-manager selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager



urls="""https://www.pinterest.de/pin/123/
https://www.pinterest.de/pin/456/
""".split()




driver = webdriver.Chrome(ChromeDriverManager().install())







for url in urls:
    driver.get("https://www.pinterest.de/suspension-appeal/netzdg/")
    reporter_name="not needed"
    reporter_email="your@mail.address"
    reporter_phone="012345678910"
    reporter_adress="not needed"


    namefield = driver.find_element_by_id("name")
    namefield.send_keys(reporter_name)

    mailfield = driver.find_element_by_id("email")
    mailfield.send_keys(reporter_email)

    phonefield = driver.find_element_by_id("phone")
    phonefield.send_keys(reporter_phone)

    addressfield = driver.find_element_by_id("address")
    addressfield.send_keys(reporter_adress)


    reported_url=driver.find_element_by_id("reported_url")
    reported_url.send_keys(url)

    report_image=driver.find_element_by_id("portion-pin_image")
    report_image.click()


    report_symbol=driver.find_element_by_id("checkbox-Verwenden von Kennzeichen verfassungswidriger und terroristischer Organisationen (§ 86a StGB)")
    report_symbol.click()

    report_Volksverhetzung=driver.find_element_by_id("checkbox-Volksverhetzung (§ 130 StGB)")
    report_Volksverhetzung.click()

    report_Propaganda=driver.find_element_by_id("checkbox-Verbreiten von Propagandamitteln verfassungswidriger und terroristischer Organisationen (§ 86 StGB)")
    report_Propaganda.click()


    report_is_accurate=driver.find_element_by_id("is_accurate")
    report_is_accurate.click()

    report_terms=driver.find_element_by_id("terms")
    report_terms.click()

    report_comment=driver.find_element_by_id("additional_details")

    report_understood=driver.find_element_by_id("understood_consequences")
    report_understood.click()
    driver.find_element_by_xpath("//button[@type='submit']").click()

#driver.close()
