import xml.etree.ElementTree as ET
import csv

# Entrada e saída
# ALTERE OS NOMES DOS ARQUIVOS CONFORME NECESSÁRIO
input_file = 'exemplo.osm'
output_file = 'exemplo.csv'

# Tags que indicam categorias válidas
VALID_CATEGORIES = ['amenity', 'shop', 'tourism', 'leisure', 'office', 'craft', 'healthcare','highway']

def extract_pois(osm_file, csv_file):
    tree = ET.parse(osm_file)
    root = tree.getroot()

    pois = []

    for node in root.findall('node'):
        lat = float(node.attrib['lat'])
        lon = float(node.attrib['lon'])
        tags = {tag.attrib['k']: tag.attrib['v'] for tag in node.findall('tag')}

        # Extrair nome se existir
        name = tags.get('name', '')

        if not name:
            continue

        # Identificar a categoria (primeira tag válida encontrada)
        category = None
        for cat in VALID_CATEGORIES:
            if cat in tags:
                category = tags[cat]
                break

        # Só inclui se tiver categoria
        if category:
            pois.append((name, category, lon, lat))

    # Salvar em CSV
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['name', 'category', 'lon', 'lat'])
        writer.writerows(pois)

    print(f"Total de POIs extraídos: {len(pois)}")
    print(f"Arquivo salvo em: {csv_file}")

if __name__ == '__main__':
    extract_pois(input_file, output_file)
