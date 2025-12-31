from Contact import Contact_DA
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


@router.get("/contacts")
def list_contacts():
    get_list = Contact_DA.get_all_contacts()
    return get_list


class ContectBody(BaseModel):
    first_name: str
    last_name: str
    phone_number: str





@router.post("/contacts")
def create_contacts(payload: ContectBody):
    inserted_id = Contact_DA.create_contact(payload.dict())
    return {"message": "The creation was successful.", "id": str(inserted_id)}


# @router.post("/contacts")
# def create_contacts(payload: ContectBody):
#     created = Contact_DA.create_contact(payload)
#     return {"message": "The creation was successful.", "id": created["id"], "contact": created["contact"]}




# @router.put("/contacts/{id}")
# def update_contact(payload: ContectBody, id):
#     Contact_DA.update_contact(payload, id)
#     return {"message": "The update was successful."}

@router.put("/contacts/{id}")
def update_contact(payload: ContectBody, id: str):
    Contact_DA.update_contact(payload.dict(), id)
    return {"message": "The update was successful."}



@router.delete("/contacts/{id}")
def delete_contacts(id):
    Contact_DA.delete_contact(id)
    return {"message": "The delete was successful."}
