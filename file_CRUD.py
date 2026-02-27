import csv

headers = ['id','position','salary','location','required skills']
def load_jobs():
    with open("./jobs.csv", mode ="r", encoding="utf-8") as file:
        return list(csv.DictReader(file))

def save_jobs(jobs):
    with open("./jobs.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(jobs)

def print_info():
    print("------------------------------")
    print("1. Atvaizduoti darbo skelbimus.")
    print("2. Įtraukti darbo skelbimą.")
    print("3. Redaguoti darbo skelbimą.")
    print("4. Trinti darbo skelbimą.")
    print("5. Išeiti iš programos.")
    print("------------------------------")

def print_jobs(jobs):
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
    id_counter = int(jobs[-1]['id']) + 1 if len(jobs) > 0 else 1
    job = {
        "id": id_counter,
        "position": position,
        "salary": salary,
        "location": location,
        "required skills": required_skills
    }
    jobs.append(job)
    save_jobs(jobs)
    return id_counter

def edit_job(jobs):
    print("Įrašykite darbo skelbimo id, kurį norite redaguoti:")
    edit_id = input()
    for job in jobs:
        if job["id"] == edit_id:
            print("Įveskite pozicijos pavadinimą:")
            job["position"] = input()
            print("Įveskite darbo užmokesčio dydį:")
            job["salary"] = float(input())
            print("Įveskite lokaciją:")
            job["location"] = input()
            print("Įveskite įgūdžius:")
            job["required skills"] = input()
            save_jobs(jobs)
            return
    else:
        print("Toks id neegzistuoja")

def delete_job(jobs):
    print("Įrašykite darbo skelbimo id, kurį norite trinti:")
    del_id = input()
    for job in jobs:
        if job["id"] == del_id:
            jobs.remove(job)
            print("Darbo skelbimas sėkmingai ištrintas")
            save_jobs(jobs)
            return
    else:
        print("Toks id neegzistuoja")
