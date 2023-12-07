*** Settings ***
Resource        sample_cites.robot

Test Setup      Empty Database


*** Test Cases ***
Listing Cites Should Succeed
    Clear Database And Add Sample Cites
    Select List Cites
    Run App
    Output Should Contain    Id
    Output Should Contain    Tyyppi
    Output Should Contain    Kirjoittajat
    Output Should Contain    title
    Output Should Contain    year

Listing Cites When There Are No Cites Should Succeed
    Select List Cites
    Run App
    Output Should Not Contain    Id
    Output Should Not Contain    Tyyppi
    Output Should Not Contain    Kirjoittajat
    Output Should Not Contain    title
    Output Should Not Contain    year
