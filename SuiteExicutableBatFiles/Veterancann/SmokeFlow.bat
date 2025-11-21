
@echo off

set currentDir=%cd%
echo %currentDir%
cd../../

pytest ./smartData2/Patient-Nurse-Approver-smoke-flow/test_004Nurse_upcoming_consults.py --alluredir=allure-results

rmdir /s /q allure-report

allure generate --single-file ./allure-results ./allure-results/html --clean
