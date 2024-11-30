from typing import List

def diagonal_difference(arr: List[List[int]]) -> int:
    # Write your code here
    sum_diagonal_primary = 0
    sum_secundary_diagonal = 0
    for i in range(0, len(arr)):
        sum_diagonal_primary += arr[i][i]
        sum_secundary_diagonal += arr[::-1][i][i]
    
    #print(f"primera diagonal {sum_diagonal_primary}")
    #print(f"segunda diagonal {sum_secundary_diagonal}")
    
    # return suma
    
    return abs(sum_diagonal_primary - sum_secundary_diagonal)



if __name__ == "__main__":
    arr_one = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
    ]
     
    arr_two = [          #                             
        [11,2,4],        #
        [4,5,6],         #
        [10,8,-12],
    ]
    
    arr_three  = [
        [1, 2, 3],   
        [4, 5, 6],
        [9, 8, 9]  
    ]
    print(diagonal_difference(arr_one))
    print(diagonal_difference(arr_two))
    print(diagonal_difference(arr_three))
    
    
    # [[10, 8, -12], 
    # [4, 5, 6], 
    # [11, 2, 4]]