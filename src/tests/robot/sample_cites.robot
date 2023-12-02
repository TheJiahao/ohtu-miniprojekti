*** Settings ***
Resource    resource.robot


*** Keywords ***
Clear Database And Add Sample Cites
    Empty Db
    Add Cite
    ...    article
    ...    introductionCS
    ...    Cortina Thomas J.
    ...    An introduction to computer science for non-majors using principles of computation
    ...    2007

    Add Cite
    ...    article
    ...    libsvm
    ...    Chang Chih-Chung, Lin Chih-Jen
    ...    LIBSVM: A Library for Support Vector Machines
    ...    2011

    Add Cite
    ...    book
    ...    newton1999principia
    ...    Newton Isaac
    ...    The Principia: mathematical principles of natural philosophy
    ...    1999

    Add Cite
    ...    book
    ...    newton1952opticks
    ...    Newton Isaac
    ...    Opticks, or, a treatise of the reflections, refractions, inflections \& colours of light
    ...    1952
