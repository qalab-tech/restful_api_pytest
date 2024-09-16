RESTful API Testing Framework with pytest
This project is a RESTful API testing framework built using pytest. It includes a collection of tests for various HTTP methods such as GET, POST, PATCH, and DELETE, and is designed to test the public API JSONPlaceholder.

The tests are written using pytest for automation and are configurable via a config.yaml file, which allows you to specify the base URL of the API being tested.

Features

Automated testing of RESTful API methods (GET, POST, PATCH, DELETE).
Configurable base URL using config.yaml.
Uses pytest for parameterized testing and test execution.
Detailed HTML test reports using pytest-html.
Parallel test execution with pytest-xdist.
Easy to extend and adapt for other APIs.

Project Structure

├── config.yaml           # Configuration file for the base URL
├── posts_methods_tests.py # Test file for API methods
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation

Requirements
Before running the tests, ensure you have Python 3.7+ installed. You can install the necessary packages using pip and the requirements.txt file.

Installation

1. Clone this repository:
git clone https://github.com/yourusername/RESTful_API_pytest.git
cd RESTful_API_pytest

2. Create a virtual environment (optional, but recommended):
python -m venv venv
source venv/bin/activate    # On Windows use: venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

Configuration
Set the base URL of the API you want to test in the config.yaml file:

API base URL: "https://jsonplaceholder.typicode.com/posts"

Running Tests
1. To run all the tests: 
pytest
2. To run tests and generate an HTML report:
pytest --html=report.html
3. To run tests with detailed output (verbosity):
pytest -v
4. Running Tests in Parallel
For larger test suites, you may want to run tests in parallel to speed up the process. 
Using pytest-xdist, you can easily execute tests across multiple processes:
pytest -n 4

For parallel execution, you'll need to have pytest-xdist installed (included in requirements.txt).
This will run the tests across 4 parallel workers.

Contribution
Feel free to fork this repository and add your own tests or improvements. Pull requests are welcome!

License
This project is licensed under the MIT License.






