

class SignUpPageXpath():

    email = "//input[@id='id_email']"
    fname= "//input[@id='id_first_name']"
    lname = "//input[@id='id_last_name']"
    dob = "//input[@id='id_dob']"
    mail_addr = "//input[@id='id_mailing_address_placeholder']"
    mail_addr_list = "(//div//span[text()='Sydney Harbour Bridge'])[1]"
    phone = "//input[@id='id_phone']"
    male_btn = "//input[@id='id_gender_1']"
    next_step_btn = "//button[normalize-space()='Next Step']"
    password = "//input[@id='id_password1']"
    password_confirmation = "//input[@id='id_password2']"
    signup_btn = "//button[normalize-space()='Sign Up']"
    invalid_dob = "//strong[normalize-space()='Enter a valid date.']"
    duplicate_email = "//div[@class='invalid-feedback d-block']"
    wrong_password = "//div[@class='invalid-feedback d-block']"
    female_btn = "//input[@id='id_gender_1']"
    other_btn = "//input[@id='id_gender_2']"
    password_condition_message = "//div[@class='invalid-feedback d-block']"
    email_exists_text_element = "//div[@class='invalid-feedback d-block']"
    age_limit_text_element = "//div[@class='invalid-feedback d-block']"