TEST_RESULT_FILE="results.txt"
TEST_RESULT_FILE_PATH=$(TEST_RESULT_FILE)

all: install test run deploy

install:
    @echo "Preparing environment..."
    pipenv --python 3.8
    pipenv install requests
    pipenv install ntplib
    pipenv install pytest

test:
    @echo "Testing the app with unit-tests..."
    @echo "========= [$$(date)] "========= >> $(TEST_RESULT_FILE_PATH)
    pipenv run pytest tests/tests.py >> $(TEST_RESULT_FILE_PATH)

run:
    @echo "Running app.py file..."
    @echo "==== [$$(date)] ====" >> $(TEST_RESULT_FILE)
    pipenv run python3 app.py >> $(TEST_RESULT_FILE)

deploy:
    @echo "Deploying..."
    git add $(TEST_RESULT_FILE)
    git add $(TEST_RESULT_FILE_PATH)
    git commit -m "Lab 2: [deploy] $$(date)"
    git push origin lab2