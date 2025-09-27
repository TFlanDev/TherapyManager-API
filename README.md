

#Create and activate virtual enviornment
python -m venv venv
source venv/Scripts/activate

#install dependencies 
pip install fastapi
pip install "uvicorn[standard]"
pip install sqlalchemy
pip install psycopg2

#run server
$ uvicorn app:app --reload