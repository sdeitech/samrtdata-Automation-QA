
@echo off

set currentDir=%cd%
echo %currentDir%
cd../../

pytest ./Dispensed/Patient(BeforePerchaseTreatmentPlan) --alluredir=allure-results



rmdir /s /q allure-report

allure generate --single-file ./allure-results ./allure-results/html

