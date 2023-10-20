def tower_of_hanoi(num_disks, source_rod, destination_rod, auxiliary_rod):
    """
    Recursive function to solve Tower of Hanoi puzzle.
    
    Parameters:
    num_disks (int): Number of disks to be moved.
    source_rod (str): Name of the source rod.
    destination_rod (str): Name of the destination rod.
    auxiliary_rod (str): Name of the auxiliary rod.
    """
    if num_disks == 0:
        return
    tower_of_hanoi(num_disks - 1, source_rod, auxiliary_rod, destination_rod)
    print("Move disk", num_disks, "from rod", source_rod, "to rod", destination_rod)
    tower_of_hanoi(num_disks - 1, auxiliary_rod, destination_rod, source_rod)

# Driver code
number_of_disks = 3
source_rod_name = 'A'
destination_rod_name = 'C'
auxiliary_rod_name = 'B'

tower_of_hanoi(number_of_disks, source_rod_name, destination_rod_name, auxiliary_rod_name)