*** Settings ***
Resource        sample_cites.robot

Test Setup      Clear Database And Add Sample Cites


*** Test Cases ***
Search By Author Should Succeed
    Select Search Cite
    Input    kirjailija
    Input    Newton Isaac
    Run App
    Output Should Contain    newton1999principia
    Output Should Contain    newton1952opticks

Search By Title Should Succeed
    Select Search Cite
    Input    otsikko
    Input    An introduction to computer science for non-majors using principles of computation
    Run App
    Output Should Contain    An introduction to computer science for non-majors using principles of computation

Search By Author Without Cites Should Not Return Anything
    Select Search Cite
    Input    kirjailija
    Input    Ihminen
    Run App
    Output Should Not Contain    libsvm
    Output Should Not Contain    newton1999principia
    Output Should Not Contain    newton1952opticks

Search By Title Without Cites Should Not Return Anything
    Select Search Cite
    Input    title
    Input    Ihminen
    Run App
    Output Should Not Contain    libsvm
    Output Should Not Contain    newton1999principia
    Output Should Not Contain    newton1952opticks
