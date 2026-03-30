*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
Handle dropdown
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//*[@id="content"]/ul/li[11]/a
    Sleep    2s

#    Page Should Contain Element    xpath=//*[@id="dropdown"]
    Page Should Contain List    xpath=//*[@id="dropdown"]
    Sleep    1s

    ${options}=  Get List Items    id=dropdown
    Log To Console    ${options}

    Select From List By Label  id=dropdown    Option 1
    
    ${select_options}=  Get Selected List Label    id=dropdown
    Log To Console    ${select_options}

    List Selection Should Be    id=dropdown  Option 1    # varifies the correct select

    Sleep    2s

    Close Browser





