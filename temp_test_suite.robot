*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Open google.com
    Open Browser    browser=chrome
    Go To    url=https://www.google.com

