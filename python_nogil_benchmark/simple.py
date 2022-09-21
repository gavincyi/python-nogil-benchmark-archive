from functools import partial                             
from timeit import timeit                                 
                                                          
                                                          
def iteration(N):                                         
    array = [0] * N                                       
    for i in range(0, N):                                 
        array[i] = 1.0                                    
                                                          
                                                          
if __name__ == '__main__':                                
    result = {}                                           
    for n in [100, 500, 1000]:                            
        result[n] = timeit(partial(iteration, n))         
                                                          
    print(f"Iteration benchmark: {result}")               
