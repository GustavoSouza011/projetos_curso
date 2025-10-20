import sqlite3

DB_NAME = 'bancobiblioteca.db'

def conector():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    return conn, cursor

def criar_tabelas(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS autores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE,
        nacionalidade TEXT NOT NULL,
        data_nascimento TEXT NOT NULL,
        data_falecimento TEXT,
        biografia TEXT,
        premios TEXT,
        obras_principais TEXT,
        foto TEXT,
        influencias TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor_id INTEGER NOT NULL,
        editora TEXT,
        ano_publicacao INTEGER,
        genero TEXT,
        isbn TEXT UNIQUE,
        paginas INTEGER,
        idioma TEXT,
        FOREIGN KEY (autor_id) REFERENCES autores(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        matricula TEXT UNIQUE NOT NULL,
        curso TEXT,
        email TEXT,
        telefone TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER NOT NULL,
        aluno_id INTEGER NOT NULL,
        data_emprestimo TEXT NOT NULL,
        data_devolucao TEXT,
        status TEXT NOT NULL DEFAULT 'emprestado',
        FOREIGN KEY (livro_id) REFERENCES livros(id),
        FOREIGN KEY (aluno_id) REFERENCES alunos(id)
    )""")

def inserir_autores(cursor, autores):
    cursor.executemany("""
    INSERT OR IGNORE INTO autores 
    (nome, nacionalidade, data_nascimento, data_falecimento, premios, obras_principais, foto, influencias)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", autores)

def inserir_livros(cursor, livros):
    cursor.executemany("""
    INSERT OR IGNORE INTO livros
    (titulo, autor_id, editora, ano_publicacao, genero, isbn, paginas, idioma)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", livros)

def inserir_alunos(cursor, alunos):
    cursor.executemany("""
    INSERT OR IGNORE INTO alunos
    (nome, matricula, curso, email, telefone)
    VALUES (?, ?, ?, ?, ?)""", alunos)

def inserir_emprestimos(cursor, emprestimos):
    cursor.executemany("""
    INSERT OR IGNORE INTO emprestimos
    (livro_id, aluno_id, data_emprestimo, data_devolucao, status)
    VALUES (?, ?, ?, ?, ?)""", emprestimos)

def buscar_autores(cursor):
    cursor.execute("SELECT * FROM autores ORDER BY nome")
    return cursor.fetchall()

def buscar_livros(cursor):
    cursor.execute("""
    SELECT livros.id, livros.titulo, autores.nome, livros.editora, livros.ano_publicacao, livros.genero, livros.isbn, livros.paginas, livros.idioma
    FROM livros
    JOIN autores ON livros.autor_id = autores.id
    ORDER BY livros.titulo
    """)
    return cursor.fetchall()

def buscar_alunos(cursor):
    cursor.execute("SELECT * FROM alunos ORDER BY nome")
    return cursor.fetchall()

def buscar_emprestimos(cursor):
    cursor.execute("""
    SELECT emprestimos.id, livros.titulo, alunos.nome, emprestimos.data_emprestimo, emprestimos.data_devolucao, emprestimos.status
    FROM emprestimos
    JOIN livros ON emprestimos.livro_id = livros.id
    JOIN alunos ON emprestimos.aluno_id = alunos.id
    ORDER BY emprestimos.data_emprestimo DESC
    """)
    return cursor.fetchall()

def mostrar_autores(autores):
    print("\n===== AUTORES =====")
    if not autores:
        print("Nenhum autor cadastrado.")
        return
    for autor in autores:
        id_, nome, nacionalidade, nascimento, falecimento, biografia, premios, obras, foto, influencias = autor
        print(f"\nID: {id_}")
        print(f"Nome           : {nome}")
        print(f"Nacionalidade  : {nacionalidade}")
        print(f"Nascimento     : {nascimento}")
        print(f"Falecimento    : {falecimento if falecimento else '—'}")
        print(f"Prêmios        : {premios if premios else '—'}")
        print(f"Obras Principais: {obras if obras else '—'}")
        print(f"Influências    : {influencias if influencias else '—'}")
        print("-" * 40)

def mostrar_livros(livros):
    print("\n===== LIVROS =====")
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    for livro in livros:
        (id_, titulo, autor, editora, ano, genero, isbn, paginas, idioma) = livro
        print(f"\nID: {id_}")
        print(f"Título        : {titulo}")
        print(f"Autor         : {autor}")
        print(f"Editora       : {editora if editora else '—'}")
        print(f"Ano Publicação: {ano if ano else '—'}")
        print(f"Gênero        : {genero if genero else '—'}")
        print(f"ISBN          : {isbn if isbn else '—'}")
        print(f"Páginas       : {paginas if paginas else '—'}")
        print(f"Idioma        : {idioma if idioma else '—'}")
        print("-" * 40)

def mostrar_alunos(alunos):
    print("\n===== ALUNOS =====")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        id_, nome, matricula, curso, email, telefone = aluno
        print(f"\nID: {id_}")
        print(f"Nome      : {nome}")
        print(f"Matrícula : {matricula}")
        print(f"Curso     : {curso if curso else '—'}")
        print(f"E-mail    : {email if email else '—'}")
        print(f"Telefone  : {telefone if telefone else '—'}")
        print("-" * 40)

def mostrar_emprestimos(emprestimos):
    print("\n===== EMPRÉSTIMOS =====")
    if not emprestimos:
        print("Nenhum empréstimo registrado.")
        return
    for emp in emprestimos:
        id_, titulo, aluno, data_emp, data_dev, status = emp
        print(f"\nID Empréstimo: {id_}")
        print(f"Livro        : {titulo}")
        print(f"Aluno        : {aluno}")
        print(f"Data Empréstimo: {data_emp}")
        print(f"Data Devolução : {data_dev if data_dev else '—'}")
        print(f"Status       : {status}")
        print("-" * 40)

def menu():
    print("\n=== BIBLIOTECA ===")
    print("1 - Mostrar Autores")
    print("2 - Mostrar Livros")
    print("3 - Mostrar Alunos")
    print("4 - Mostrar Empréstimos")
    print("0 - Sair")

def main():
    conn, cursor = conector()
    criar_tabelas(cursor)

    # Dados iniciais para popular banco
    autores = [
        ('Machado de Assis', 'Brasileiro', '21/06/1839', '29/09/1908',
         'Prêmio Machado de Assis (1908)', 'Dom Casmurro, Memórias Póstumas de Brás Cubas, Quincas Borba',
         'https://imgs.search.brave.com/lyk61jMSsqYDgI2TwgampAnFETT378P-hhFsNH3lhqc/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly9zdGF0/aWMucG9ydHVndWVz/LmNvbS5ici9jb250/ZXVkby9pbWFnZXMv/bWFjaGFkby1hc3Np/cy10cmFuc2l0b3Ut/Y29tLW1hZXN0cmlh/LXBvci1kaXZlcnNv/cy1nZW5lcm9zLWxp/dGVyYXJpb3MtZW50/cmUtZWxlcy1wb2Vz/aWEtNWM5YTBjNGU1/NzUzYi5qcGc',
         'Fiódor Dostoiévski, Eça de Queirós'),
        ('Clarice Lispector', 'Brasileira', '10/12/1920', '09/12/1977',
         'Prêmio Jabuti (1977)', 'A Hora da Estrela, Perto do Coração Selvagem',
         'https://imgs.search.brave.com/HaqAVryzVyHM35Mg1C5qVEnwvAl9YfJfE3DvzPvk9QY/rs:fit:500:0:1:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy9h/L2E3LygxOTIwLTE5/NzcpX0NsYXJpY2Vf/TGlzcGVjdG9yXzZ6/eGtwX3BsZWFzZV9j/cmVkaXQocGFsZXR0/ZS5mbSkucG5n',
         'Virginia Woolf, Simone de Beauvoir'),
    ]
    inserir_autores(cursor, autores)
    conn.commit()

    # Pegar ids dos autores inseridos
    cursor.execute("SELECT id, nome FROM autores")
    autores_db = cursor.fetchall()
    autor_id_machado = next((id_ for id_, nome in autores_db if nome == 'Machado de Assis'), None)
    autor_id_clarice = next((id_ for id_, nome in autores_db if nome == 'Clarice Lispector'), None)

    livros = []
    if autor_id_machado and autor_id_clarice:
        livros = [
            ('Dom Casmurro', autor_id_machado, 'Editora XYZ', 1899, 'Romance', '978-3-16-148410-0', 256, 'Português'),
            ('A Hora da Estrela', autor_id_clarice, 'Editora ABC', 1977, 'Romance', '978-1-23-456789-7', 128, 'Português')
        ]
    inserir_livros(cursor, livros)
    conn.commit()

    alunos = [
        ('João Silva', '2021001', 'Engenharia', 'joao.silva@email.com', '(11) 99999-8888'),
        ('Maria Souza', '2021002', 'Literatura', 'maria.souza@email.com', '(21) 98888-7777')
    ]
    inserir_alunos(cursor, alunos)
    conn.commit()

    # Pegar ids para empréstimos
    cursor.execute("SELECT id FROM livros WHERE titulo='Dom Casmurro'")
    livro_casmurro_id = cursor.fetchone()
    cursor.execute("SELECT id FROM alunos WHERE nome='João Silva'")
    aluno_joao_id = cursor.fetchone()

    if livro_casmurro_id and aluno_joao_id:
        emprestimos = [
            (livro_casmurro_id[0], aluno_joao_id[0], '2025-10-01', None, 'emprestado'),
        ]
        inserir_emprestimos(cursor, emprestimos)
        conn.commit()

    while True:
        menu()
        escolha = input("Escolha uma opção: ").strip()
        if escolha == '1':
            mostrar_autores(buscar_autores(cursor))
        elif escolha == '2':
            mostrar_livros(buscar_livros(cursor))
        elif escolha == '3':
            mostrar_alunos(buscar_alunos(cursor))
        elif escolha == '4':
            mostrar_emprestimos(buscar_emprestimos(cursor))
        elif escolha == '0':
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

    conn.close()

if __name__ == '__main__':
    main()
