import sqlite3

DB_NAME = 'clinica.db'

def conector():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    return conn, cursor

def criar_tabelas(cursor):
    # Criar tabelas na ordem correta para respeitar chaves estrangeiras
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS especialidades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL UNIQUE
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        crm TEXT UNIQUE NOT NULL,
        especialidade_id INTEGER NOT NULL,
        telefone TEXT,
        email TEXT,
        FOREIGN KEY (especialidade_id) REFERENCES especialidades(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT UNIQUE NOT NULL,
        data_nascimento TEXT,
        telefone TEXT,
        email TEXT
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        medico_id INTEGER NOT NULL,
        paciente_id INTEGER NOT NULL,
        data_consulta TEXT NOT NULL,
        hora_consulta TEXT NOT NULL,
        descricao TEXT,
        status TEXT NOT NULL DEFAULT 'agendada',
        FOREIGN KEY (medico_id) REFERENCES medicos(id),
        FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
    )""")

def inserir_especialidades(cursor, especialidades):
    cursor.executemany("INSERT OR IGNORE INTO especialidades (nome) VALUES (?)", [(e,) for e in especialidades])

def inserir_medicos(cursor, medicos):
    cursor.executemany("""
    INSERT OR IGNORE INTO medicos (nome, crm, especialidade_id, telefone, email)
    VALUES (?, ?, ?, ?, ?)""", medicos)

def inserir_pacientes(cursor, pacientes):
    cursor.executemany("""
    INSERT OR IGNORE INTO pacientes (nome, cpf, data_nascimento, telefone, email)
    VALUES (?, ?, ?, ?, ?)""", pacientes)

def inserir_consultas(cursor, consultas):
    cursor.executemany("""
    INSERT OR IGNORE INTO consultas (medico_id, paciente_id, data_consulta, hora_consulta, descricao, status)
    VALUES (?, ?, ?, ?, ?, ?)""", consultas)

def mostrar_dados(cursor):
    print("\n" + "="*40)
    print("=== ESPECIALIDADES ===")
    cursor.execute("SELECT id, nome FROM especialidades ORDER BY nome")
    especialidades = cursor.fetchall()
    if especialidades:
        for esp in especialidades:
            print(f"ID: {esp[0]:<3} | Nome: {esp[1]}")
    else:
        print("Nenhuma especialidade cadastrada.")

    print("\n" + "="*40)
    print("=== MÉDICOS ===")
    cursor.execute("""
    SELECT m.id, m.nome, m.crm, e.nome, m.telefone, m.email
    FROM medicos m 
    JOIN especialidades e ON m.especialidade_id = e.id
    ORDER BY m.nome
    """)
    medicos = cursor.fetchall()
    if medicos:
        for m in medicos:
            print(f"ID: {m[0]:<3} | Nome: {m[1]:<20} | CRM: {m[2]:<10} | Especialidade: {m[3]:<15} | Tel: {m[4]:<14} | Email: {m[5]}")
    else:
        print("Nenhum médico cadastrado.")

    print("\n" + "="*40)
    print("=== PACIENTES ===")
    cursor.execute("SELECT id, nome, cpf, data_nascimento, telefone, email FROM pacientes ORDER BY nome")
    pacientes = cursor.fetchall()
    if pacientes:
        for p in pacientes:
            print(f"ID: {p[0]:<3} | Nome: {p[1]:<20} | CPF: {p[2]:<14} | Nasc: {p[3]:<10} | Tel: {p[4]:<14} | Email: {p[5]}")
    else:
        print("Nenhum paciente cadastrado.")

    print("\n" + "="*40)
    print("=== CONSULTAS ===")
    cursor.execute("""
    SELECT c.id, m.nome, p.nome, c.data_consulta, c.hora_consulta, c.descricao, c.status
    FROM consultas c
    JOIN medicos m ON c.medico_id = m.id
    JOIN pacientes p ON c.paciente_id = p.id
    ORDER BY c.data_consulta, c.hora_consulta
    """)
    consultas = cursor.fetchall()
    if consultas:
        for c in consultas:
            print(f"ID: {c[0]:<3} | Médico: {c[1]:<20} | Paciente: {c[2]:<20} | Data: {c[3]} | Hora: {c[4]} | Status: {c[6]} | Descrição: {c[5]}")
    else:
        print("Nenhuma consulta cadastrada.")
    print("="*40)

def main():
    conn, cursor = conector()
    criar_tabelas(cursor)

    especialidades = ['Cardiologia', 'Dermatologia', 'Pediatria', 'Ginecologia']
    inserir_especialidades(cursor, especialidades)
    conn.commit()

    # Obter IDs das especialidades para usar no cadastro de médicos
    cursor.execute("SELECT id, nome FROM especialidades")
    esp_dict = {nome: id_ for id_, nome in cursor.fetchall()}

    medicos = [
        ('Dr. João Silva', 'CRM12345', esp_dict['Cardiologia'], '(11)99999-1111', 'joao.silva@clinica.com'),
        ('Dra. Ana Souza', 'CRM54321', esp_dict['Dermatologia'], '(11)98888-2222', 'ana.souza@clinica.com')
    ]
    inserir_medicos(cursor, medicos)
    conn.commit()

    pacientes = [
        ('Carlos Alberto', '123.456.789-00', '1980-05-20', '(11)97777-3333', 'carlos.a@email.com'),
        ('Maria Clara', '987.654.321-11', '1995-10-10', '(21)96666-4444', 'maria.c@email.com')
    ]
    inserir_pacientes(cursor, pacientes)
    conn.commit()

    # Pegando ids para consultas
    cursor.execute("SELECT id FROM medicos WHERE nome='Dr. João Silva'")
    medico_id = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM pacientes WHERE nome='Carlos Alberto'")
    paciente_id = cursor.fetchone()[0]

    consultas = [
        (medico_id, paciente_id, '2025-11-01', '14:30', 'Consulta de rotina', 'agendada')
    ]
    inserir_consultas(cursor, consultas)
    conn.commit()

    mostrar_dados(cursor)
    conn.close()

if __name__ == '__main__':
    main()
