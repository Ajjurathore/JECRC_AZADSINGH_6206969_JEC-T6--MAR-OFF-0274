*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://inc.in/

*** Test Cases ***
handling js
    Open Browser    ${url}  chrome
    Maximize Browser Window
    Sleep    2s

    Execute Javascript    window.scrollTo(0,document.body.scrollHeight)
    Sleep    1s


    Close Browser