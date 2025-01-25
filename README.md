# testgen

To run this FastAPI application, you need to install FastAPI and an ASGI server like uvicorn. You can do this by creating a requirements.txt file:

Then, install the dependencies using pip:

pip install -r requirements.txt

Finally, run the FastAPI application using uvicorn:

uvicorn app.main:app --reload

This will start the FastAPI server, and you can access the endpoint:

test.http test file: 

POST https://testgenfn.azurewebsites.net/api/prinfo HTTP/1.1
Content-Type: application/json

{
    "operator": "subtract",
    "numbers": [10, 5]
}



