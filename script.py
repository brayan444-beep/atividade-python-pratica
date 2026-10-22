# Lista de alunos com suas respectivas notas
alunos_e_notas = {
    "Ana": 8.5,
    "Carlos": 4.5,
    "Beatriz": 7.0,
    "Daniel": 5.5,
    "Eduarda": 9.0
}

print("--- FILTRAGEM DE NOTAS DE ALUNOS ---")
print("Alunos Aprovados (Nota maior ou igual a 7.0):")

# Filtrando os alunos aprovados
for aluno, nota in alunos_e_notas.items():
    if nota >= 7.0:
        print(f" - {aluno}: Nota {nota}")

print("\nAlunos em Recuperação (Nota menor que 7.0):")
# Filtrando os alunos em recuperação
for aluno, nota in alunos_e_notas.items():
    if nota < 7.0:
        print(f" - {aluno}: Nota {nota}")
