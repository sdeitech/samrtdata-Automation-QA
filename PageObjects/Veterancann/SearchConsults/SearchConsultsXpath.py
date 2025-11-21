class SearchConsultsXpath():
    search_box = "//input[contains(@placeholder,'Search name or email ...')]"
    review_application_btn = "//button[@type='submit'][normalize-space()='Review Application'][1]"
    view_pending_prescription = "//tr[1]/td[5]/a[normalize-space()='View Pending Prescription']"
    mark_as_missed_btn = "//button[normalize-space()='Mark As Missed']"

    patient_summary_text = "//h1[contains(text(),'Patient Summary')]"
    read_missed_consults_number = "//a[contains(@href,'/doctor/upcoming-consults')]/span[2]"
    missed_patient_name =  "//table[@id='datatable']/tbody/tr/td/a"
    missed_patient_status = "//table[@id='datatable']/tbody/tr/td[3]/span[1]"

    view_profile = "//tbody/tr[1]/td[1]/a[1]"
    naviagtion_drpdwn = "//div[@role='button']"