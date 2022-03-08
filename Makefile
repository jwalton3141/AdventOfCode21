VIRTUALENV_NAME=venv

.phony: clean test

$(VIRTUALENV_NAME): requirements.txt
	virtualenv -p python3 $(VIRTUALENV_NAME)
	. $(VIRTUALENV_NAME)/bin/activate
	pip install -r requirements.txt

test:
	for day in $$(find -type f -name test_solutions.py -exec dirname {} + | sort); do \
		echo \\nTesting $$(basename $$day)...; \
		cd $$day && pytest && cd ..; \
	done

clean:
	rm -rf $(VIRTUALENV_NAME)
