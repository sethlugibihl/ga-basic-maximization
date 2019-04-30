The simple implementation includes a basic testing framework with a wide array of values iterating through 
population sizes, mutation rates, and crossover rates.

The GA takes a pair, compares their fitness measures and takes the best and places in in a "best fit" list

The "best fit" population is fed into the mutation algorithm which determines if a given member will be mutated, in which case the individual bit
at a random location is flipped. If not, the original member is added.

The mutated population is fed into the crossover algorithm that takes a member, determines if to crossover, then picks a random member from the 
mutation population and performs crossover and adds the new member to the crossover list.

This process is completed till 95% convergence.

At the end of the testing, it should list the optimal (least iteartions) converge variables.

My findings indicated a best run of the following:

Iterations: 15
Population Size: 20
Mutation Rate: 0.001
Population Rate: 0.6