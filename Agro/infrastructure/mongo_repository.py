import os
from typing import Optional, Dict, Any, Iterable
from pymongo import MongoClient
from bson import ObjectId

from Agro.domain.repositories import ProductRepository  # Si tu app es "agro" usa: from agro.domain.repositories import ProductRepository

class MongoProductRepository(ProductRepository):
    def __init__(self, client: MongoClient | None = None):
        uri = os.getenv("MONGODB_URI")
        if not client:
            client = MongoClient(uri)
        self.db = client["agromerc"]      # cambia el nombre si tu DB es otra
        self.col = self.db["products"]
        self.col.create_index("name")
        self.col.create_index("category")
        self.col.create_index("created_at")

    def add(self, data: Dict[str, Any]) -> str:
        res = self.col.insert_one(data)
        return str(res.inserted_id)

    def get(self, id: str) -> Optional[Dict[str, Any]]:
        return self.col.find_one({"_id": ObjectId(id)})

    def list(self, filters: Optional[Dict[str, Any]] = None) -> Iterable[Dict[str, Any]]:
        return self.col.find(filters or {})
