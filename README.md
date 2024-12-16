# Solución Parcial

## Solución Parcial Backend

[Solución parcial backend]

### Instrucciones para ejecutar la solución backend

1. Clona el repositorio:
   ```sh
   git@github.com:Santiago4271/parcial_aplicaciones_web.git
2. Navega al directorio del proyecto:
   cd tu-repositorio-backend

3. Crea y activa un entorno virtual:
   python -m venv venv
   
   source venv/bin/activate  # En Windows usa `source   
   venv\Scripts\activate`

5. Instala las dependencias
   fastapi
   
   uvicorn
   
   sqlalchemy
   
   pydantic
   
   databases

7. Ejecuta la aplicación:
   uvicorn main:app --reload o uvicorn backend.main:app --reload
