.PHONY: clean test

test:
	py.test -svx test

clean:
	find . -name "*.pyc" -exec rm {} \;

