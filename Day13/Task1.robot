*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://testautomationpractice.blogspot.com/


*** Test Cases ***
Handle multiselect
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Scroll Element Into View    xpath=//*[@id="colors"]

    Page Should Contain List    id=colors
    
    ${options}  Get List Items    id=colors
    Log To Console    ${options}

    Select From List By Label    id=colors  Red
    Select From List By Label    id=colors  Blue             +
    
    ${selected_options}=  Get Selected List Labels    id=colors
    Log To Console    ${selected_options}

    List Selection Should Be    id=colors  @{selected_options}

    Sleep    3s
    Close Browser

