*** Settings ***
Resource        sample_cites.robot

Test Setup      Clear Database And Add Sample Cites


*** Test Cases ***
Listing Cites Should Succeed
    Select List Cites
    Run App
    Output Should Contain    Cortina Thomas J.
