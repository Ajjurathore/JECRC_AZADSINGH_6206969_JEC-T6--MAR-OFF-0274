*** Settings ***

Library    SeleniumLibrary

*** Variables ***
${url}  https://the-internet.herokuapp.com/


*** Test Cases ***
#Handling drag and drop
#    Open Browser    ${url}  chrome
#    Maximize Browser Window
#    Sleep    1s
#
#    Click Element    //*[@id="content"]/ul/li[10]/a
#    Sleep    2s
#
#    Drag And Drop    //*[@id="column-b"]  //*[@id="column-a"]
#    Sleep    3s
#
#    Close Browser


Handling hover
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Click Element    xpath=//*[@id="content"]/ul/li[25]/a
    Sleep    1s

    Mouse Over    xpath=//*[@id="content"]/div/div[1]/img       #hovering
    Sleep    3s

    Close Browser

scoll to element
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    1s

    Scroll Element Into View    xpath=//*[@id="content"]/ul/li[25]/a       #hovering
    Sleep    3s

    Close Browser
