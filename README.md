CREATE a requirements.txt file 
CREATE a main.py file 
CREATE a virtual environment
python -m venv venv
ACTIVATE ENV: source venv bin/activate
pip install -r requirements.txt
CREATE main: on vs code 
# filename: app
UVICORN: uvicorn main:app --reload \
remote on the same network: uvicorn main:app --reload --host 0.0.0.0      
