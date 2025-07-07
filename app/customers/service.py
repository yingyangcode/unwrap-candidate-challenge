from app.customers.interfaces import CustomerRepositoryInterface
from app.customers.models import Customer
from app.exceptions import CustomerNotFoundException


class CustomerService:
    def __init__(self, customer_repo: CustomerRepositoryInterface):
        self.customer_repo = customer_repo
    
    def create_customer(self, name: str, email: str, customer_id: str) -> Customer:
        customer = Customer(
            name=name,
            email=email,
            customer_id=customer_id
        )
        
        result = self.customer_repo.create(customer)
        return result
    
    def get_customer_by_id(self, customer_id: str) -> Customer:
        customer = self.customer_repo.get_by_id(customer_id)
        if not customer:
            raise CustomerNotFoundException(customer_id)
        
        return customer