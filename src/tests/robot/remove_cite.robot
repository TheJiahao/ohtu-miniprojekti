*** Settings ***
Resource        sample_cites.robot
Test Setup      Clear Database And Add Sample Cites

*** Test Cases ***
Remove Cite By Correct Id Should Succeed
    Select Remove Cite
    Select Remove By Id
    Input    introductionCS
    Select List Cites
    Run App
    Output Should Not Contain    introductionCS
    Output Should Not Contain    Cortina Thomas J.
    Output Should Not Contain    An introduction to computer science for non-majors using principles of computation
    Output Should Not Contain    2007

Remove Cite By Incorrect Id Should Not Remove Anything
    Select Remove Cite
    Select Remove By Id
    Input    intro
    Select List Cites
    Run App
    Output Should Contain    introductionCS
    Output Should Contain    libsvm
    Output Should Contain    newton1999principia
    Output Should Contain    newton1952opticks

Remove Cite By Incorrect Removal Method Should Not Remove Anything
    Select Remove Cite
    Input    5
    Select List Cites
    Run App
    Incorrect Input
    Output Should Contain    introductionCS
    Output Should Contain    libsvm
    Output Should Contain    newton1999principia
    Output Should Contain    newton1952opticks

*** Keywords ***
Incorrect Input
    Output Should Contain    virheellinen syöte

Select Remove By Id
    Input    id