#'''
#Robot is a keyword driven testing framework
#similar to coffee machine - press a single button and all the things will work automatically
#
#all import and packages from other files will come under:- settings section
#variables will come under where we will declare:-variables section
#scripts containing test cases will come under :- Test Cases section
#when we create user defined keyword will come under :- keyword section
#'''
#
#'''
#Close Window :- closes a tab of the recent browser
#Close Browser :- closes the recent browser all tabs
#Close All Browser :- closes all browser
#'''


# open browser
*** Settings ***
Documentation  Opening of browsers
Library  SeleniumLibrary

*** Variables ***
${url}  https://www.youtube.com/ 
#scaler Variables
${bikes}  ktm  kawasaki  honda  pulser
#dict variables
&{cars}  bmw=m5cs  merecedes=gwagon



*** Test Cases ***
#Opening Chrome headless Browser
#    [Documentation]  Chrome browser navigating to https://www.youtube.com
#    [Tags]  smoke  reg
#    # open browser  URL  ChromeType
#    Open Browser  ${url}  headlesschrome
#    Maximize Browser Window
#    Log    navigated to youtube     # Will give output in log file
#    Log To Console  ${bikes}[1]    # gives output in terminal4
#    Log To Console  ${cars.bmw}
#    Sleep  3s
#
#    Close Browser


#Opening Chrome Browser
#    [Documentation]  Chrome browser navigating to https://www.youtube.com
#    [Tags]  smoke  reg
#    # open browser  URL  ChromeType
#    Open Browser  ${url}  headlesschrome
#    Maximize Browser Window
#    Log    navigated to youtube     # Will give output in log file
#    Log To Console  ${cars.bmw}    # gives output in terminal4
#    Sleep  3s
#
#    Close Browser

Open cricbuzz in edge
    Open Edge Browser

*** Keywords ***
Open Edge Browser
    [Documentation]  Chrome browser navigating to https://www.youtube.com
    [Tags]  smoke  reg
    # open browser  URL  ChromeType
    Open Browser  ${url}  headlesschrome
    Maximize Browser Window
    Log    navigated to youtube     # Will give output in log file
    Log To Console  ${cars.bmw}    # gives output in terminal4
    Sleep  3s

    Close Browser
