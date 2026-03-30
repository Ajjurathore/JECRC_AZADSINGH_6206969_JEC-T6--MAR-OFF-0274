*** Settings ***
Library    SeleniumLibrary
Library    String

*** Variables ***
${URL}    https://www.amazon.in

*** Test Cases ***
Amazon Product Flow
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Wait Until Element Is Visible    xpath=//a[text()=' Electronics ']    10s
    Click Element    xpath=//a[text()=' Electronics ']

    Click Element    xpath=//*[@id="s-refinements"]/div[4]/ul/li[4]/span/a/div/label/i

    Wait Until Element Is Visible    xpath=(//div[@data-component-type='s-search-result'])[1]    10s

    ${product_name}=    Get Text    xpath=(//h2//span)[6]
    Log To Console    Product Name: ${product_name}

    Click Element    xpath=(//h2//span)[6]
    Switch Window    NEW

    Wait Until Page Contains    ${product_name}    5s

    ${actual_price}=    Get Text    xpath=//*[@id="corePriceDisplay_desktop_feature_div"]/div[2]/span/span[1]/span[2]/span/span[1]
    ${discounted_price}=    Get Text    xpath=//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]

    Log To Console    Actual Price: ${actual_price}
    Log To Console    Discounted Price: ${discounted_price}

    ${discount}=    Get Text    xpath=//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[2]/span
    Log To Console    Discount: ${discount}

    Scroll Element Into View    id=add-to-cart-button
    Click Button    id=add-to-cart-button

    Wait Until Element Is Visible    id=nav-cart    5s
    Click Element    id=nav-cart
    Wait Until Page Contains    ${product_name}    5s

    Log To Console    successfully added to cart

    Close Browser