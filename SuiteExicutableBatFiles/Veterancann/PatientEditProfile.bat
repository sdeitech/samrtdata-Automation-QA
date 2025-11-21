
@echo off

set currentDir=%cd%
echo %currentDir%
cd../../

pytest ./smartData2/Patient/test_003Patient_edit_profile.py --alluredir=allure-results

rmdir /s /q allure-report

allure generate --single-file ./allure-results ./allure-results/html --clean
