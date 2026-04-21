*** Settings ***
Resource    ../../resources/pages/login_page.robot
Resource    ../../resources/common_resources.robot

Suite Setup    Load Environment
Test Setup    Open Application    https://gullylabs.com/account/login
Test Teardown    Close Application

*** Test Cases ***
TC01 login

    [Documentation]  checking login
    [Tags]    functional
    
    Login Page    azadsr158@gmail.com    Pranjal@123
    Login Page    ${given_mail}    ${given_pass}
    