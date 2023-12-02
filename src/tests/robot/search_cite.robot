*** Settings ***
Resource        sample_cites.robot

Test Setup      Clear Database And Add Sample Cites


*** Test Cases ***
Search By Author Should Succeed
    Select Search Cite
    Input    2
    Input    Newton Isaac
    Run App
    Output Should Contain    newton1999principia
    Output Contains    newton1952opticks

Search By Title Should Succeed
    Select Search Cite
    Input    1
    Input    An introduction to computer science for non-majors using principles of computation
    Run App
    Output Contains    An introduction to computer science for non-majors using principles of computation
