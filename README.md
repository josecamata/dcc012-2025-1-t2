
# 🧾 Trabalho Prático
## Comparação entre k-d Tree e Quadtree para Consulta Espacial de Pontos de Interesse

### 🎯 Objetivo Geral

Desenvolver uma aplicação em **C++** que implemente e compare duas estruturas de dados espaciais — **k-d tree** e **quadtree** — para indexação e realização de consultas eficientes sobre **pontos de interesse (POIs)** extraídos de dados reais do **OpenStreetMap (OSM)**.

---

### 📂 Descrição do Problema

Sua tarefa é construir um sistema capaz de:

1. Ler dados de pontos de interesse (latitude, longitude e nome) a partir de um arquivo `.osm`;
2. Implementar duas estruturas de dados espaciais:
   - `k-d tree` (com divisão alternada por eixos);
   - `quadtree` (com divisão recursiva do plano em quatro quadrantes);
3. Inserir todos os pontos em **ambas** as estruturas;
4. Permitir ao usuário realizar:
   - **Consulta por região** (*range query*);
   - **Busca por vizinho mais próximo** (*nearest neighbor*);
5. Comparar o desempenho (tempo de execução e número de comparações) das duas estruturas nas mesmas consultas.

---

### Implementação

- Linguagem: **C++**;
- Ambas as estruturas devem ser **implementadas do zero**;
- O código deve conter (pelo menos):
  - Classe `Point` com: `x`, `y`, `nome`, `categoria`;
  - Classes `KDTree` e `QuadTree` com os métodos:
    - `void insert(Point p)`
    - `std::vector<Point> rangeQuery(double xmin, double ymin, double xmax, double ymax)`
    - `Point nearestNeighbor(double x, double y)`
    - `Point nearestNeighbor(double x, double y, std::string categoria)`

### Entrada e Saída

- **Entrada**: dados extraídos do arquivo `.osm`, convertidos para `.csv`;
- **Saída**: resultados das consultas e comparações entre as estruturas.

---

### Compilação e Execução



