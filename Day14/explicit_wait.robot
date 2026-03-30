*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://practicetestautomation.com/practice-test-login/

*** Test Cases ***
Explicit
    Open Browser    ${url}  chrome

    Wait Until Element Is Visible    id = username
    Input Text    id=username  Password123

    Wait Until Element Is Visible    id=password
    Input Text    id=username  Password123

    Wait Until Element Is Enabled    submit
    Click Element    id=submit

    Wait Until Location Contains    logged-in-successfully
    Close Browser