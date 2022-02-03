## Task
An ATM only has 100, 50 and 20 dollar bills (USD) available to be dispensed.

Given an amount between 40 and 10000 dollars (inclusive) and assuming that the ATM wants to use as few bills as possible, determinate the minimal number of 100, 50 and 20 dollar bills the ATM needs to dispense (in that order).

## Example
For n = 250, the result should be [2, 1, 0].
For n = 260, the result should be [2, 0, 3].
For n = 370, the result should be [3, 1, 1].
For n = 230, the result should be [1, 1, 4].

## Input/Output

### [input] integer n

n: Amount of money to withdraw. 

### [output] integer array
An array of number of 100, 50 and 20 dollar bills needed to complete the withdraw (in that order).