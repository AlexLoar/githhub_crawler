up:
	uvicorn src.views:app --reload --workers 2 --host 0.0.0.0 --port 8000

test:
	pytest -vv
