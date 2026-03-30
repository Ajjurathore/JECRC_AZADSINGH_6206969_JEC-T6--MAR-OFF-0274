*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${url}  https://the-internet.herokuapp.com/
${check_download}  C:\\Users\\azads\\Downloads\\file.txt

*** Test Cases ***
#upload
#    Open Browser    ${url}  chrome
#    Maximize Browser Window
#
#    Click Element    xpath=//*[@id="content"]/ul/li[18]/a
#    Sleep    1s
#
#    ${path}  Normalize Path    ${CURDIR}/sample.txt
#
#    Choose File    id=file-upload  ${path}
#    Sleep    1s
#    Click Button    id=file-submit
Download
    Open Browser    ${url}  chrome
    Maximize Browser Window

    Click Element    xpath=//a[@href='/download']
    Sleep    1s

    Click Element    xpath=//a[@href='download/file.txt']
    Sleep    1s
    
    Wait Until Created  ${check_download}  timeout=10s
    
    File Should Exist    ${check_download}
    Log To Console    is donwload sciss
    Close Browser