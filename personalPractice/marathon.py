"""
Approach:
- firstly I calculate the sum of all participant's round number
- as one of them will be the referee, so n-1 numbers people are the participants
- so I divide the sum by n-1 (the actual participants)
- then I took the the int value and add extra_sum with this if toatl_sum%(n-1) is equal not 0
- finally we return the max value between estimated_answer and max value of the array

Time Complexity: n
"""

def marathon():
    
    n = int(input())
    arr = list(map(int, input().split()))[:n]
    total_sum = sum(arr)
    max_num = max(arr)
    extra = 1 if total_sum%(n-1) != 0 else 0

    estimated_answer = total_sum//(n-1) + extra
    
    print(max(estimated_answer, max_num))
        
if __name__ == "__main__":
    marathon()