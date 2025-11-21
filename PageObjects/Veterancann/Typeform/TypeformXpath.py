class TypeformXpath():
    type_form_frame = "//div[@class='tf-v1-widget']//iframe"
    yes_btn = "//div[@data-value-string='have_conventional_treatment_taken-yes']"
    no_btn = "//div[@data-value-string='have_conventional_treatment_taken-no']"
    reset_btn = "//div[@data-value-string='c6036742-add4-4ac1-a64d-133ae34cd091']"
    i_use_cannabis_often = "//div[@data-value-string='372b0907-ede2-4764-81d5-f14c02da5c10']"
    select_true_btn = "//div[@data-value-string='3a88e9c4-63e7-4fda-ba3b-dacd8522c21f']"
    suffer_from_btn = "//div[@data-value-string='29f01f5e-20fa-4dc4-910e-1805d91146ab']"
    click_to_proceed_btn = "//div[@data-value-string='f3577e2f-4782-4dd4-a2fe-d0a84df3a121']"
    psycosis = "//div[@data-value-string='4ed148a3-218b-42c5-a0ef-62f5d49aa700']"
    care_plan = "//div[@data-value-string='9b3f6e0f-be0f-4144-9a77-b629c0aa020c-yes']"
    dva_textarea = "(//textarea)[1]"
    dva_ok_btn = "(//button)[2]"
    expiry_date = "//input[contains(@aria-describedby, 'short_text-dva_expiry_date')]"
    expiry_date_ok_btn = "(//button)[2]"
    chronic_pain = "//li[@aria-label='Chronic Pain']"
    injury = "//li[@aria-label='Injury']"
    ok_btn = "(//button)[2]"
    dva_card = "//div[@data-value-string='61a86511-87eb-4c4e-886f-67e23c202bad']"
    other_pain_yes_btn = "//div[@data-value-string='e2599bad-c5af-4dc0-bd91-b98c75309722']"

    pain_area = {
        "head": "(//input[@name='53388b4b-2bf8-4317-8c5d-cf5df0f117c8'])",
        "face": "(//input[@name='1ad1626b-dede-4d26-9fc5-925f5410e562'])",
        "neck": "(//input[@name='b49b7569-11b5-44d1-8bd4-ab65b27cb3b1'])",
        "shoulder": "(//input[@name='0458af5c-2ef8-466f-91cf-552d4b5544be'])",
        "chest": "(//input[@name='577bd91e-afc2-4b23-91a2-90e08c6c94ff'])",
        "upper_back": "(//input[@name='dafc19bb-dd3f-44e6-b2e7-526f21fda1f1'])",
        "mid_back": "(//input[@name='f9f0fec5-fc3e-49e3-9170-12e1395bd9a6'])",
        "lower_back": "(//input[@name='cc0f35e3-1a9e-467a-8e57-d046795eab2e'])",
        "abdomen": "(//input[@name='7cf6e5a2-8e5f-4313-8524-435a436354fa'])",
        "groin": "(//input[@name='f8a95e6f-7ee6-4944-a637-e92beed41058'])",
        "hip": "(//input[@name='65174b68-e7ce-4fb2-8f7a-2435540e44b9'])",
        "buttock": "(//input[@name='c42179fe-0de9-4ae1-afaa-5574e0bf19ba'])",
        "quad": "(//input[@name='967a283c-2c8b-4dcf-807c-9ac4cbe895bf'])",
        "knee": "(//input[@name='14ad5672-5cfc-410b-88e5-d6808e1180ac'])",
        "shin": "(//input[@name='56542f52-472c-48a3-8cac-aa4917dfad69'])",
        "calf": "(//input[@name='3683d8a3-3192-4afd-b7e4-efe9e52f1baa'])",
        "foot": "(//input[@name='b943508c-9730-486f-bbf0-64cdf35f0583'])",
        "bicep": "(//input[@name='e9f4f16b-dec2-43ef-9adf-3d6d0326f374'])",
        "elbow": "(//input[@name='449071d4-58d3-434b-9c40-8d2a386b44d8'])",
        "forearm": "(//input[@name='90e22b25-6279-439a-916b-7ac371845149'])",
        "hand": "(//input[@name='8d3a76f6-a6c3-4393-aa57-6d7db933608d'])"
    }
    rate_pain = {
        "worst": "(//input[@name='9d399772-d076-4dca-b893-a330997c460f'])[3]",
        "least": "(//input[@name='9bfd873b-08ac-4f7b-95d8-a110a600f839'])[5]",
        "average": "(//input[@name='a727a8bd-cd53-45a6-8a17-10dc6b31b17e'])[7]",
        "right_now": "(//input[@name='27805cee-4e35-4084-ae9f-e1612a22aa21'])[9]"
    }
    rate_pain_ok_btn = "(//button[@class='ButtonWrapper-sc-__sc-1qu8p4z-0 fElwmG'])[2]"
    bpi_24hr_dropdown = "//button[@aria-label='Show options']"
    bpi_option = "(//ul//li)[5]"
    past_24hr_pain = {
        "general_activity": "(//input[@name='8458b311-2006-4fd6-acb6-7a6c41c933b0'])[1]",
        "mood": "(//input[@name='b9e5ac28-ec5f-4e46-b71c-2a54da5ba770'])[2]",
        "walking_ability": "(//input[@name='b9c08232-e1f5-413a-8ede-e465555fdeb6'])[3]",
        "normal_walk": "(//input[@name='a6b25475-4165-47c8-91c1-c2d5b42f0d6e'])[4]",
        "relationship": "(//input[@name='6f107cf8-b05f-4542-9c3c-e612c576e69e'])[5]",
        "sleep": "(//input[@name='8b727156-9056-4dc8-a86a-14610f711d08'])[6]",
        "enjoyment_of_life": "(//input[@name='69ace60c-1682-4930-886f-699af7b873a3'])[7]"
    }
    cssrs = {
        "Have you wished you were dead or wished you could go to sleep and not wakeup?": "(//input[@name='cac046ee-ba50-40ef-80e0-64296239ee97'])[2]",
        "Have you actually had any thoughts of killing yourself?": "(//input[@name='37bb4c3e-9398-4249-a0b6-3bb2a3edcd5d'])[1]",
        "Have you been thinking about how you might do this?": "(//input[@name='ea66b072-bff1-43ba-807d-e8d5b7795e0c'])[2]",
        "Have you had these thoughts and had some intention of acting on them?": "(//input[@name='733fe000-7d12-46a8-96b5-c05287115b45'])[1]",
        "Have you started to work out or worked out the details of how to kill yourself? Did you intend to carry out this plan?": "(//input[@name='f9843f32-c2c5-4b28-8bcf-3b5e40b28461'])[2]",
        "Have you ever done anything, started to do anything, or prepared to do anythingto end your life?": "(//input[@name='080900cd-f762-4b85-9d8c-af1983e518b6'])[1]",
        "If 'Yes' to the above Was this within the past three months?": "(//input[@name='ae046e09-d7ce-4d42-ae63-7a145aa4debf'])[2]"
    }
    dass_21 = {
        "I found it hard to wind down": "(//input[@name='8b21a19b-5d1b-4783-b2ae-917e4fd7aa53'])[1]",
        "I was aware of dryness of my mouth": "(//input[@name='773432c2-52d6-4463-91f3-ea4046b0e25f'])[2]",
        "I couldn't seem to experience any positive feelings at all": "(//input[@name='7ec34811-0cd0-489c-be61-7532257e9a2f'])[3]",
        "I experienced breathing difficulty (eg, excessively rapid breathing, breathlessness in the absence of physical exertion)": "(//input[@name='34d9e26d-7620-4e3c-a5ee-85bd35a5cff5'])[4]",
        "I found it difficult to work up the initiative to do things": "(//input[@name='5090746a-466a-4237-a2d4-fa4df20e8b7c'])[3]",
        "I tended to over-react to situations": "(//input[@name='aa275559-6440-4c74-ada1-0be7257fbe99'])[2]",
        "I experienced trembling (eg, in the hands)": "(//input[@name='ad511530-c80d-4223-9dc4-45615a16fc46'])[1]",
        "I felt that I was using a lot of nervous energy": "(//input[@name='d5bcbfae-84f1-4571-8c0d-1b331421019e'])[2]",
        "I was worried about situations in which I might panic and make a fool of myself": "(//input[@name='324f0cfb-1135-4b2e-ad47-60473e5f93b3'])[3]",
        "I felt that I had nothing to look forward to": "(//input[@name='9ae2641f-f9fe-4535-9716-f1282015411f'])[4]",
        "I found myself getting agitated": "(//input[@name='b222d74a-0724-4b5e-b2de-a3b4b69f1e17'])[3]",
        "I found it difficult to relax": "(//input[@name='0f4e1d90-cfad-45da-aa01-70df704d732f'])[2]",
        "I felt down-hearted and blue": "(//input[@name='d0f9d164-6ad9-44ac-9ae1-1ff004141b94'])[1]",
        "I was intolerant of anything that kept me from getting on with what I was doing": "(//input[@name='828f75c0-e62d-4009-bf38-2b67443481de'])[2]",
        "I felt I was close to panic": "(//input[@name='89dfb0d1-0273-4e67-8e5d-f57a1c218528'])[3]",
        "I was unable to become enthusiastic about anything": "(//input[@name='ba6bea88-bd0f-4d3c-9dd7-eb2261e6626c'])[4]",
        "I felt I wasn't worth much as a person": "(//input[@name='d86d58dc-5708-4173-88f2-a0acab57be68'])[3]",
        "I felt that I was rather touchy": "(//input[@name='fae724a1-5515-4b84-a4d8-b5cfe9a10376'])[2]",
        "I was aware of the actions of my heart in the absence of physical exertion (eg, sense of heart rate increase, heart missing a beat)": "(//input[@name='902e2890-0b2f-4ae3-a8b3-719574dc77ca'])[1]",
        "I felt scared without any good reason": "(//input[@name='597c6894-50e1-47ab-9aa0-43646ebcd85d'])[2]",
        "I felt that life was meaningless": "(//input[@name='acd832c2-ac23-4864-8324-eb04cb28c70d'])[3]",
    }
    accept_declaration = "//div[@data-value-string='declaration_answers_2-accept']"
    medicare_textarea = "(//textarea)[1]"
    medicare_ok_btn = "//div[@id='block-99f9af4f-5355-4973-884f-c7cbef6db796']//button[@class='ButtonWrapper-sc-__sc-1qu8p4z-0 iVFzUR']"
    reference_textarea = "(//textarea)[1]"
    reference_ok_btn = "(//button)[2]"
    pain_btn = "//div[@data-value-string='c1307770-6990-44da-bfe2-366fc9d82b75']"
    radio_btn = "//div[@data-value-string='d48a36fe-716f-41cc-a41f-996af890d3c9']"
    i_accept_btn = "//div[@data-value-string='declaration_answers_2-accept']"
    i_dont_accept_btn = "//div[@data-value-string='declaration_answers_2-reject']"
    reject_validation = "//div[contains(text(),'Please agree to the terms & conditions')]"
    fname = "//input[@id='dd82c182-e018-45d0-92c4-37f608fd19d9']"
    lname = "//input[@id='d7ad48b6-ccf7-4034-9876-c8bc5b9ec985']"
    phone = "//input[@id='fee397cc-277d-41c3-933d-b9ca72e59946']"
    occupation = "//input[@placeholder='Type your answer here...']"
    gender = "//li[@aria-label='Male']"
    weight = "//input[contains(@id, 'number-weight')]"
    height = "//input[contains(@id, 'number-height')]"
    new_to_cannabis = "//li[@aria-label='I am new to cannabis. I would like to try medicinal cannabis as I am not benefiting from pharmaceutical medications and other therapies.']"
    conditions = "//input[@placeholder='Type your answer here...']"
    about_sleep = "//li[@aria-label='I always sleep well']"
    diagnosed_year = "//input[contains(@id, 'number-yeardiagnosed')]"
    select_sensitive = "//li[@aria-label='Yes']"
    describe_sensitive_from = "//input[@placeholder='Type your answer here...']"
    comfortable_method = "//div[@data-value-string='fac561a5-10ef-4744-9fb3-fe4dadb2c7fa']"
    previously_funded = "//div[@data-ref='currentmedicines']//li[@aria-label='Yes']"
    pain_medication = "//input[contains(@aria-labelledby, 'short_text-treatments_or_medications_for_pain')]"

