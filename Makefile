VIRTUALENV_NAME=venv

.phony: clean test

$(VIRTUALENV_NAME): requirements.txt
	virtualenv -p python3 $(VIRTUALENV_NAME)
	. $(VIRTUALENV_NAME)/bin/activate
	pip install -r requirements.txt

test:
	./scripts/pytest.sh

clean:
	rm -rf $(VIRTUALENV_NAME)
