# Automart

## Code Challenge

### Getting started

Its assumed you have python>=3.10 installed via your favorite package or version manager.

```bash
# be sure the proceeding command is at least Python 3.10
python -V

# install depedencies
pip install -r requirements.txt

# seed db data
PYTHONPATH=$(pwd) python data/setup_db.py

# start the app
./start
```

Open API docs should be available at http://localhost:9000/docs