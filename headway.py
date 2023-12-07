import csv
from selenium.webdriver.common.by import By
import time
import csv
from seleniumbase import Driver
driver = Driver(uc=True)

with open('URL.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        Region = row[0]
        driver.get(row[1])
        time.sleep(2)

        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        match=False
        while(match==False):
            lastCount = lenOfPage
            time.sleep(3)
            lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
            if lastCount==lenOfPage:
                match=True

        provider_links = []
        provider_elements = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div[1]/div[1]/a')
        for provider_element in provider_elements:
            provider_link = provider_element.get_attribute("href")
            provider_links.append(provider_link)
        for provider_link in provider_links:
            driver.get(provider_link)

            try:
                Name = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[1]/div[1]/div[2]/div[1]').text
                Name.replace("\n", "")
            except:
                Name = "Empty"

            try:
                title = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[1]/div[1]/div[2]/div[2]').text
            except:
                title = "Empty"

            try:
                state = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[1]/div[1]/div[2]/div[3]').text
            except:
                state = "Empty"

            try:
                Specializes_in = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[1]/section[1]/div[2]/div/div').text
                Specializes_in = Specializes_in.replace("\n", ", ")
            except:
                Specializes_in = "Empty"

            try:
                Accept_Insurance = driver.find_element(By.XPATH, '//*[@id="cost"]/div[2]/div').text
                if Accept_Insurance :
                    Accept_Insurance = "YES"
                    Insurance_carriers = Accept_Insurance.replace("\n", ", ")

                else:
                    Accept_Insurance = "No"
                    Insurance_carriers = " "
            except:
                Accept_Insurance = "Empty"
            
            try:
                In_network_with_Accepted_Insurances = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[1]/section[1]/div[1]/div/div').text
                In_network_with_Accepted_Insurances = In_network_with_Accepted_Insurances.replace("\n", ", ")
            except:
                In_network_with_Accepted_Insurances = "Empty"

            try:
                style_ALL = driver.find_element(By.XPATH, '//*[@id="style"]/div').text
                style_ALL = style_ALL.replace("\n", ", ")
            except:
                style_ALL = "Empty"

            try:
                price_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div[2]/div/div[1]/div[2]/section[3]/div[1]/div[1]/div[1]')
                price = price_element.text
            except:
                price="None"

            try:
                Min_Range = price.split("-")[0]
                Max_Range = "$" + price.split("-")[1]
            except:
                Min_Range = "Empty"
                Max_Range = "Empty"

            try:
                tests = driver.find_elements(By.CSS_SELECTOR, '#__next > div > div > main > div.css-1bjlo2e.evctw9v0 > div > div.css-qlhj95 > div.css-tgz829 > div.css-qbubgm > div.css-fk1h94> div')
                element_count = len(tests)
                if(element_count == 2):
                    In_person_sessions = "YES"
                    Virtual_sessions = "YES"
                elif(element_count == 1):
                    In_person_sessions = "No"
                    Virtual_sessions = "YES"
            except:
                In_person_sessions = "None"
                Virtual_sessions = "None"

            try:
                Degree = driver.find_element(By.XPATH, '//*[@id="more"]/div/div[1]/div[1]/span').text
            except:
                Degree = "Empty"

            try:
                License_type= driver.find_element(By.XPATH, '//*[@id="more"]/div/div[1]/div[2]/span').text
                License_type = License_type.split(": ")[1]
            except:
                License_type = "Empty"

            try:
                Gender = driver.find_element(By.XPATH, '//*[@id="more"]/div/div[1]/div[3]/span').text
                Gender = Gender.split(": ")[1]
            except:
                Gender = "Empty"

            try:
                Ethnicity = driver.find_element(By.XPATH, '//*[@id="more"]/div/div[1]/div[4]/span').text
                Ethnicity = Ethnicity.split(": ")[1]
            except:
                Ethnicity = "Empty"

            try:
                Language = driver.find_element(By.XPATH, '//*[@id="more"]/div/div[1]/div[5]/span').text
                Language = Language.split(": ")[1]
            except:
                Language = "Empty"

            try:
                Works_with = driver.find_element(By.XPATH, '//*[@id="more"]/div/div[1]/div[6]/span').text
                Works_with = Works_with.split(": ")[1]
            except:
                Works_with = "Empty"

            try:
                More_specialties = driver.find_element(By.XPATH, '//*[@id="more"]/div/div[1]/div[7]/span').text
                More_specialties = More_specialties.split(": ")[1]
            except:
                More_specialties = "Empty"     

            try:
                Modalities = driver.find_element(By.XPATH, '//*[@id="more"]/div/div[1]/div[8]/span').text
                Modalities = Modalities.split(": ")[1]
            except:
                Modalities = "Empty"

            try:
                Location = driver.find_element(By.XPATH, '//*[@id="more"]/div/div[2]/div[2]/span').text
                Location = Location.replace("\n", " ")
            except:
                Location = "Empty"
                
            days = []
            page = 1
            results = []

            while(True):
                try:
                    firstDate = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[1]/div[1]').text
                    firstDate = firstDate.replace("\n", ", ")
                    firstcount = 0
                    while(True):
                        try:
                            meetings = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[1]/div[2]/div/div/div[1]/div/div')
                            meetingTime = meetings[firstcount].text
                            if meetingTime == "More" :
                                meetings[firstcount].click()
                            else :
                                firstcount += 1
                        except:
                            break
                    days.append(firstcount)
                    try:
                        secondDate = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[2]/div[1]').text
                        secondDate = secondDate.replace("\n", ", ")
                        secondcount = 0
                        while(True):
                            try:
                                meetings = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[2]/div[2]/div/div/div[1]/div/div')
                                meetingTime = meetings[secondcount].text
                                if meetingTime == "More" :
                                    meetings[secondcount].click()
                                else :
                                    secondcount += 1
                            except:
                                break
                        days.append(secondcount)
                    except:
                        break
                    try:
                        thirdDate = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[3]/div[1]').text
                        thirdDate = thirdDate.replace("\n", ", ")
                        thirdcount = 0
                        while(True):
                            try:
                                meetings = driver.find_elements(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/div/div[3]/div[2]/div/div/div[1]/div/div')
                                meetingTime = meetings[thirdcount].text
                                if meetingTime == "More" :
                                    meetings[thirdcount].click()
                                else :
                                    thirdcount += 1
                            except:
                                break
                        days.append(thirdcount)

                        nextButton = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[2]/div/div[2]/div/div[2]/form/div/button[2]')
                        if (nextButton.get_attribute("disabled")):
                            break
                        else:
                            nextButton.click()
                            page += 1
                    except: 
                        break
                except:
                    days = [0]
                    break
            total = 0
            headers = ["State USED", "Profile URL", "Name", "Title", "State", "In-person Sessons", "Virtual session", "Accept Insurance", "In-network with/Accepted Insurances", "Specializes in", "Style ALL", "Cost FULL", "Min Range", "Max Range", "Insurance carriers", "DEGREE", "License type", "Gender", "Ethnicity", "language", "Works with", "More specialties", "Modalities", "Location", "TOTAL COUNT OF APPOINTMENTS 1st Day", "TOTAL COUNT OF APPOINTMENTS 2nd Day", "TOTAL COUNT OF APPOINTMENTS 3rd Day", "TOTAL COUNT OF APPOINTMENTS 4th Day", "TOTAL COUNT OF APPOINTMENTS 5th Day", "TOTAL COUNT OF APPOINTMENTS 6th Day", "TOTAL COUNT OF APPOINTMENTS 7th Day", "TOTAL COUNT OF APPOINTMENTS 8th Day", "TOTAL COUNT OF APPOINTMENTS 9th Day", "Total count of Appointments in all 9 Days"]
            results = [Region, provider_link, Name, title, state, In_person_sessions, Virtual_sessions, Accept_Insurance, In_network_with_Accepted_Insurances, Specializes_in, style_ALL, price, Min_Range, Max_Range, Insurance_carriers, Degree, License_type, Gender, Ethnicity, Language, Works_with, More_specialties, Modalities, Location]
            for i in range(0, 9):
                try:
                    day = days[i]
                except:
                    day = 0
                results.append(day)
                total = total+day

            results.append(total)

            with open('clients.csv', mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(results)
driver.close()    