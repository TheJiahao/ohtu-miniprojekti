*** Settings ***
Resource  resource.robot
Test Setup  Empty Database

*** Test Cases ***
Run App And End With Lopeta
    Run App

Add Cite With Incorrect Choice
    Add Cite  eiole  lopeta  ..  ..  ..  ..  
    Incorrect Input

Add Cite With Incorrect Type
    Add Cite  lisää  eiole  lopeta  ..  ..  ..  
    Incorrect Input


Add Cite With Correct Inputs
    Add Cite  lisää  1  robotesti  Robotti Ruttunen  Robotin ohjekirja  2023 
    Add Cite  lisää  2  robo2  Sähkövirta Smith , Aarne Terästähti  Robottien tulevaisuus  1989 
    Run App

Add Journal Type Cite With Correct Inputs
    Add Cite  lisää  3  journaltesti  journalauthor  journaltitle  1984
    Run App

*** Keywords ***
Incorrect Input
    Run App
    Output Should Contain  Toimintoa ei olemassa tai ei toteutettu vielä.