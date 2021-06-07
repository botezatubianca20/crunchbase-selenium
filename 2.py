# De pe site-ul http://www.crunchbase.com/ , pentru o companie oarecare, extrageti locatia companiei, numărul de angajați, website-ul și totalul fondurilor primite.
from selenium import webdriver

url = 'https://www.crunchbase.com/organization/softbank'

driver = webdriver.Chrome(executable_path=r"C:\chromedriver.exe")
driver.get(url)

ul = driver.find_element_by_class_name("section-content")
elementList = ul.find_elements_by_tag_name("li")
location = elementList[3].text
nr_employees = elementList[1].text
website = elementList[4].text
total_funds = driver.find_elements_by_xpath("/html/body/chrome/div/mat-sidenav-container/mat-sidenav-content/div/ng-component/entity-v2/page-layout/div/div/div/page-centered-layout[2]/div/row-card/div/div[2]/profile-section/section-card/mat-card/div[2]/div/anchored-values/div[6]/a/div/field-formatter/span")[0].text

print(f'Locatia companiei: {location} \n Nr angajati: {nr_employees} \n Website: {website} \n Totalul fondurilor primite:: {total_funds}')


