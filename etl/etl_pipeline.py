from extract import extract_data
from transform import transform_data
from load import load_data 
import traceback

def main():
    try:
        print("Starting ETL pipeline...")
        
        # Extract
        print("Step 1: Extracting data...")
        data = extract_data()
        
        # Transform
        print("Step 2: Transforming data...")
        data = transform_data(data)
        
        # Load
        print("Step 3: Loading data...")
        load_data(data)
        
        print("ETL pipeline completed successfully!")
        
    except Exception as e:
        print(f"ETL pipeline failed: {e}")
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())