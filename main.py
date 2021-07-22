from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.binary_location = "/usr/bin/google-chrome"
# chrome_driver_binary = "/usr/bin/chromedriver"
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
driver = webdriver.Chrome()

first_question = input("Do you want a camera?(y or n): ")
if first_question.lower() == "y":
    cheap = input("Do you want the cheapest?(y or n): ")
    if cheap.lower() == "y":
        print("This is the camera for you!")
        driver.get('https://smile.amazon.com/IEBRT-Vlogging-Rechargeable-Portable-Gifts%EF%BC%88Black%EF%BC%89/dp/B08PKRBRZ6/ref=sr_1_4?dchild=1&keywords=digital+camera&qid=1625162956&refinements=p_72%3A1248879011&rnid=10705423011&s=photo&sr=1-4')
    else:
        beginner = input("Do you want a beginner's camera?(y or n): ")
        if beginner.lower() == "y":
            print("This is the camera for you!")
            driver.get('https://smile.amazon.com/2-7K-Digital-Camera-Pixels-Vlogging/dp/B093D25W21/ref=sr_1_20?dchild=1&keywords=digital+camera&qid=1625163001&refinements=p_72%3A1248879011&rnid=10705423011&s=photo&sr=1-20')
        else:
            underwater = input("Do you want an underwater camera?(y or n): ")
            if underwater.lower() == "y":
                print("This is the camera for you!")
                driver.get('https://smile.amazon.com/Underwater-Waterproof-Digital-Recording-Snorkeling/dp/B0932P349W/ref=sr_1_16?dchild=1&keywords=digital+camera&qid=1625163001&refinements=p_72%3A1248879011&rnid=10705423011&s=photo&sr=1-16')
            else:
                optical_zoom = input("Do you want optical zoom?(y or n): ")
                if optical_zoom.lower() == "y":
                    print("This is the camera for you!")
                    driver.get('https://smile.amazon.com/Canon-PowerShot-Digital-Camera-Optical/dp/B019UDIAI6/ref=sr_1_6?dchild=1&keywords=digital+camera&qid=1625162956&refinements=p_72%3A1248879011&rnid=10705423011&s=photo&sr=1-6#HLCXComparisonWidget_feature_div')
                else:
                    print("This is the camera for you!")
                    driver.get('https://smile.amazon.com/Canon-Rebel-T7-18-55mm-II/dp/B07C2Z21X5/ref=sr_1_10?dchild=1&keywords=digital+camera&qid=1625163001&refinements=p_72%3A1248879011&rnid=10705423011&s=photo&sr=1-10#HLCXComparisonWidget_feature_div')
else:
    print("Until next time!")