*** Settings ***
Library  ../../AppLibrary.py

*** Keywords ***
Run App
    Input  lopeta
    Start App

Add Cite
    [Arguments]  ${choise}  ${type}  ${name}  ${authors}  ${title}  ${year}
    Input  ${choise}
    Input  ${type}
    Input  ${name}
    Input  ${authors}
    Input  ${title}
    Input  ${year}

Empty Database
    Empty Db

Output Should Contain
    [Arguments]  ${value}
    Output Contains  ${value}