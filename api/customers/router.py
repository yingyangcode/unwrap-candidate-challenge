from fastapi import APIRouter
from api.customers.schemas import CustomerCreateSchema, CustomerResponseSchema
from app.customers.service import CustomerService
from app.customers.repository import CustomerRepository
from app.storage.memory_store import memory_store

router = APIRouter(tags=["customers"])


@router.post("/customers", response_model=CustomerResponseSchema, status_code=201)
def create_customer(request: CustomerCreateSchema):
    customer_repo = CustomerRepository(memory_store)
    customer_service = CustomerService(customer_repo)
    customer_result = customer_service.create_customer(
        name=request.name,
        email=request.email,
        customer_id=request.customer_id
    )
    return CustomerResponseSchema(**customer_result.model_dump())


@router.get("/customers/{customer_id}", response_model=CustomerResponseSchema)
def get_customer(customer_id: str):
    customer_repo = CustomerRepository(memory_store)
    customer_service = CustomerService(customer_repo)
    customer_result = customer_service.get_customer_by_id(customer_id)
    return CustomerResponseSchema(**customer_result.model_dump())