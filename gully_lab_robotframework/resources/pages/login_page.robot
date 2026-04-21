*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/login_locators.robot

*** Variables ***
${given_mail}    azadsr158@gmail.com
${given_pass}    Pranjal@123

*** Keywords ***
Login Page
    [Arguments]    ${given_email}    ${given_pass}
    Input Text    ${email}  ${given_mail}
    Input Text    ${password}    ${given_pass}
    Click Button    ${click}
    
    Page Should Contain Element    xpath=//a[@href="/account"]
    Page Should Contain Element   xpath=//a[@href="/account/logout"]

    sleep  5s



    
    