.PHONY: test
test:
	pytest -vv

.PHONY: format
format:
	black .

.PHONY: run
run:
	python3 src/investing/compound.py