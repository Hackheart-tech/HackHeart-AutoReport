
from datetime import datetime

sections = [
    {"icon": "🕵️‍♂️", "title": "Exploration"},
    {"icon": "🔍", "title": "Reconnaissance"},
    {"icon": "📦", "title": "Découverte"},
    {"icon": "💣", "title": "Exploitation"},
    {"icon": "🧠", "title": "Élévation de privilèges"},
    {"icon": "🎯", "title": "Preuve / Loot"},
]

report_data = {}

print("=== Générateur de Rapport Pentest HackHeart ===")
report_data['target_ip'] = input("IP de la cible : ")
report_data['report_name'] = input("Nom du rapport (ex: report-fuelcms) : ")

for section in sections:
    entries = []
    print(f"\n{section['icon']} {section['title']}")

    while True:
        entry = input("➤ Ajoute une entrée (laisser vide pour finir cette section) : ")
        if not entry.strip():
            break
        files = []
        while True:
            add_file = input("  📁 Veux-tu ajouter un fichier à cette entrée ? (o/n) : ").lower()
            if add_file == 'o':
                file_path = input("  📎 Chemin du fichier à inclure (nom, screenshot, etc) : ")
                files.append(file_path)
            else:
                break
        entries.append({"text": entry, "files": files})
    
    report_data[section['title']] = entries

# Génération du contenu Markdown
md_lines = [
    f"# Rapport de Pentest — {report_data['report_name']}",
    f"**Cible :** {report_data['target_ip']}",
    f"**Date :** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
    "---"
]

for section in sections:
    title = section["title"]
    icon = section["icon"]
    md_lines.append(f"\n## {icon} {title}\n")
    for entry in report_data.get(title, []):
        md_lines.append(f"- {entry['text']}")
        for file in entry['files']:
            md_lines.append(f"  - 📎 *Fichier lié :* `{file}`")

# Sauvegarde en fichier
filename = f"{report_data['report_name']}.md"
with open(filename, "w") as f:
    f.write("\n".join(md_lines))

print(f"\n✅ Rapport généré : {filename}")
