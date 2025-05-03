.PHONY: build run clean

build:
	python -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	. .venv/bin/activate && reflex run

clean:
	rm -rf .venv/
	rm -rf .states/
	rm -rf .web/
	find . -name "__pycache__" -type d -exec rm -rf {} +