
@echo off

set currentDir=%cd%
echo %currentDir%
cd../../

pytest ./Dispensed/Support/test_004SupportPage.py --alluredir=allure-results

rmdir /s /q allure-report

allure generate --single-file ./allure-results ./allure-results/html
