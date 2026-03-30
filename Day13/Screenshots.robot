*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://in.bookmyshow.com/explore/events-jaipur?cat=CT
*** Test Cases ***
screenshsots
    Set Screenshot Directory    ${CURDIR}/../screenshots
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s
    
    Capture Page Screenshot    fullpage.png
    Sleep    2s
    Capture Element Screenshot    xpath=//*[@id="super-container"]/div/div[2]/div[3]/div[2]/div[4]/div/div/div[2]/a[1]/div/div[1]/div/img
    Sleep    2s

    Close Browser