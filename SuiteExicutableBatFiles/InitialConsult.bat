
@echo off

set currentDir=%cd%
echo %currentDir%
cd../../

pytest ./smartData2/InitialConsult/test_004Nurse_upcoming_consults.py --alluredir=allure-results

rmdir /s /q allure-report

allure generate --single-file ./allure-results ./allure-results/html

