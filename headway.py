import csv
from selenium.webdriver.common.by import By
import time
from seleniumbase import Driver

driver = Driver(uc=True)

with open('test.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(">>> ", row[0])
        driver.get(row[0])
        time.sleep(2)

        page = 1
        while(True):
            print(">>>>>>>>>>>>>>>>>> ", page, " >>>>>>>>>>>>>>>>>>>>>>>>")

            firstDate = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[1]/div[1]').text
            firstDate = firstDate.replace("\n", ", ")
            print("firstDate >>> ", firstDate)

            firstcount = 0
            while(True):
                try:
                    # print("--- ", firstcount, " ---")
                    meetings = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[1]/div[2]/div/div/div[1]/div/div')
                    meetingTime = meetings[firstcount].text
                    if meetingTime == "More" :
                        meetings[firstcount].click()
                    else :
                        # print("Meeting Time >>> ", meetingTime)
                        firstcount += 1
                except:
                    break
            print("first count >>> ", firstcount)
            try:
                secondDate = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[2]/div[1]').text
                secondDate = secondDate.replace("\n", ", ")
                print("secondDate >>> ", secondDate)

                secondcount = 0
                while(True):
                    try:
                        # print("--- ", secondcount, " ---")
                        meetings = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div/div')
                        meetingTime = meetings[secondcount].text
                        if meetingTime == "More" :
                            meetings[secondcount].click()
                        else :
                            # print("Meeting Time >>> ", meetingTime)
                            secondcount += 1
                    except:
                        break
                print("second count >>> ", secondcount)
            except:
                print("No second date")
            try:
                thirdDate = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[3]/div[1]').text
                thirdDate = thirdDate.replace("\n", ", ")
                print("thirdDate >>> ", thirdDate)

                thirdcount = 0
                while(True):
                    try:
                        # print("--- ", thirdcount, " ---")
                        meetings = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[3]/div[2]/div/div/div[1]/div/div')
                        meetingTime = meetings[thirdcount].text
                        if meetingTime == "More" :
                            meetings[thirdcount].click()
                        else :
                            # print("Meeting Time >>> ", meetingTime)
                            thirdcount += 1
                    except:
                        break
                print("third cound >>> ", thirdcount)
            except:
                print("No third date")

            nextButton = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/button[2]')
            if (nextButton.get_attribute("disabled")):
                break
            else:
                nextButton.click()
                page += 1

        # price_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div[1]/div[2]/section[3]/div[1]/div[1]/div[1]')
        # price = price_element.text
        # print(price)