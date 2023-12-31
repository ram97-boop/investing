.PHONY: test
test:
	pytest -vv

.PHONY: format
format:
	black .