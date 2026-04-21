*** Settings ***
Library    SeleniumLibrary
Resource    ../../locators/gully_locators.robot


*** Keywords ***
Home page
#    Click Element  ${account}
    Click Element  ${search}
