# Problem
# Read problem statements in Vietnamese,
# Bengali, Mandarin Chinese, and Russian as well.
# Chefland has 2 different types of coconut, type A and type B. Type A contains only xa milliliters of coconut water and type B contains only xb grams of coconut pulp. Chef's nutritionist has advised him to consume 
# Xa milliliters of coconut water and Xb grams of coconut pulp every week in the summer. Find the total number of coconuts (type A + type B) that Chef should buy each week to keep himself active in the hot weather.
# Input Format
# The first line contains an integer T, the number of test cases. Then the test cases follow.
# Each test case contains a single line of input, four integers 
# xa,xb,Xa,Xb.
# Output Format
# For each test case, output in a single line the answer to the problem.

# cook your dish here
for i in range(int(input())):
    a,b,A,B=list(map(int,input().split()))
    x=A//a
    y=B//b
    print(x+y)