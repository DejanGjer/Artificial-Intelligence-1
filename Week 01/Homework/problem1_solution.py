"""
Interviewbit - Amazon, Google
Pascal Triangle

link: https://www.interviewbit.com/problems/pascal-triangle/

Problem Description:
Given an integer A, equal to numRows, generate the first numRows of Pascal's triangle.
Pascal's triangle: To generate A[C] in row R, sum up A'[C] and A'[C-1] where A' is array from row R - 1.

Problem Constraints:
0 <= A <= 25

Example Input:
A = 5

Example Output:
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
"""

# @param A : integer
# @return a list of list of integers
def solve(A):
    if A == 0:
        return []
    sol = [[1]]
    i = 2
    while i <= A:
        arr = []
        for j in range(i):
            arr.append((sol[-1][j - 1] if j - 1 >= 0 else 0) + (sol[-1][j] if j < i - 1 else 0))
        sol.append(arr)
        i += 1 
    return sol
    
if __name__ == "__main__":
    print(solve(5))
            