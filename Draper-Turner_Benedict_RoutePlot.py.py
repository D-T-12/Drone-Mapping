"""
29/11/22
30294693 Benedict Draper-Turner
Submission for JCS Module 3: Python
'A Program to plot routes for a simple drone guidance system'
"""


def read_file(filename):
    """
    Handles file opening.
    Input: drone_route text file.
    Output: A string of the route file.
    """
    while True:

        # Check the file exists.
        try:
            file = open(filename)

        # Raise an error if the file does not exist.
        except FileNotFoundError:
            print("The file is not found")
            return 0

        # Read the file if it exists.
        else:
            file_string = file.read()
            file.close()
            return file_string


def clean_instructions(file_string):
    """
    Gets start co-ordinates and transform instructions to list.
    Input: A route string.
    Output: Start co-ordinates and the route instructions (NWWE...).
    """
    # Create a list splitting on every newline.
    instructions = file_string.split("\n")

    # Create start co-ordinates
    x = int(instructions.pop(0))
    y = int(instructions.pop(0))  # Pop zero both times as item 1 takes the 0 space after pop.
    start = (x, y)

    return start, instructions


def generate_coordinates(start, instructions):
    """
    Generates the full co-ordinate set and check for errors in route.
    Input: Start co-ordinates and route instructions.
    Output: A full set of route co-ordinates.
    """
    # Initialise grids list and add start grid.
    grids = [start]

    # Create working grid manipulation.
    working_grid = list(start)

    # Generate the rest of the grids.
    for item in instructions:

        if item == "N":
            working_grid[1] += 1
        elif item == "E":
            working_grid[0] += 1
        elif item == "S":
            working_grid[1] -= 1
        elif item == "W":
            working_grid[0] -= 1
        else:
            pass

        # Check route doesn't leave boundaries and return error if so.
        if 0 in working_grid or 13 in working_grid:
            print(f"Route leaves boundaries at {working_grid}")
            return 0
        else:
            grids.append(tuple(working_grid))

    return grids


def display_map(grids):
    """
    A function to display the route.
    Input: Grid list.
    Output: Route map.
    """
    # Block and number defining.
    space_block = "   :"
    sep_block = "---:"
    mark_block = " x :"
    num = {1: " 1", 2: " 2", 3: " 3", 4: " 4", 5: " 5", 6: " 6",
           7: " 7", 8: " 8", 9: " 9", 10: "10", 11: "11", 12: "12"}

    # Printing map row by row.
    for y in range(13):

        # Top row generation.
        if y == 0:
            print(space_block * 13, end="")
            print("   ")

        # Numbered rows generation.
        if y < 12:

            # Printing seperator rows every other row.
            print(sep_block * 13, end="")
            print("---")

            # Printing non seperator rows.
            for x in range(13):

                # Creating a variable for the current grid.
                current_square = (x, 12-y)

                # Adding row number at start.
                if x == 0:
                    print(f" {num[12-y]}:", end="")

                else:
                    # Condition to check if current block is in the route and mark with x.
                    if current_square in grids:
                        print(mark_block, end="")
                    else:
                        print(space_block, end="")

        # Final row including column numbers.
        else:
            # Final seperator row
            print(sep_block * 13, end="")
            print("---")

            # Column number row
            for z in range(13):
                if z == 0:
                    print("   :", end="")
                else:
                    print(f"{num[z]} :", end="")

        print("")


def run():
    """
    The main function to run the programme
    """
    # Run while stop hasn't been called.
    while 1:
        check = input("Please input a file name or STOP to finish:").lower()

        if check != "stop":
            one = read_file(check)

            if one == 0:
                pass

            else:
                start_loc, instr = clean_instructions(one)
                drone_grids = generate_coordinates(start_loc, instr)

                if drone_grids == 0:
                    pass

                else:
                    display_map(drone_grids)
                    print(f"Coordinates:")

                    for x in drone_grids:
                        print(x)

        else:
            break


# Checking the file is not imported before running.
if __name__ == "__main__":
    run()
