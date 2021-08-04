from selenium import webdriver
chrome_driver_path = "C:\Drivers\chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.n11.com/urun/onvo-ov32f152-32-frameless-hd-ready-android-smart-led-tv-1948250?magaza=cantekno")

tittle = driver.find_element_by_class_name("proName").text
price = driver.find_element_by_class_name("newPrice").find_element_by_tag_name("ins").text
searchInput = driver.find_element_by_id("searchData").get_attribute("value")
kurumsallink = driver.find_element_by_xpath('//*[@id="footer"]/div/div[2]/div[2]/div/ul/li[1]/a').get_attribute("href")
logo = driver.find_element_by_css_selector(".home img").get_attribute("src")
print(tittle)
print(price)
print(searchInput)
print(kurumsallink)
print(logo)
driver.close()