install:
	python -m pip install --upgrade pip

format:
	# yapf --in-place --recursive --style="{indent_width: 4}" *.py Lambdas/

lint:
	find Lambdas -name 'stpAddress*.py' ! -name 'z_*.py' -exec python -m pylint --disable=R,C {} +

test:
	python -m pytest -vv *.py
	
debug:
	python -m pytest -vv --pdb --cov=. --cov=tests

pull:
	git pull origin main
	
branch:
	# List all branches and their last commit date
	git for-each-ref --sort=-committerdate --format='%(refname:short) %(committerdate:relative)' refs/heads

reset:
	# Discard all changes in the working directory
	git reset --hard HEAD

clean:
	# Remove all untracked files and directories
	git clean -fd

all: install format lint test