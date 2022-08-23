class Logger_page:
    #filter xpaths
    filter_dropdown_btn = "//span[.='Filter']"
    filter_language = "//p[.='Language']"
    filter_Campaign_Name = "//p[.='Campaign Name']"
    filter_Region = "//p[.='Region']"
    filter_Flow = "//p[.='Flow']"
    filter_Call_Duration = "//p[.='Call Duration']"
    filter_Disposition = "//p[.='Disposition']"
    filter_Status = "//p[.='Status']"
    filter_Attempt = "//p[.='Attempt']"

    #DateRange
    Calender_icon = "//img[@alt='Calendar Icon']"


    #download
    download_report = "//img[@alt='Download']"

    def __init__(self, driver):
        self.driver = driver