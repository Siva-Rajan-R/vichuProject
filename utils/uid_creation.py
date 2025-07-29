import uuid

def create_unique_id(data:str):
    try:
        return str(uuid.uuid5(uuid.uuid4(),data))
    except Exception as e:
        print(f"something went wrong while creating unique id {e}")