#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)The number of operations will increase at the same rate as the value of n. Therefore, the run time will be O(n)


b)The number of operations here increases slower than the value of n. It increase near the square root of n. Therefore the run time is O(sqrt n)


c)This recursine will occur at the same number of times as is the value of bunnies. Therefore the run time is linear or O(n). 

## Exercise II

This is basically a search function. We are searching for the lowest floor in which an egg will break if dropped from it. We could do a loop of each floor but in a worst case scenario, we would us up all of our eggs. A more efficient way to do this is to use a binary search. 

1) We will start with the middle floor, which is initially n/2, and see it the egg breaks. 

2) If the egg breaks we will then set the new middle to be halfway between the ground floor and the old middle floor and then run the experiment again. (Step 1.)

3) If the egg does not break at floor n/2, then we will find the new middle which is between the old middle floor and the top floor. Then we will go back to step 1 to repeat the experiment.

Eventually, will will find the lowest floor in which the egg breaks and return that result.
