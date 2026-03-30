*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/javascript_alerts

*** Test Cases ***
Simple Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Sleep    3s
    Click Button    xpath=//*[@id="content"]/div/ul/li[1]/button
    Sleep    2s
    Handle Alert
    Sleep    1s
    Close Browser

confirm Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Sleep    3s
    Click Button    xpath=//*[@id="content"]/div/ul/li[2]/button
    Sleep    2s
#    Handle Alert
#    Handle Alert  action=DISMISS
    Input Text Into Alert    Nik  action=DISMISS
    Sleep    1s
    Close Browser


