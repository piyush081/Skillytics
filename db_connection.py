from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def load_secrets(file_path: str):
    secrets = {}
    try:
        with open(file_path, "r") as file:
            for line in file:
                key, value = line.strip().split("=", 1)
                secrets[key.strip()] = value.strip()
    except Exception as e:
        raise Exception(f"Error reading secrets file: {e}")
    return secrets

secrets_file = "secrets.txt"
secrets = load_secrets(secrets_file)

# Build the DATABASE_URL using secrets
DATABASE_URL = f"mysql+mysqlconnector://{secrets['sql_username']}:{secrets['password']}@{secrets['connection']}/{secrets['schema_name']}"


engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()