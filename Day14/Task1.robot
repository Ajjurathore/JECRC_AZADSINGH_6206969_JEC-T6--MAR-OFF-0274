*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handle Popup Window
    Open Browser    ${url}    chrome
    Maximize Browser Window
    Scroll Element Into View    xpath=//button[contains(text(),'Popup')]
    Sleep    2s
    ${windows}=    Get Window Handles
    ${parent}=    Set Variable    ${windows}[0]
    Click Element    xpath=//button[contains(text(),'Popup')]
    Sleep    2s
    Switch Window    NEW
    ${title}=    Get Title
    Log To Console    ${title}
    Close Window
    Switch Window    ${parent}
    Element Should Contain    xpath=//h1    Automation Testing Practice
    Close Browser