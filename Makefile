.PHONY: build run clean frontend

build:
	python -m venv .venv
	. .venv/bin/activate
	pip install --upgrade pip
	pip install -r requirements.txt

run:
	. .venv/bin/activate && reflex run

frontend: build
	. .venv/bin/activate && reflex export --frontend-only
	rm -rf public/
	mkdir -p public/
	unzip -o frontend.zip -d public/
	rm frontend.zip

clean:
	rm -rf .venv/
	rm -rf .states/
	rm -rf .web/
	rm -rf public/
	find . -name "__pycache__" -type d -exec rm -rf {} +