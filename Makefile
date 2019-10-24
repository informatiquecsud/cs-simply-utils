test.%:
	@echo "Testing module $*"
	@python -m unittest test_$*

.PHONY: test

test: test.polybius