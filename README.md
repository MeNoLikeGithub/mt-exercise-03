# MT Exercise 3: Pytorch RNN Language Models

This repo shows how to train neural language models using [Pytorch example code](https://github.com/pytorch/examples/tree/master/word_language_model). Thanks to Emma van den Bold, the original author of these scripts. 

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/moritz-steiner/mt-exercise-03
    cd mt-exercise-03

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software:

    ./scripts/install_packages.sh

Download and preprocess data:

    ./scripts/download_data.sh

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh
	


# Run order

Should have remained the same, except that the table generating script is added at the end.

# Changes

- Changed the source text by replacing the number on the original link with a random different number.
- Replaced all instances of the old folder/file names (grimm/numbers) in train/download/generate scripts with the new ones (tom/4711).
- Edited "/tools/pytorch-examples/word language model/main.py" to gather all the necessary data in lists that are then written as a csv log file at the location specified in the train-script.
- For the creation of the models/data at different dropout levels the train script had the save-locations modified for each run.
- Added Bokeh and Pandas to the install_packages script.
- Created the "TablesnGraphs" python script that produces the "Tables_and_Graphs" HTML-file containing the tables and graphs of the data.
- For the creation of the different samples the generate script had the save-location modified for each run.
