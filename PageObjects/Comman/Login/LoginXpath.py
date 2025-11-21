class LoginPageXpath():
    log_in_now_link = "//a[normalize-space()='Log In Now']"
    email_address = "//input[@id='id_username']"
    password = "//input[@id='id_password']"
    login_btn = "//input[@id='submit-id-']"
    logout_btn = "//a[@class='nav-link pe-0 align-middle ps-1']//span[@class='text-white d-inline']"
    login_link = "(//a[@href='/accounts/logout/'])[2]"
    wrong_login = "//li[contains(text(),'Password incorrect - Please enter a correct email ')]"