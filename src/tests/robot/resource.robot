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

Add Cite
    [Arguments]    ${type}    ${id}    ${authors}    ${title}    ${year}
    Select Add Cite
    Input Cite Data    ${type}    ${id}    ${authors}    ${title}    ${year}

Select Add Cite
    Input    lisää

Select Search Cite
    Input    hae

Select Remove Cite
    Input    poista

Select List Cites
    Input    listaa

Empty Database
    Empty Db
