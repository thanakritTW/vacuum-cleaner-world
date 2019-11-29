unittest:
	python3 -m unittest discover -v -s tests

integration:
	python3 -m unittest discover -v -s tests/integration

test: unittest integration