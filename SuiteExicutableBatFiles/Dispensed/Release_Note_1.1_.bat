
@echo off

set currentDir=%cd%
echo %currentDir%
cd../../

pytest ./Dispensed/Approver/test_007Approver_dropdown_navigation.py --alluredir=allure-results

rmdir /s /q allure-report

allure generate --single-file ./allure-results ./allure-results/html

