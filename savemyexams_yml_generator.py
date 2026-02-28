import os
import yaml
import sys

# ==============================================================================
# CONFIGURACIÓN DE RUTAS
# ==============================================================================
base_path = os.path.join("tareas", "savemyexams") # Carpeta de origen
output_dir = "_data"                             # Carpeta de destino Jekyll
output_file = os.path.join(output_dir, "savemyexams.yml")

# ==============================================================================
# VALIDACIONES DE SEGURIDAD (PROTECCIONES)
# ==============================================================================

# 1. Detener si la carpeta _data no existe (No crea carpetas nuevas)
if not os.path.exists(output_dir):
    print(f"❌ ERROR: La carpeta '{output_dir}' no existe. Proceso detenido.")
    sys.exit()

# 2. Detener si el archivo YAML ya existe (No sobrescribe por accidente)
if os.path.exists(output_file):
    print(f"⚠️ AVISO: El archivo '{output_file}' ya existe. Bórralo para regenerar.")
    sys.exit()

# 3. Diccionario de traducción para nombres limpios en inglés
translations = {
    "Algebra_Sequences": "Algebra & Sequences",
    "Coordinate_Geometry_Graphs": "Coordinate Geometry & Graphs",
    "Geometry": "Geometry",
    "Investigations_Modelling": "Investigations & Modelling",
    "Lengths_Areas_Volumes": "Lengths, Areas & Volumes",
    "Number": "Number",
    "Probability": "Probability",
    "Pythagoras_Trigonometry": "Pythagoras & Trigonometry",
    "Statistics": "Statistics",
    "Vectors_Transformations": "Vectors & Transformations"
}

data_structure = []

# ==============================================================================
# PROCESAMIENTO DE ARCHIVOS Y AGRUPACIÓN
# ==============================================================================
try:
    # Recorrer cada carpeta de tema
    for topic_folder in sorted(os.listdir(base_path)):
        topic_path = os.path.join(base_path, topic_folder)
        
        # Filtrar solo carpetas reales y omitir ocultas
        if os.path.isdir(topic_path) and not topic_folder.startswith('.'):
            display_name = translations.get(topic_folder, topic_folder.replace("_", " "))
            
            topic_entry = {
                "topic": display_name,
                "id": topic_folder.lower().replace("_", "-"),
                "tasks": []
            }
            
            files = sorted(os.listdir(topic_path))
            temp_tasks = {} # Para agrupar 'tema.pdf' con 'tema-calculator.pdf'

            for filename in files:
                if filename.endswith(".pdf"):
                    # Detectar si es versión calculadora
                    is_calculator = "-calculator" in filename
                    # Nombre base para agrupar (elimina '-calculator' y la extensión)
                    base_name = filename.replace("-calculator", "").replace(".pdf", "")
                    
                    # Si la tarea no existe en el grupo temporal, se crea
                    if base_name not in temp_tasks:
                        temp_tasks[base_name] = {
                            "id": f"{topic_entry['id']}-{base_name}",
                            "title": base_name.replace("-", " ").title(),
                            "variants": []
                        }
                    
                    # Definir etiqueta según el nombre del archivo
                    v_name = "Calculator" if is_calculator else "Non-Calculator"
                    v_path = f"/tareas/savemyexams/{topic_folder}/{filename}"

                    temp_tasks[base_name]["variants"].append({
                        "name": v_name,
                        "file": filename,
                        "path": v_path,
                        "type": "calc" if is_calculator else "standard" # Etiqueta para CSS
                    })

            # Convertir el diccionario temporal a la lista final de tareas
            topic_entry["tasks"] = list(temp_tasks.values())
            data_structure.append(topic_entry)

    # ==============================================================================
    # GUARDADO DEL YAML
    # ==============================================================================
    with open(output_file, 'w', encoding='utf-8') as f:
        yaml.dump(data_structure, f, sort_keys=False, allow_unicode=True)
    
    print(f"✅ YAML generado con éxito en {output_file}")

except Exception as e:
    print(f"❌ Error inesperado: {e}")