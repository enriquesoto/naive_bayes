SIMPLE NAIVE BAYES IMPLEMENTATION IN PYTHON
===========

Simple Naive Bayes classifier using look-up tables, like in this link:


http://computersciencesource.wordpress.com/2010/01/28/year-2-machine-learning-naive-bayes-classifier/


EXAMPLE OF INPUT DATA

----------------------------------------------
car.data
----------------------------------------------
@RELATION CAR
@ATTRIBUTE buying {vhigh,high,med,low} 
@ATTRIBUTE maint {vhigh,high,med,low}
@ATTRIBUTE doors {2,3,4,5more}
@ATTRIBUTE persons {2,4,more}
@ATTRIBUTE lug_boot {small,med,big}
@ATTRIBUTE safety {low,med,high} 
@ATTRIBUTE class {unacc,acc,good,vgood}
@DATA
vhigh,vhigh,2,2,small,low,unacc
vhigh,vhigh,2,2,small,med,unacc
vhigh,vhigh,2,2,small,high,unacc
vhigh,vhigh,2,2,med,low,unacc
vhigh,vhigh,2,2,med,med,unacc
vhigh,vhigh,2,2,med,high,unacc
vhigh,vhigh,2,2,big,low,unacc
vhigh,vhigh,2,2,big,med,unacc
vhigh,vhigh,2,2,big,high,unacc
vhigh,vhigh,2,4,small,low,unacc
vhigh,vhigh,2,4,small,med,unacc
.
.
.
--------------------------------------------
car-prueba.data
--------------------------------------------
low,low,4,2,big,high
low,low,5more,4,med,med
low,low,5more,more,big,low
high,vhigh,3,4,big,med
...

OUTPUT

[[ 0.4541007  0.         0.         0.       ]]
[[ 0.34102509  0.48888306  0.73573345  0.        ]]
[[ 0.52936709  0.          0.          0.        ]]
[[ 0.55107556  0.47677294  0.          0.        ]]

---------------------------------------------

means that we have to choose the highest value, i.e. for the first row we choose 0.454100 -> unaac
for second row choose 0.7357 -> good
and so on




Enrique Soto Mendoza
San Agustin University - Arequipa


