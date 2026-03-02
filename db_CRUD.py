import pymysql

DB_CONFIG = {
    'host':'localhost',
    'port':3306,
    'user':'root',
    'password':'Silvija321!',
    'database':'jobs_db'
}

headers = ['id','position','salary','location','required skills']

def get_conn():
    return pymysql.connect(**DB_CONFIG)

def load_jobs():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from jobs")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    jobs = []
    for row in rows:
        single_job = {}
        for col_num in range(len(headers)):
            single_job[headers[col_num]] = row[col_num]
        jobs.append(single_job)
    return jobs

def print_info():
    print("------------------------------")
    print("1. Atvaizduoti darbo skelbimus.")
    print("2. Įtraukti darbo skelbimą.")
    print("3. Redaguoti darbo skelbimą.")
    print("4. Trinti darbo skelbimą.")
    print("5. Išeiti iš programos.")
    print("------------------------------")

def print_jobs(jobs):
    jobs = load_jobs()
    print("Atvaizduoju darbo skelbimus:")
    for job in jobs:
        print(
            f"{job["id"]}. Pozicija: {job["position"]} | Darbo užmokestis: €{float(job["salary"]):.2f} | Lokacija: {job["location"]} | Įgūdžiai: {job["required skills"]}")

def create_job(jobs,id_counter):
    print("Įveskite naujos pozicijos pavadinimą:")
    position = input()
    print("Įveskite darbo užmokesčio dydį:")
    salary = float(input())
    print("Įveskite lokaciją:")
    location = input()
    print("Įveskite įgūdžius:")
    required_skills = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO `jobs_db`.`jobs`(`position`,`salary`,`location`,`required_skills`) VALUES (%s,%s,%s,%s);",(position, salary, location, required_skills))
    conn.commit()
    cur.close()
    conn.close()

def edit_job(jobs):
    print("Įrašykite darbo skelbimo id, kurį norite redaguoti:")
    edit_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from jobs where id = %s", (edit_id,))
    row = cur.fetchone()
    if row:
        print("Įveskite pozicijos pavadinimą:")
        position = input()
        print("Įveskite darbo užmokesčio dydį:")
        salary = float(input())
        print("Įveskite lokaciją:")
        location = input()
        print("Įveskite įgūdžius:")
        required_skills = input()
        cur.execute("UPDATE `jobs_db`.`jobs` SET `position` = %s, `salary` = %s, `location` = %s, `required_skills` = %s WHERE `id` = %s;",
                    (position, salary, location, required_skills, edit_id))
        conn.commit()
        print("Darbo skelbimas sėkmingai atnaujintas")
    else:
        print("Toks id neegzistuoja")
    cur.close()
    conn.close()

def delete_job(jobs):
    print("Įrašykite darbo skelbimo id, kurį norite trinti:")
    del_id = input()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from jobs where id = %s", (del_id,))
    row = cur.fetchone()
    if row:
        print(f"{row[0]}. Pozicija: {row[1]} | Darbo užmokestis: €{float(row[2]):.2f} | Lokacija: {row[3]} | Įgūdžiai: {row[4]}")
        print("Darbo skelbimas sėkmingai ištrintas")
        cur.execute("delete from jobs where id = %s", (del_id,))
        conn.commit()
    else:
        print("Toks id neegzistuoja")
    cur.close()
    conn.close()