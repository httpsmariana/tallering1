from django.conf import settings
from Agro.domain.repositories import ProductRepository  # si es "agro", cambia Agro. por agro.
from Agro.infrastructure.mongo_repository import MongoProductRepository

def get_product_repo() -> ProductRepository:
    repo_kind = getattr(settings, "PRODUCT_REPO", "mongo")
    if repo_kind == "mongo":
        return MongoProductRepository()
    raise RuntimeError("Repositorio de productos no configurado")
