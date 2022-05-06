import json
from selenium import webdriver
import utils

def set_driver(output_path):

    appState = {
        "recentDestinations": [
            {
                "id": "Save as PDF",
                "origin": "local",
                "account": ""
            }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
        "isHeaderFooterEnabled": False
    }

    profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState),
            'savefile.default_directory': output_path}

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('prefs', profile)
    chrome_options.add_argument('--kiosk-printing')    
    # chrome_options.add_argument('--headless')    

    # driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome(executable_path=f"{utils.get_file_path()}//driver//chromedriver.exe", options=chrome_options)    

    return driver
