# =====================================================================
# ESCOLA DO FUTURO DE GOIÁS (EFG) - SISTEMA INTEGRADO
# Aula 04 - Herança de Classes e Relacionamentos de Agregação
# =====================================================================

# 1. SUPERCLASSE (Classe Pai): Reúne atributos comuns a qualquer pessoa no sistema
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    # Método comum herdado por todos
    def exibir_dados(self):
        print(f"👤 Usuário: {self.nome} | E-mail: {self.email}")


# 2. SUBCLASSE (Classe Filho): Herda tudo de Usuario e adiciona especificidades
class Aluno(Usuario):
    def __init__(self, nome, email, matricula):
        # A chamada super() ativa o construtor do pai e inicializa nome e email
        super().__init__(nome, email)
        self.matricula = matricula    # Atributo exclusivo de Aluno
        self.__notas = []              # Atributo privado encapsulado

    def lancar_nota(self, nota):
        if 0.0 <= nota <= 10.0:
            self.__notas.append(nota)
        else:
            print(f"❌ [ERRO]: Nota {nota} inválida para {self.nome}!")

    # SOBRESCRITA DE MÉTODO (Method Overriding)
    # Customizamos o exibir_dados() herdado do pai para adicionar dados do Aluno
    def exibir_dados(self):
        print(f"🎓 [ESTUDANTE] Nome: {self.nome} | Matrícula: {self.matricula} | Notas: {self.__notas}")


# 3. CLASSE CONTÊINER: Representa a Agregação ("Tem alunos")
class Curso:
    def __init__(self, nome_curso):
        self.nome_curso = nome_curso
        self.estudantes_matriculados = []  # Lista que receberá instâncias de Aluno

    # Método que implementa o relacionamento de Agregação
    def me_matricular_estudante(self, aluno_objeto):
        # O curso recebe um objeto Aluno de fora e o guarda na sua lista interna
        self.estudantes_matriculados.append(aluno_objeto)
        print(f"📌 [MATRÍCULA]: {aluno_objeto.nome} inserido na turma de {self.nome_curso}!")

    def exibir_diario_classe(self):
        print("\n" + "=" * 50)
        print(f"📖 DIÁRIO DE CLASSE: {self.nome_curso}")
        print("=" * 50)
        if not self.estudantes_matriculados:
            print("Nenhum aluno matriculado neste curso.")
        for aluno in self.estudantes_matriculados:
            # Polimorfismo e chamada do método sobrescrito do aluno
            aluno.exibir_dados()
        print("=" * 50 + "\n")


# =====================================================================
# ÁREA DE EXECUÇÃO (Teste no Laboratório)
# =====================================================================
if __name__ == "__main__":
    print("--- SISTEMA INTEGRADO EFG: MÓDULO DE MATRÍCULAS ---")

    # Instanciando Alunos (Criando objetos filhos)
    estudante_1 = Aluno("Guilherme Silva", "gui@efg.com", "EFG-2026-101")
    estudante_2 = Aluno("Beatriz Souza", "bea@efg.com", "EFG-2026-102")

    # Lançando notas parciais
    estudante_1.lancar_nota(9.5)
    estudante_2.lancar_nota(8.8)

    # Instanciando o Curso (O contêiner de Agregação)
    curso_dev = Curso("Técnico em Desenvolvimento Web II")

    # Realizando a Agregação na prática (Matriculando os objetos aluno no curso)
    curso_dev.me_matricular_estudante(estudante_1)
    curso_dev.me_matricular_estudante(estudante_2)

    # Exibindo o diário de classe do curso
    curso_dev.exibir_diario_classe()
