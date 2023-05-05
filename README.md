# Automart

E-commerce platform.

## Code Challenge

https://vpic.nhtsa.dot.gov/api/vehicles/getmakesformanufacturerandyear/988?year=2014&format=json
https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/aston%20martin?format=json

### Getting started

Its assumed you have python>=3.10 installed via your favorite package or version manager.

```bash
# be sure the proceeding command is at least Python 3.10
python -V

# install depedencies
pip install -r requirements.txt

# seed db data
```bash
PYTHONPATH=$(pwd) python data/setup_db.py
```

# start the app
```bash
./start
```

Open API should be available at http://localhost:9000