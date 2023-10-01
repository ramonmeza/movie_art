SOURCE_DIR=movie_art

.PHONY: lint tests

lint:
	pylint ${SOURCE_DIR} 

tests:
	pytest tests