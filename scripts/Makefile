.PHONY: run

run:
	python3 -m venv docs && \
	. docs/bin/activate && \
	pip install -r requirements.txt && \
	python3 update_docs.py && \
	python3 update_navigation.py

clean:
	rm -rf docs