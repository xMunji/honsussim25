import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- ASCII Art Components ---

# Landscape elements
TREE = " /\\ \n_||_"
TINY_HOUSE = "[~~]"
HILL = "  .--.  \n /    \\ \n/______\\"
FLOWER = " `,*,'"
GRASS = ",,,,,,,,"
WATER = "~~~~~"

# Stadium elements (will be built up)
STADIUM_WALL = "|"
STADIUM_SEAT = "="
STADIUM_ROOF_EDGE = "_"
STADIUM_FIELD = "." # or blank space

# --- Animation Frames ---
# Each frame is a list of strings (lines of the scene)

def generate_initial_landscape(width=70, height=15):
    scene = [list(' ' * width) for _ in range(height)]
    
    # Add some grass at the bottom
    for i in range(width):
        if i % 5 == 0: scene[height-1][i] = ','
        if i % 7 == 1: scene[height-2][i] = '.'

    # Place some trees
    scene[height-4][5] = '/'; scene[height-4][6] = '\\';
    scene[height-3][4] = '_'; scene[height-3][5] = '|'; scene[height-3][6] = '|'; scene[height-3][7] = '_';

    scene[height-5][width-10] = '/'; scene[height-5][width-9] = '\\';
    scene[height-4][width-11] = '_'; scene[height-4][width-10] = '|'; scene[height-4][width-9] = '|'; scene[height-4][width-8] = '_';
    
    # Place a hill
    scene[height-6][width//2-2] = '.'; scene[height-6][width//2-1] = '-'; scene[height-6][width//2] = '-'; scene[height-6][width//2+1] = '.';
    scene[height-5][width//2-3] = '/'; scene[height-5][width//2+2] = '\\';
    scene[height-4][width//2-4] = '/'; scene[height-4][width//2-3:width//2+3] = list('______'); scene[height-4][width//2+3] = '\\';


    # Tiny house
    scene[height-3][width//3] = '['; scene[height-3][width//3+1] = '~'; scene[height-3][width//3+2] = '~'; scene[height-3][width//3+3] = ']';
    scene[height-4][width//3+1] = '/'; scene[height-4][width//3+2] = '\\';


    return ["".join(row) for row in scene]

def build_stadium_frames(initial_scene, width=70, height=15, steps=20):
    frames = []
    current_scene_list = [list(row) for row in initial_scene]

    # Stadium will grow from center outwards, bottom up
    stadium_center_x = width // 2
    stadium_bottom_y = height - 2 

    max_stadium_width_radius = width // 3
    max_stadium_height = height // 2 + 2

    for step in range(steps):
        frame_scene_list = [list(row) for row in initial_scene] # Start with landscape
        
        # Overwrite with current stadium state, gradually replacing landscape
        # This is a simplified growth model
        current_stadium_width_radius = (max_stadium_width_radius * step) // steps + 1
        current_stadium_height = (max_stadium_height * step) // steps + 1

        for y_offset in range(current_stadium_height):
            y = stadium_bottom_y - y_offset
            if 0 <= y < height:
                # Calculate width at this height (oval shape)
                # This is a very rough approximation of an oval stadium wall
                dynamic_width_radius = current_stadium_width_radius * (1 - (y_offset / (max_stadium_height * 1.5) )**2 )
                dynamic_width_radius = max(1, int(dynamic_width_radius))

                for x_offset in range(-dynamic_width_radius, dynamic_width_radius + 1):
                    x = stadium_center_x + x_offset
                    if 0 <= x < width:
                        # Inner part is field/seats, outer is wall
                        if abs(x_offset) > dynamic_width_radius - 2 and y_offset < current_stadium_height -1 : # Wall
                            frame_scene_list[y][x] = STADIUM_WALL if step > steps//4 else ' ' # Wall appears later
                        elif y_offset < current_stadium_height -1 : # Seats / Field
                            if y % 2 == 0 and step > steps //3: # seats appear after field
                                frame_scene_list[y][x] = STADIUM_SEAT
                            else:
                                frame_scene_list[y][x] = STADIUM_FIELD if step > steps//5 else ' ' # Field
                        
                        # Roof edge
                        if y_offset == current_stadium_height - 1 and abs(x_offset) <= dynamic_width_radius and step > steps//2:
                             frame_scene_list[y][x] = STADIUM_ROOF_EDGE
        
        # Make a copy of the modified landscape (where stadium is now)
        # This makes the stadium "eat" the landscape permanently in subsequent frames
        if step > 0: # Ensure stadium elements from previous step persist and "erase"
            for r_idx, row_val in enumerate(frames[-1]): # Get previous frame
                prev_frame_row = list(row_val)
                for c_idx, char_val in enumerate(prev_frame_row):
                    if char_val in [STADIUM_WALL, STADIUM_SEAT, STADIUM_ROOF_EDGE, STADIUM_FIELD, ' ']: # If it was stadium or erased
                        if frame_scene_list[r_idx][c_idx] not in [STADIUM_WALL, STADIUM_SEAT, STADIUM_ROOF_EDGE, STADIUM_FIELD]:
                             # If current landscape pixel is NOT yet stadium, but previous was, erase it.
                             if char_val == ' ': # If previous was erased space
                                frame_scene_list[r_idx][c_idx] = ' '
                             elif char_val == STADIUM_FIELD and frame_scene_list[r_idx][c_idx] != ' ': # If prev was field
                                frame_scene_list[r_idx][c_idx] = STADIUM_FIELD
                             # This logic is tricky; the goal is that once stadium covers something, it stays covered/erased.

        frames.append(["".join(row) for row in frame_scene_list])
    
    # Final frames: "Fade" remaining landscape elements by replacing them with spaces
    # This is the "pixel by pixel" decay part
    landscape_chars = ['/', '\\', '_', '|', '[', '~', ']', '.', '-', ','] # Chars to fade
    
    # Get the last stadium frame as a base
    last_stadium_frame_list = [list(row) for row in frames[-1]]

    for _ in range(10): # Number of fade steps
        faded_something = False
        new_fade_frame_list = [list(row) for row in last_stadium_frame_list] # Work on a copy
        
        # Iterate randomly to pick landscape pixels to fade
        # To make it more "pixel by pixel" and less uniform row by row
        coords_to_fade = []
        for r in range(height):
            for c in range(width):
                if new_fade_frame_list[r][c] in landscape_chars:
                    coords_to_fade.append((r,c))
        
        if not coords_to_fade: break # Nothing left to fade

        import random
        random.shuffle(coords_to_fade)

        # Fade a percentage of remaining landscape pixels in this step
        num_to_fade_this_step = max(1, len(coords_to_fade) // 5) 

        for i in range(min(num_to_fade_this_step, len(coords_to_fade))):
            r, c = coords_to_fade[i]
            new_fade_frame_list[r][c] = ' ' # Fade to blank
            faded_something = True
        
        if not faded_something and len(frames) > steps : break # Avoid infinite loop if no landscape left
        
        last_stadium_frame_list = [list(row) for row in new_fade_frame_list] # Update base for next fade
        frames.append(["".join(row) for row in new_fade_frame_list])


    return frames


def display_epilogue(animation_frames, frame_delay=0.15):
    title = "Decay to Growth"
    for i, frame_content in enumerate(animation_frames):
        clear_screen()
        print(title.center(len(frame_content[0]) if frame_content else 70))
        print("-" * (len(frame_content[0]) if frame_content else 70))
        for line in frame_content:
            print(line)
        print("-" * (len(frame_content[0]) if frame_content else 70))
        # Add a slight slow down towards the end of stadium growth, then speed up fade
        if i < len(animation_frames) * 0.7:
            time.sleep(frame_delay + (i * 0.005) ) # Stadium growth slows slightly
        elif i < len(animation_frames) - 5: # Main fade
             time.sleep(frame_delay * 0.8)
        else: # Final few fade frames
            time.sleep(frame_delay * 0.5)


if __name__ == "__main__":
    width = 75
    height = 20
    
    initial_ls = generate_initial_landscape(width, height)
    
    # More steps for stadium growth, fewer for pure fade
    stadium_growth_steps = 35 
    # Fade steps are now integrated into the end of build_stadium_frames
    
    all_frames = build_stadium_frames(initial_ls, width, height, steps=stadium_growth_steps)
    
    display_epilogue(all_frames, frame_delay=0.1)