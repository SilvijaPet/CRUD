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
            f"{job["id"]}. Pozicija: {job["position"]} | Darbo užmokestis: €{job["salary"]:.2f} | Lokacija: {job["location"]} | Įgūdžiai: {job["required skills"]}")

def delete_job(jobs):
    print("Įrašykite darbo skelbimo id, kurį norite trinti:")
    del_id = int(input())
    for job in jobs:
        if job["id"] == del_id:
            jobs.remove(job)
            print("Darbo skelbimas sėkmingai ištrintas")
            return
    else:
        print("Toks id neegzistuoja")

def edit_job(jobs):
    print("Įrašykite darbo skelbimo id, kurį norite redaguoti:")
    edit_id = int(input())
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
            return
    else:
        print("Toks id neegzistuoja")

def create_job(jobs,id_counter):
    print("Įveskite naujos pozicijos pavadinimą:")
    position = input()
    print("Įveskite darbo užmokesčio dydį:")
    salary = float(input())
    print("Įveskite lokaciją:")
    location = input()
    print("Įveskite įgūdžius:")
    required_skills = input()
    id_counter += 1
    job = {
        "id": id_counter,
        "position": position,
        "salary": salary,
        "location": location,
        "required skills": required_skills
    }
    jobs.append(job)
    return id_counter