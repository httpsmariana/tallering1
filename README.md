# P1-AgroMerc
this repository is designed to do a EAFIT University´s student project 

## Requisitos
- Python 3.10+
- pip
(Opcional) MongoDB Atlas si quieres probar el modo mongo

## Cómo correr (TL;DR)
# 1) Crear y activar venv (opcional pero recomendado)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Modo demo sin DB (recomendado para la entrega)
# En AgroMerc/settings.py debe estar:
# PRODUCT_REPO = "memory"

# 4) Ejecutar
python manage.py runserver


## Actividad 2 — Revisión autocrítica (Usabilidad, Compatibilidad, Rendimiento, Seguridad)

Usabilidad
- Formularios simples (forms.py) y vistas claras (/patterns/products/)
- Orden configurable por URL (?order=) sin recargar lógica de vista.
- Inversión sugerida: agregar navegación/base template y paginación si crece el listado.

Compatibilidad
- Modo demo sin DB (en memoria) para no depender de Atlas.
- Alternancia de repositorio por setting (PRODUCT_REPO).
- Inversión sugerida: estandarizar contratos si se expone API (nombres/formatos).

Rendimiento
- En memoria no hay I/O (rápido para demo).
- Inversión sugerida: cuando migre a Mongo, añadir índices en name, category, created_at y paginación en listados.

Seguridad
- No se suben credenciales; variables por entorno cuando se use Mongo.
- Inversión sugerida: mover SECRET_KEY y configuraciones sensibles a .env, validar entradas de usuario en formularios complejos.

## Actividad 3 — Inversión de Dependencias (DIP)

Qué se hizo
Interfaz ProductRepository → Agro/domain/repositories.py.

Implementaciones:
MongoProductRepository → Agro/infrastructure/mongo_repository.py.
MemoryProductRepository → Agro/infrastructure/memory_repository.py (demo).
Selector get_product_repo() → Agro/Services.py.

Uso
Las vistas no dependen de una tecnología concreta; piden get_product_repo() y trabajan contra la interfaz. Cambiar de memoria a Mongo no requiere tocar las vistas.


## Actividad 4 — Patrón de diseño Python: Strategy

Problema
La lista de productos puede ordenarse por distintos criterios (más nuevos, precio asc/desc). Sin Strategy, la vista crecería con ifs y lógica duplicada.

Decisión
Se aplicó Strategy para encapsular cada criterio de orden.

Implementación
Archivo: Agro/domain/sorting.py
SortByNewest, SortByPriceAsc, SortByPriceDesc
En views_patterns.py, se selecciona estrategia por ?order=:
STRATEGIES = {"newest": ..., "price_asc": ..., "price_desc": ...}
strategy = STRATEGIES.get(order, STRATEGIES["newest"])
productos = list(strategy.apply(repo.list()))

Cumple OCP (Open/Closed)


## Actividad 5 — Patrones de diseño Django

Se implementan dos patrones en capas distintas, manteniendo todo simple:

Controladores: Class-Based Views (CBV)

Archivo: Agro/views_patterns.py

Vistas:
ProductListView (GET + ordenamiento vía Strategy)
ProductCreateView (formulario para crear productos)

Rutas: Agro/urls_patterns.py
Vistas viven en /patterns/... para no afectar tu app original.

Presentación/Validación: Django Forms
Archivo: Agro/forms.py
Encapsula validación y render de campos.
