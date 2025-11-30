n = int(input())
polyhedrons = []

for i in range(n):
    polyhedrons.append(input())

nana = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}   
result = 0
for kaka in polyhedrons:
    result+= nana[kaka]
print(result)
