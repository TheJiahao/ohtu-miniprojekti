*** Settings ***
Library     ../../AppLibrary.py


*** Keywords ***
Run App
    Input    lopeta
    Start App

Input Cite Data
    [Arguments]    ${type}    ${id}    ${authors}    ${title}    ${year}
    Input    ${type}
    Input    ${id}
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
