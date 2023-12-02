*** Settings ***
Resource        resource.robot

Test Setup      Select Add Cite
Test Teardown   Empty Database


*** Test Cases ***
Add Cite With Incorrect Choice
    Input    incorrect choice
    Run App
    Incorrect Input

Add Cite With Incorrect Type
    Add Cite    eiole    ..    ..    ..    ..
    Run App
    Incorrect Input

Add Cite With Correct Inputs
    Add Cite    1    robotesti    Robotti Ruttunen    Robotin ohjekirja    2023
    Add Cite    2    robo2    Sähkövirta Smith , Aarne Terästähti    Robottien tulevaisuus    1989
    Run App

Add Journal Type Cite With Correct Inputs
    Add Cite    3    journaltesti    journalauthor    journaltitle    1984
    Run App


*** Keywords ***
Incorrect Input
    Output Should Contain    Toimintoa ei olemassa tai ei toteutettu vielä.
