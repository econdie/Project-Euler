# can be reasoned out mathematically

# consider the factors

# we need 20 to be a factor: 20 * ....

# we need 19 to be a factor as its prime: 20 * 19 * ....

# we dont need 18 to be a factor because we get 2 from 20 (20 = 10*2)
# but we need 9 to be a factor, and we get 18 by 9 * 2
# so we get 20 * 19 * 9 * ... = 10 * 2 * 19 * 9 * ...

#we need 17 to be a factor as its prime: 20 * 19 * 17 * 9 * ...

#we dont need 16 to be a factor because we get 4 from 20 (20 = 5*4)
#but we need another 4 as a factor, and we get 16 by 4 * 4
#so we get 20 * 19 * 17 * 9 * 4 * ...

#we dont need 15 to be a factor because we get 5 from 20 and 3 from 9: 5 * 3 = 15

#we dont need 14 to be a factor because we get 2 from 20 but we need 7
#so we get 20 * 19 * 17 * 9 * 7 * 4

#we need 13 to be a factor as its prime: 20 * 19 * 17 * 13 * 9 * 7 * 4

#we dont need 12 to be a factor because we get 5 from 20 and we have 4

#we need 11 to be a factor as its prime: 20 * 19 * 17 * 13 * 11 * 9 * 7 * 4

#we dont need 10 because we get 5 from 20 and 2 from 4

#continuing with this logic we already have the rest of the numbers from 1 to 9

#final answer is 20 * 19 * 17 * 13 * 11 * 9 * 7 * 4 which is lowest number divisible by numbers in {1, ... , 20}

print(20 * 19 * 17 * 13 * 11 * 9 * 7 * 4)
