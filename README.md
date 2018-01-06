# Biased Pseudo Random Number Generator in Python

Code for a biased PRNG written in Python using Pemuted Congruential Generator(PCG)

## Working

It generated numbers between 1 to 10 with a bias of 73% for numbers greater than 5.
The bias is introduced by a simple if/else check on the number returned by the random number generator.
The probabity of getting any number is equal. So if the number returned(normalized to fall between 0 and 1) is less than 0.73, keep calling the generator until it produce a number between [6-10], else wait for it to return number [1-5]. 
This if/else condition biases the output as aforementioned because the chances of number returned being less than 0.73 is 73% since the generator itself is not biased. 

rand() function:
A seed is provided taking the milliseconds from time.time() from the time module.
To keep the numbers in bound, it is converted to a 64-bit using ctypes.c_uint64 method
The first 5 bits are used as a count to rotate the next 32 bits and return it as a random number which then is normalized to lie between 1-10. 

### Output

The python script generates a text file in the same directory with 'n' random numbers and also the percentage of numbers greater and less than 5.


