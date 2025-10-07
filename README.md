# P1-AgroMerc
this repository is designed to do a EAFIT University´s student project 

## Cómo correr
1. Definir variable de entorno:
   - Windows (PowerShell): `setx MONGODB_URI "mongodb+srv://USUARIO:PASS@CLUSTER/db?..."`
   - macOS/Linux: `export MONGODB_URI="mongodb+srv://USUARIO:PASS@CLUSTER/db?..."`
2. `python manage.py makemigrations && python manage.py migrate`
3. `python manage.py runserver`
4. DIP + Strategy: `http://127.0.0.1:8000/patterns/products/`
5. CRUD Categorías (CBV): `http://127.0.0.1:8000/patterns/categories/`

## Actividad 2 — Revisión autocrítica
- **Usabilidad**: plantillas separadas, orden dinámico (Strategy). _Mejora_: navbar reusable, paginación.
- **Compatibilidad**: URLs limpias. _Mejora_: estandarizar endpoints y contratos si se expone API.
- **Rendimiento**: índices Mongo (`name`, `category`, `created_at`). _Mejora_: paginación y cache por vista.
- **Seguridad**: `ALLOWED_HOSTS`, credenciales en `MONGODB_URI`, CSRF activo. _Mejora_: `SECRET_KEY` en `.env`.

## Actividad 3 — Inversión de Dependencias (DIP)
- **Interfaz**: `Agro/domain/repositories.py` → `ProductRepository`.
- **Infra**: `Agro/infrastructure/mongo_repository.py` → `MongoProductRepository` (+ índices).
- **Proveedor**: `Agro/services.py` → `get_product_repo()`.
- **Uso en vistas**: controladores dependen de la **interfaz**, no de PyMongo.

## Actividad 4 — Patrón Python (Strategy)
- **Archivo**: `Agro/domain/sorting.py` (Price ↑/↓, Newest).
- **Vista**: `ProductListView` selecciona estrategia via `?order=` sin modificar la vista (OCP).

## Actividad 5 — Patrones Django
- **Controladores**: Generic **CBV** para `Category` (`List/Create/Update/Delete`) en `views_patterns.py`.
- **Modelos (Normalización)**: `Agro/models.py` → `Category(name unique, description)`; `makemigrations/migrate`.

