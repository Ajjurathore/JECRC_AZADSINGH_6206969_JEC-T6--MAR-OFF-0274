*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Simple Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Sleep    3s
    Click Button    xpath=//*[@id="alertBtn"]
    Sleep    2s
    Handle Alert
    Sleep    1s
    Close Browser

confirm Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Sleep    3s
    Click Button    xpath=//*[@id="confirmBtn"]
    Sleep    2s
    Handle Alert
#    Handle Alert  action=DISMISS
#    Input Text Into Alert    Nik  action=DISMISS
    Sleep    1s
    Close Browser


promt Alert
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Sleep    3s
    Click Button    xpath=//*[@id="promptBtn"]
    Sleep    2s
#    Handle Alert
    Input Text Into Alert    ram jane
    Sleep    1s

    Close Browser