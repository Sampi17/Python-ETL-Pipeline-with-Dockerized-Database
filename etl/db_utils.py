from dotenv import load_dotenv 
from sqlalchemy import create_engine, text
import os

load_dotenv()

def connection(host='container-host', port=5432):  # Default to localhost
    """Create database connection with fallback"""
    try:
        db_user = os.getenv('POSTGRES_USER')
        db_password = os.getenv('POSTGRES_PASSWORD')
        db_name = os.getenv('POSTGRES_DB')
        
        if not all([db_user, db_password, db_name]):
            raise ValueError("Missing database credentials in environment variables")
        
        engine = create_engine(
            f"postgresql://{db_user}:{db_password}@{host}:{port}/{db_name}"
        )
        
        # Test connection
        with engine.begin() as conn:
            conn.execute(text("SELECT 1"))
            
        print("Database connection successful")
        return engine
        
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise

def create_table():
    """Create table if it doesn't exist"""
    engine = connection()
    try:
        with engine.begin() as conn:
            conn.execute(text(
                 """CREATE TABLE IF NOT EXISTS employee_data (
                        empid  VARCHAR(50) PRIMARY KEY,
                        age INTEGER NOT NULL,
                        gender VARCHAR(20) NOT NULL,
                        employmentstatus VARCHAR(10) NOT NULL,
                        businesstravel VARCHAR(50) NOT NULL,
                        department VARCHAR(100) NOT NULL,
                        education INTEGER NOT NULL,
                        educationfield VARCHAR(100) NOT NULL,
                        jobrole VARCHAR(100) NOT NULL,
                        yearsatcompany INTEGER NOT NULL
                    );"""
            ))
        print("Table created or already exists")
    except Exception as e:
        print(f"Table creation failed: {e}")
        raise