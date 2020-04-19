# Coursera algorithm course week 1 assignment 1
"""
In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.

To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers. You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.

So: what's the product of the following two 64-digit numbers?

3141592653589793238462643383279502884197169399375105820974944592
2718281828459045235360287471352662497757247093699959574966967627

[TIP: before submitting, first test the correctness of your program on some small test cases of your own devising. Then post your best test cases to the discussion forums to help your fellow students!]

[Food for thought: the number of digits in each input number is a power of 2. Does this make your life easier? Does it depend on which algorithm you're implementing?]

The numeric answer should be typed in the space below. So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks.

(We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)
"""

import math
import unittest

x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def karatsuba(x, y): 
	# base case: return only single digit multiplication
	if len(str(x)) == 1 or len(str(y)) == 1: 
		return x * y
	else: 
		# break down into n/2
		midpoint = math.floor(len(str(x)) / 2)

		# step 1: extract a b c d 
		a = x // 10**midpoint
		c = y // 10**midpoint
		b = x % 10**midpoint
		d = y % 10**midpoint

		# step 2: recursively compute ac and bd
		ac = karatsuba(a, c)
		bd = karatsuba(b, d)

		# step 3: recursively compute (a+b)(c+d) and subtract ac and bd 
		aplusb = int(a) + int(b)
		cplusd = int(c) + int(d)
		three = aplusb * cplusd
		three = int(three) - int(ac) - int(bd)

		return ac * (10**(midpoint*2)) + three * (10**midpoint) + bd


class TestCalc(unittest.TestCase): 

	def test_under_four(self): 
		self.assertEqual(karatsuba(123, 456), 56088)
		self.assertEqual(karatsuba(999, 999), 998001)
		self.assertEqual(karatsuba(182, 201), 36582)
		self.assertEqual(karatsuba(1, 20), 20)

	def test_larger_numers(self): 
		self.assertEqual(karatsuba(1234, 5678), 7006652)
		self.assertEqual(karatsuba(99999999, 99999999), 9999999800000001)
		self.assertEqual(karatsuba(87291, 111119292), 9699714117972)


if __name__ == '__main__':
	unittest.main()
	# assingment problem
	z = karatsuba(x,y)
	print(z)
