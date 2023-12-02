*** Settings ***
Library     ../../AppLibrary.py


*** Keywords ***
Run App
    Input    lopeta
    Start App

Add Cite
    [Arguments]    ${type}    ${name}    ${authors}    ${title}    ${year}
    Input    ${type}
    Input    ${name}
    Input    ${authors}
    Input    ${title}
    Input    ${year}

Select Add Cite
    Input    lisää

Empty Database
    Empty Db

Output Should Contain
    [Arguments]    ${value}
    Output Contains    ${value}
