*** Settings ***
Resource            resource.robot

Test Teardown       Empty Database


*** Test Cases ***
Command Info Not Shown At Beginning
    Run App
    Output Should Not Contain    lisää
    Output Should Not Contain    listaa
    Output Should Not Contain    hae
    Output Should Not Contain    poista
    Output Should Not Contain    lopeta

Command Info Is Shown When Help Is Called
    Input    help
    Run App
    Output Should Contain    lisää
    Output Should Contain    listaa
    Output Should Contain    hae
    Output Should Contain    poista
    Output Should Contain    lopeta
