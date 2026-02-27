import os

def get_paper_info(filename):
    # Detectar el número de paper (ej: _qp_12 o paper-11)
    paper_num = "1" 
    for i in range(1, 7):
        if f"_qp_{i}" in filename or f"paper-{i}" in filename:
            paper_num = str(i)
            break
    
    # Limpiar el nombre para el botón (March, June, Winter)
    fn_lower = filename.lower()
    display_name = ""
    
    if "june" in fn_lower or "_s" in fn_lower: display_name = "June"
    elif "_m" in fn_lower: display_name = "March"
    elif "_w" in fn_lower: display_name = "Winter"
    else: display_name = "Exam"

    # Detectar Variante (TZ) basada en los números del archivo
    if any(x in filename for x in ["11", "21", "31", "41", "51", "61"]): display_name += " TZ1"
    elif any(x in filename for x in ["12", "22", "32", "42", "52", "62"]): display_name += " TZ2"
    elif any(x in filename for x in ["13", "23", "33", "43", "53", "63"]): display_name += " TZ3"
    
    return paper_num, display_name

def build_yaml():
    base_path = "pastpapers"
    if not os.path.exists(base_path):
        print(f"❌ Error: No se encuentra la carpeta '{base_path}'")
        return

    # Obtener años de las carpetas (2022, 2023, 2024)
    years = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))], reverse=True)
    
    # Crear carpeta _data si no existe
    if not os.path.exists("_data"):
        os.makedirs("_data")

    with open("_data/exams.yml", "w", encoding="utf-8") as yml:
        for year in years:
            yml.write(f"- year: \"{year}\"\n")
            yml.write("  papers:\n")
            
            papers_dir = os.path.join(base_path, year, "Papers")
            if not os.path.exists(papers_dir): continue
            
            # Agrupar archivos por número de Paper
            grouped = {}
            for f in sorted(os.listdir(papers_dir)):
                if f.endswith(".pdf"):
                    p_num, v_name = get_paper_info(f)
                    if p_num not in grouped: grouped[p_num] = []
                    
                    # Generar nombre del Markscheme correspondiente
                    ms_file = f.replace("question-paper", "mark-scheme").replace("_qp_", "_ms_")
                    
                    grouped[p_num].append({
                        "name": v_name,
                        "file": f,
                        "ms": ms_file
                    })

            # Escribir en el formato YAML para el loop de Jekyll
            for p_num in sorted(grouped.keys()):
                subtitle = "(Core)" if p_num in ["1", "3", "5"] else "(Extended)"
                yml.write(f"    - id: \"p{p_num}-{year}\"\n")
                yml.write(f"      title: \"Paper {p_num}\"\n")
                yml.write(f"      subtitle: \"{subtitle}\"\n")
                yml.write("      variants:\n")
                for v in grouped[p_num]:
                    yml.write(f"        - name: \"{v['name']}\"\n")
                    yml.write(f"          file: \"{v['file']}\"\n")
                    yml.write(f"          ms: \"{v['ms']}\"\n")
    
    print("✅ ¡Archivo _data/exams.yml generado con éxito!")

if __name__ == "__main__":
    build_yaml()