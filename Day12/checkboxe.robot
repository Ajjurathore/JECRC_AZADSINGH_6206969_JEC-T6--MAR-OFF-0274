*** Settings ***
Documentation    handling checkboxes
Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${url1}  https://testautomationpractice.blogspot.com/

*** Test Cases ***
#Handling checkboxes
#    [Documentation]    herokuapp checkboxes
#    Open Browser    ${url}  chrome
#    Maximize Browser Window
#    Sleep    2s
#
#    Click Element    xpath=//*[@id="content"]/ul/li[6]/a
#    Sleep    4s
#    Page Should Contain Checkbox    xpath=//*[@id="checkboxes"]/input[1]
#
#    Select Checkbox    xpath=//*[@id="checkboxes"]/input[1]
#    Sleep    2s
#    Unselect Checkbox   xpath=//*[@id="checkboxes"]/input[2]
#    Sleep    3s
#    
#    
Handling checkboxes
    [Documentation]    testautomation checkboxes
    Open Browser    ${url1}  chrome
    Maximize Browser Window
    Sleep    2s

    Click Element    xpath=//*[@id="male"]
    Sleep    4s

    Page Should Contain Checkbox    xpath=//*[@id="sunday"]


    Select Checkbox    xpath=//*[@id="sunday"]
    Select Checkbox    xpath=//*[@id="saturday"]
    Sleep    2s
    Unselect Checkbox   xpath=//*[@id="sunday"]
    Sleep    3s

    Close Browser