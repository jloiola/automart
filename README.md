# Automart Code Challenge

This repo contains part of a simple api for a fictional Japanese autoparts store. This api needs to keep track of customers, as well as vehicle makes and models, which it gets from a 3rd party API.

## User stories

There are two user stories provided below. Please review each and implement them in the app.

As you might with a ticket for a real application, please explain any assumptions you may have made, any points of confusion etc if applicable. Feel free to include these notes directly under the stories in the "Dev Comments" section.

### Task #1: Add Endpoint to Update Customer Info

Add an endpoint that allows for updating customer records.

**Acceptance Criteria:**

- The endpoint allows for the updating of the customer's first name and last name. Both fields can be updated in one request, but both don't have to be specified.
- The API considers possible errors and edge cases, and raises errors with appropriate HTTP status codes.

**Dev Comments:**

...


### Task #2: Add Functionality to Keep Our Vehicle Data up to Date

Vehicle makes the store supports are stored in the database. The models these manufactures produce should be stored in the database as well, but must be kept in sync as manufactures add or discontinue models.

Use the [NHTSA API](https://vpic.nhtsa.dot.gov/api/) to fetch the latest data about the makes and create, update, and/or delete their associated models accordingly in the database.

Create an endpoint that triggers this fetching and sync process.

**Acceptance Criteria:**

- Sending a request to the endpoint starts the process to update the model data stored in our database with the latest data on vehicle models pulled from the NHTSA.
- The API endpoint returns a JSON object containing a list of the makes that were updated.
- Assuming that the number of makes and models continues to grow, the endpoint should consider best practices for slow running processes in an API. FastAPI's [Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/?h=backg#background-tasks) could be one way to handle this, but note, there is no one right answer for this. Use your best judgement.
- The API considers possible errors and edge cases, and raises errors with appropriate HTTP status codes.
- The process only updates model data for makes that are currently listed in our database.
- The process must account for the future addition of more makes to our database.

**Dev Comments:**

...

**Notes/Tips on NHTSA API Usage**

- The `id`s in our tables match the make and model ids that the NHTSA use.
- Here's an example use of one of their endpoints:

```bash
curl "https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMakeId/440?format=json"
```

### Bonus Task: Implement Unit Testing

If time allows, consider adding unit tests for the two endpoints you just added.

We'd prefer this be treated purely as a bonus: take the time to make the 2 tasks above as complete as they can be. Once you feel they're fully complete, start on this if you have extra time.

We already have one test in place for the `GET /customer/{id}` endpoint as an example.

To run the tests:

```bash
python -m pytest
```

## Getting started

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

![Alt OpenAPI Screenshot](docs/open-api-screenshot.png?raw=true "OpenAPI Screenshot")
