import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_login_link(browser):
    browser.maximize_window()
    browser.get(link)
    #time.sleep(30) #Раскоментировать, что бы визуально увидеть кнопку добавления в корзину
    button = len(browser.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/form/button"))
    assert button > 0, 'Button is not at page'

