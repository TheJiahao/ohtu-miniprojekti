*** Settings ***
Resource        sample_cites.robot
Library         OperatingSystem

Test Setup      Clear Database And Add Sample Cites


*** Test Cases ***
Export Cites Creates File
    Select Export Cites
    Run App
    File Should Exist    ./export/cites.bib

Exported File Contains Cites
    ${file}=    Get File    ./export/cites.bib
    Should Contain    ${file}    @article{libsvm,
    Should Contain    ${file}    author = {Chang Chih-Chung and Lin Chih-Jen},
    Should Contain    ${file}    title = {LIBSVM: A Library for Support Vector Machines},
    Should Contain    ${file}    year = {2011},
    Should Contain    ${file}    },
