dev:
	pip install -r requirements.txt
	pip install -r test-requirements.txt
run-tests:
	python3 -c "import pytest" > /dev/null 2>&1 || python3 -m pip install pytest
	python3 -m pytest -qq
coverage:
	python3 -c "import pytest" > /dev/null 2>&1 || python3 -m pip install pytest
	python3 -c "import coverage" > /dev/null 2>&1 || python3 -m pip install coverage
	python3 -m coverage run -m pytest -qq
	rm -r htmlcov || true
	python3 -m coverage report

coverage-html:
	python3 -c "import pytest" > /dev/null 2>&1 || python3 -m pip install pytest
	python3 -c "import coverage" > /dev/null 2>&1 || python3 -m pip install coverage
	python3 -m coverage run -m pytest -qq
	rm -r htmlcov || true
	python3 -m coverage report
	python3 -m coverage html
