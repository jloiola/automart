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

### User stories

__Update Customer Info__
- We want to be able to update customer info
- Update the customers first and last name (more?)

__Sync models by make with NHTSA API__
- We want to have up to date models
- Using the NHTSA API, write an endpoint to sync data for our specified makes
