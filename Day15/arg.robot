*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://sauce-demo.myshopify.com/account/login

*** Test Cases ***
Login
    Open Browser  ${url}  headlesschrome
    Login Success    Cheeseburger@gmail.com
    Sleep    2s

*** Keywords ***
Login Success
    [Arguments]    ${email}    ${pwd}=banana
    Input Text    id=customer_email  ${email}
    Input Text    id=customer_password  ${pwd}