#DIGM 131 - Assignment 2: Procedural Pattern Generator

import maya.cmds as cmds

# Clear the scene.
cmds.file(new=True, force=True)

def generate_pattern():

    # --- Configuration variables ---
    number_of_rows = 5          # Number of rows in the pattern.
    number_of_columns = 5       # Number of columns in the pattern.
    object_spacing = 3.0        # Distance between object centers.

    # --- Generate grid using nested loops ---
    for current_row in range(number_of_rows):

        for current_column in range(number_of_columns):

            # --- Calculate position ---
            position_x = current_column * object_spacing
            position_z = current_row * object_spacing

            # --- Conditional: change object type ---
            # Creating cubes, they are a bit larger to contrast with the spheres and cylinders
            if (current_row + current_column) % 3 == 0:
                created_object = cmds.polyCube()[0]
                base_scale = 1.0

            # Creating Spheres
            elif (current_row + current_column) % 3 == 1:
                created_object = cmds.polySphere()[0]
                base_scale = 0.6

            # Creating Cylinders
            else:
                created_object = cmds.polyCylinder()[0]
                base_scale = 0.8

            # --- Conditional: change height based on index ---
            object_index = (current_row * number_of_columns) + current_column

            # This condition creates a repeating height rhythm across the grid
            if object_index % 3 == 0:
                height_scale = 2.0

            # Taller objects stand out in the pattern

            else:
                height_scale = 1.0

            # --- Apply transformations ---
            # Positioning, places the object into the grid structure
            cmds.move(position_x, 0, position_z, created_object)

            # Scaling, applies both base size and height variation
            cmds.scale(base_scale, height_scale, base_scale, created_object)


# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.

cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
