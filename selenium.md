# Selenium

[SeleniumHQ WebElement](https://seleniumhq.github.io/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html)


## Python

[Selenium-Python](http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.firefox.webdriver)

FirefoxWebElement:
	: elemento.get_attribute('class') )
	: elemento.get_attribute('innerHTML') )
	: elemento.is_displayed() )
	: elemento.find_element_by_xpath('..') )
	: elemento.find_element_by_xpath('..').get_attribute('class') 
	: student = WebDriverWait( driver, retraso ).until( EC.element_to_be_clickable((By.CLASS_NAME, 'student')), 'Enlace al curso no es clickable' )
	: student.click()
	: mi_unidad = WebDriverWait( driver, retraso ).until( EC.element_to_be_clickable((By.ID, 'section-1')), 'Buff' )
	: titu = mi_unidad.find_element_by_class_name("activityinstance").find_element_by_tag_name("a")
	: titu.click()