
@echo off

set currentDir=%cd%
echo %currentDir%
cd../../

pytest ./smartData2/Patient/test_001Patient_signup.py --alluredir=allure-results

rmdir /s /q allure-report

allure generate --single-file ./allure-results ./allure-results/html --clean
