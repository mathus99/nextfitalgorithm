
# To assign memory blocks to processes, define the NextFit function.
def NextFit(blockSize, numB, processSize, numP): 
    """
    numB - Number of  Memory blocks
    numP - Number of Processes
    j - Tracks  memory block  currently checking
    t-  A variable used  to end point track
    """
    # Initialize allocation array with -1 
    allocation = [-1] * numP
    j = 0      # checking memory blocks from the first block
    t = numB-1 # Set the initial end point to the last block
    

    # Iterate over each process to find a suitable memory block
    for i in range(numP):


        # Check memory blocks starting from the current point
        while j < numB:
            # If the block can fit the process, allocate it
            if blockSize[j] >= processSize[i]:
                
                # Allocate the block to the process
                allocation[i] = j
                
                # Reduce available memory in  block.
                blockSize[j] -= processSize[i]
                
                # Update the end point for the next allocation
                t = (j - 1) % numB
                break
            
            #  If the end point is reached, set a new end point
            if t == j:
              
                t = (j - 1) % numB   # Set the end point
                # breaks the loop after going through all memory block
                break

            # Move to the next block in a circular manner
            j = (j + 1) % numB

    print("ProcessNumber              Process Size              Block Number")
    
            # Print process number and size

    for i in range(numP):
        print("\t", i + 1, "\t\t\t", processSize[i], end="\t\t\t")

        # If the process is allocated to a block, print the block number
        if allocation[i] != -1:
            print(allocation[i] + 1)
        # If not allocated, print "Not Allocated"   
        else:
            print("Not Allocated")

if __name__ == '__main__':
    # User input for memory block sizes
    blockSize = list(map(int, input("Enter memory block sizes with spaces: ").split()))
    
    # User input for process sizes
    processSize = list(map(int, input("Enter process sizes with spaces: ").split()))

    # Calculate Numvber of the memory blocks and processes
    numB = len(blockSize)
    numP = len(processSize)

    NextFit(blockSize, numB, processSize, numP)
