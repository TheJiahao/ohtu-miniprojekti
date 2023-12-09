*** Settings ***
Resource        sample_cites.robot

Test Setup      Clear Database And Add Sample Cites


*** Test Cases ***
Remove All Should Succeed
    Select Remove Cite
    Select Remove All
    Input    vahvista
    Select List Cites
    Run App
    Output Should Not Contain    introductionCS
    Output Should Not Contain    libsvm
    Output Should Not Contain    newton1999principia
    Output Should Not Contain    newton1952opticks

Remove All By Incorrect Confirmation Should Not Remove Anything
    Select Remove Cite
    Select Remove All
    Input    vaahvaastaaaa
    Select List Cites
    Run App
    Output Should Contain    introductionCS
    Output Should Contain    libsvm
    Output Should Contain    newton1999principia
    Output Should Contain    newton1952opticks


*** Keywords ***
Incorrect Input
    Output Should Contain    Toimintoa ei olemassa tai ei toteutettu vielä.

Select Remove All
    Input    kaikki
