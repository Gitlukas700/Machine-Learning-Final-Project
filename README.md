# Machine-Learning-Final-Project
This program uses a genetic algorithm to generate a team composition.
The fitness for each team is judged based on the sum of their average win rates.
It doesn't take any other statistic into account past this average win rate sum.

The data used is provided by kaggle from the following link:



step 1:
    Set up a virtual environment of you preference

step 2:
    Download all requirments with the command "pip install requirments"

step 3:
    Use the following command to launch the front end local server.
    A link will be provided in the console to take you to the web page.

    python -m flask --app main run

Step 4:
    Clicking the button "generate new team" well create a new team through the use
    of a genetic algorithm. Along with a plot of the fitness through
    each generation.

Notes:
    The graph is displayed by saving a plot as a png then giving a command to open it
    This was a needed work around since just displaying the plot did not work at all.