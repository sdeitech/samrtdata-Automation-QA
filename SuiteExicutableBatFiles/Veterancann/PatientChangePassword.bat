
@echo off

set currentDir=%cd%
echo %currentDir%
cd../../

pytest ./smartData2/Patient/test_002Patient_change_password.py --alluredir=allure-results

rmdir /s /q allure-report

allure generate --single-file ./allure-results ./allure-results/html --clean
