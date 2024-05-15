# Ecton

Ecton Recruiting Task


## Author
[Maciej Zięba \<maciekz82@gmail.com\>](https://github.com/maciekz)


## Installation

Create a python virtualenv and activate it:

```
python -m venv venv
source ./venv/bin/activate
```

Install application and its dependencies:

```
pip install -e .
```


## Running the application

Use the virtualenv's `python` interpreter to run the `read_recipes.py` script providing input folder and output file as parameters:

```
python src/ecton_recruiting_task/read_recipes.py --input_directory ./src/ecton_recruiting_task/tests/test_data/ --output_file output.json
```


## Running tests

To run tests, use the `pytest` command:

```
pytest src/ecton_recruiting_task/tests
```