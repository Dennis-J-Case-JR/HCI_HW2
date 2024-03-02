###########################################################
# Imports
###########################################################

import time                                     # Import time
from tkinter import *                           # Import tkinter from libraries



###########################################################
# Making the GUI window
###########################################################

import tkinter as tk                            # Import tkinter into variable for GUI creation



###########################################################
# Some Global Variables and Arrays
###########################################################

w               = 960                           # Width of the window
h               = 540                           # Height of the window
bw              = 20                            # Width of button
bh              = 10                            # Height of button
difflvlcounter  = 0                             # What difficulty is the trial on
pairCounter     = 0                             # Counter for number of times pair has been clicked
endTime         = 0                             # End time
startTime       = 0                             # Start time
timeToComplete  = 0                             # Time it takes to complete the task
trialAverage    = 0                             # Average of a trial
overallAverage  = 0                             # Overall average of all times

timeAverages = {}                               # Array to store time averages per 10 sets
timeArray = {}                                  # Array to store time of each set



###########################################################
# Making the GUI window
###########################################################

window = tk.Tk()                                # Initialize the window screen
window.geometry('1000x600')                     # Give window its dimensions
window.configure(background="dark gray")        # Change background color to gray (easier on the eyes)



###########################################################
# Delete frame to make room for a new frame
###########################################################

# Function that clears screen to allow new variables to be used
def clear_screen():
    for widget in window.winfo_children():      # Calls on all window children variables
        widget.destroy()                        # Destroys all window children variables



###########################################################
# Making the Intro Screen
###########################################################

# Intro screen for user to prep and get ready in
def intro_screen():
    clear_screen()                              # Not needed for the first time but needed for restarts at the end

    global bw                                   # Call on global button width
    global bh                                   # Call on global button height
    
    bw = 20                                     # Reassign button width for restarting the test
    bh = 10                                     # Reassign button height for restarting the test

    global title                                # Call on global title
    title = tk.Label(                           # Initialize title on intro screen
        master = window,
        text = "Fitts Law"
    )
    title.pack()

    startButton = tk.Button(                    # Initialize start button
        master = window,
        text = "Press to Start",
        width = 25,
        height = 5,
        background = "white",
        foreground = "black",
        command=lambda: difficulty_levels()
    )
    startButton.place(x = 380, y = 200)         # Initialize placement of start button



###########################################################
# Making the Difficulty Levels Screen
###########################################################

# Function that will make the basic layout for levels
def difficulty_levels():
    clear_screen()                              # Clears screen content to make room for a new screen

    global title                                # Call on global title
    title = tk.Label(                           # Initialize title for difficulty levels screen
        master = window,
        text = "Difficulty Level " + str(difflvlcounter + 2)
    )
    title.pack()

    global blueButton                           # Call on global blue button
    blueButton = tk.Button(                     # Initialize blue button info
        master = window,
        text = "Start Timer",
        width = bw,
        height = bh,
        foreground = "white",
        background = "blue",
        command = start_Timer
    )
    blueButton.pack()

    global redButton                            # Call on global red button
    redButton = tk.Button(                      # Initialize red button info (disabled to start)
        master = window,
        text = "Stop Timer",
        width = bw,
        height = bh,
        foreground = "black",
        background = "gray",
        state = tk.DISABLED,
        command = add_To_Counter
    )
    redButton.pack()

    blueButton.place(x = 150, y = 200)          # Initial blue button placement
    redButton.place(x = 650, y = 200)           # Initial red button placement



###########################################################
# Make the Difficulty Completion Screen
###########################################################

# Function to make screen between each difficulty    
def difficulty_Completion_Screen():
    clear_screen()                              # Clears the content on the screen for a new screen

    global title                                # Call on global title
    global difflvlcounter                       # Call on global difficulty level counter
    title = tk.Label(                           # Initialize title on next level screen
        master = window,
        text = "Difficulty " + str(difflvlcounter + 2) + " Complete"
    )
    title.pack()

    global averagesTitle                        # Call on global average title
    averagesTitle = tk.Label(                   # Initialize average title on difficulty completion screen
        master = window,
        text = ""
    )
    averagesTitle.pack()

    nextLevelButton = tk.Button(                # Initialize next level button
        master = window,
        text = "Start Next Difficulty",
        width = 25,
        height = 5,
        background = "white",
        foreground = "black",
        command=lambda: difficulty_levels()
    )
    nextLevelButton.place(x = 450, y = 250)     # Initialize placement of start button
    averagesTitle.place(x = 300, y = 100)       # Initialize placement of averages title



###########################################################
# Make the End Screen
###########################################################

# Function to make end screen and print times out to a text file
def end_Screen():
    clear_screen()                              # Not needed for the first time but needed for restarts at the end

    global title                                # Call on global title
    title = tk.Label(                           # Initialize title on end screen
        master = window,
        text = "Finished Trials"
    )
    title.pack()

    global averagesTitle                        # Call on global average title
    averagesTitle = tk.Label(                   # Initialize average title on end screen
        master = window,
        text = ""
    )
    averagesTitle.pack()

    restartButton = tk.Button(                  # Initialize restart button
        master = window,
        text = "Back to Intro",
        width = 25,
        height = 5,
        background = "white",
        foreground = "black",
        command=lambda: intro_screen()
    )
    restartButton.place(x = 450, y = 300)       # Initialize placement of start button
    averagesTitle.place(x = 300, y = 100)       # Initialize placement of averages title



###########################################################
# Make the Difficulty Completion Screen
###########################################################

# Function to make screen between each difficulty
def calculate_Averages():
    global timeArray
    global timeAverages
    global trialAverage
    global averagesTitle
    global overallAverage

    if pairCounter <= 30:                       # Calculates averages of sets 1 - 3
        for i in range(10):
            trialAverage = trialAverage + timeArray[i]
        timeAverages[0] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 10]
        timeAverages[1] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 20]
        timeAverages[2] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        averagesTitle.configure(text = "The averages for your first 3 rounds in seconds are:\n"
            + str(timeAverages[0]) + "\n"
            + str(timeAverages[1]) + "\n"
            + str(timeAverages[2])
        )
    
    elif pairCounter <= 60:                     # Calculate averages of sets 4 - 6
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 30]
        timeAverages[3] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 40]
        timeAverages[4] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 50]
        timeAverages[5] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        averagesTitle.configure(text = "The averages for your second 3 rounds in seconds are:\n"
            + str(timeAverages[3]) + "\n"
            + str(timeAverages[4]) + "\n"
            + str(timeAverages[5])
        )
        
    elif pairCounter <= 90:                     # Calculate averages of sets 7 - 9
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 60]
        timeAverages[6] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 70]
        timeAverages[7] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 80]
        timeAverages[8] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        averagesTitle.configure(text = "The averages for your third 3 rounds in seconds are:\n"
            + str(timeAverages[6]) + "\n"
            + str(timeAverages[7]) + "\n"
            + str(timeAverages[8])
        )

    elif pairCounter <= 120:                    # Calculate averages of sets 10 - 12
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 90]
        timeAverages[9] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 100]
        timeAverages[10] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 110]
        timeAverages[11] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        averagesTitle.configure(text = "The averages for your fourth 3 rounds in seconds are:\n"
            + str(timeAverages[9]) + "\n"
            + str(timeAverages[10]) + "\n"
            + str(timeAverages[11])
        )
    
    else:                                       # Calculate averages of sets 13 - 15
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 120]
        timeAverages[12] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 130]
        timeAverages[13] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(10):
            trialAverage = trialAverage + timeArray[i + 140]
        timeAverages[14] = trialAverage / 10
        trialAverage = 0                        # Reset variable for reuse later
        for i in range(150):
            overallAverage = overallAverage + timeArray[i]
        overallAverage = overallAverage / 150
        averagesTitle.configure(text = "The averages for your last 3 rounds plus your overall average in seconds are:\n"
            + str(timeAverages[12]) + "\n"
            + str(timeAverages[13]) + "\n"
            + str(timeAverages[14]) + "\n"
            + str(overallAverage)
        )

        with open("results.txt", "a") as f:     # Write to results.txt file and append ("a") its contents
            for i in range(len(timeArray)):     # Loop to print out all recorded times with respective info
                print("Trial " + str(i + 1) + "'s time in seconds on difficulty " + str(int((i) / 30) + 2) + " to complete: " + str(timeArray[i]) + "\n", file = f)
            for i in range(len(timeAverages)):  # Loop to print out the average times of all sets of 10 with same size and positioning
                print("Set " + str(i + 1) + "'s average time in seconds to complete: " + str(timeAverages[i]) + "\n", file = f)
            print("Overall average for all trials is: " + str(overallAverage) + "\n", file = f)



###########################################################
# Add to counter and stop timer
###########################################################

# Function to add to counter, enable/disable buttons, and reposition and size buttons when needed, bulk of the code
def add_To_Counter(): 
    global endTime                              # Call on global end time
    endTime = time.time()                       # Assign end time

    global startTime                            # Call on global start time
    global timeToComplete                       # Call on global time to complet
    timeToComplete = endTime - startTime        # Calculate time to complete

    global timeArray                            # Call on global time array
    global pairCounter                          # Call on global counter
    timeArray[pairCounter] = timeToComplete     # Assign completion time to array

    pairCounter = pairCounter + 1               # Increment counter

    disableRedButtonState()                     # Disable red button
    enableBlueButtonState()                     # Enable blue button

    global blueButton                           # Call on global blue button
    global redButton                            # Call on global red button
    global difflvlcounter                       # Call on global difficulty level counter
    global bw                                   # Call on global button width
    global bh                                   # Call on global button height

    if pairCounter < 10:                        # Beginning of level 2 difficulty
        blueButton.place(x = 150, y = 200)      # First position for blue and red buttons
        redButton.place(x = 650, y = 200)
    elif pairCounter < 20:
        blueButton.place(x = 150, y = 300)      # Second position for blue and red buttons
        redButton.place(x = 650, y = 100)
    elif pairCounter < 30:
        blueButton.place(x = 250, y = 350)      # Third position for blue and red buttons
        redButton.place(x = 550, y = 150)

    elif pairCounter == 30 and difflvlcounter == 0:     # Start completion level screen and change size of the buttons
        difficulty_Completion_Screen()          # Screen to let user know a new difficulty is coming up
        calculate_Averages()                    # Calculate averages of the first 3 sets

        difflvlcounter = difflvlcounter + 1     # Increment difficulty level counter

        bw = int(bw * 3 / 4)                    # Resize the width of the buttons
        bh = int(bh * 3 / 4)                    # Resize the height of the buttons

    elif pairCounter < 40:                      # Beginning of level 3 difficulty
        blueButton.place(x = 150, y = 200)      # Fourth position for blue and red buttons
        redButton.place(x = 650, y = 200)
    elif pairCounter < 50:
        blueButton.place(x = 300, y = 350)      # Fifth position for blue and red buttons
        redButton.place(x = 700, y = 250)
    elif pairCounter < 60:
        blueButton.place(x = 200, y = 270)      # Sixth position for blue and red buttons
        redButton.place(x = 600, y = 150)
    

    elif pairCounter == 60 and difflvlcounter == 1:     # Start completion level screen and change size of the buttons
        difficulty_Completion_Screen()          # Screen to let user know a new difficulty is coming up
        calculate_Averages()                    # Calculate averages for the second 3 sets


        difflvlcounter = difflvlcounter + 1     # Increment difficulty level counter

        bw = int(bw * 3 / 4)                    # Resize the width of the buttons
        bh = int(bh * 3 / 4)                    # Resize the height of the buttons

    elif pairCounter < 70:                      # Beginning of level 4 difficulty
        blueButton.place(x = 150, y = 200)      # Seventh position for blue and red buttons
        redButton.place(x = 650, y = 200)
    elif pairCounter < 80:
        blueButton.place(x = 200, y = 350)      # Eighth position for blue and red buttons
        redButton.place(x = 600, y = 450)
    elif pairCounter < 90:
        blueButton.place(x = 400, y = 350)      # Ninth position for blue and red buttons
        redButton.place(x = 600, y = 150)

    elif pairCounter == 90 and difflvlcounter == 2:     # Start completion level screen and change size of the buttons
        difficulty_Completion_Screen()          # Screen to let user know a new difficulty is coming up
        calculate_Averages()                    # Calculate averages for the third 3 sets

        difflvlcounter = difflvlcounter + 1     # Increment difficulty level counter

        bw = int(bw * 3 / 4)                    # Resize the width of the buttons
        bh = int(bh * 3 / 4)                    # Resize the height of the buttons

    elif pairCounter < 100:                     # Beginning of level 5 difficulty
        blueButton.place(x = 150, y = 200)      # Tenth position for blue and red buttons
        redButton.place(x = 650, y = 200)
    elif pairCounter < 110:
        blueButton.place(x = 200, y = 350)      # Eleventh position for blue and red buttons
        redButton.place(x = 600, y = 150)
    elif pairCounter < 120:
        blueButton.place(x = 300, y = 150)      # Twelfth position for blue and red buttons
        redButton.place(x = 800, y = 450)

    elif pairCounter == 120 and difflvlcounter == 3:    # Start completion level screen and change size of the buttons
        difficulty_Completion_Screen()          # Screen to let user know a new difficulty is coming up
        calculate_Averages()                    # Calculate averages for the fourth 3 sets

        difflvlcounter = difflvlcounter + 1     # Increment difficulty level counter

        bw = int(bw * 3 / 4)                    # Resize the width of the buttons
        bh = int(bh * 3 / 4)                    # Resize the height of the buttons

    elif pairCounter < 130:                     # Beginning of level 6 difficulty
        blueButton.place(x = 150, y = 200)      # Thirteenth position for blue and red buttons
        redButton.place(x = 650, y = 200)
    elif pairCounter < 140:
        blueButton.place(x = 100, y = 350)      # Fourteenth position for blue and red buttons
        redButton.place(x = 800, y = 150)
    elif pairCounter < 150:
        blueButton.place(x = 400, y = 300)      # Fifthteenth position for blue and red buttons
        redButton.place(x = 700, y = 350)

    else:
        end_Screen()                            # Move to the end screen
        calculate_Averages()                    # Calculate average for the last 3 sets



###########################################################
# Start timer
###########################################################

#Function to start the timer, disable blue button, and enable red button
def start_Timer():
    global startTime                            # Call on global start time
    startTime = time.time()                     # Assign start time
    disableBlueButtonState()                    # Disable blue button
    enableRedButtonState()                      # Enable red button



###########################################################
# Enable/Disable Buttons
###########################################################
        
# Function to disable red button
def disableRedButtonState():
    global redButton                            # Call on global red button
    redButton.configure(                        # Reconfigure red button to be disabled
        state = tk.DISABLED,
        background = "gray",
        foreground = "black"
    )

# Function to enable the red button
def enableRedButtonState():
    global redButton                            # Call on global red button
    redButton.configure(                        # Reconfigure red button to be enabled
        state = tk.NORMAL,
        background = "red"
    )

# Function to disable the blue button
def disableBlueButtonState():
    global blueButton                           # Call on global blue button
    blueButton.configure(                       # Reconfigure blue button to be disabled
        state = tk.DISABLED,
        background = "gray"
    )

# Function to enable the blue button
def enableBlueButtonState():
    global blueButton                           # Call on global blue button
    blueButton.configure(                       # Reconfigure blue button to be enabled
        state = tk.NORMAL,
        background = "blue"
    )



###########################################################
# Running the code
###########################################################

intro_screen()                                  # Start program
window.mainloop()                               # Loop to continue window working until X in top right is clicked