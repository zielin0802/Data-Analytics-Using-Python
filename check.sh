echo 'Linting...'
flake8 'week1/assignment1_utils.py'
flake8 'week1/test_assignment1_utils.py'
flake8 'week2/assignment2.py'
flake8 'week2/test_assignment2.py'

echo 'Testing...'
pytest
