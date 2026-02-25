jobs = [
    {"id":1,
     "position":"Duomenų analitikas",
     "salary":1850,
     "location": "Vilnius",
     "required skills":"SQL,Python,PowerBI,Windows,Excel" },
    {"id":2,
     "position":"Apskaitininkas",
     "salary":1300,
     "location":"remote",
     "required skills":"accounting principles, G/L accounts, payroll, taxes, reconciliation"},
    {"id": 3,
     "position":"Marketingo specialistas",
     "salary": 1450,
     "location": "Kaunas",
     "required skills":"Canva, Google Ads, KPIs, social media planning"}
]
id_counter = 3

while True:
    print("------------------------------")
    print("1. Atvaizduoti darbo skelbimus.")
    print("2. Įtraukti darbo skelbimą.")
    print("3. Redaguoti darbo skelbimą.")
    print("4. Trinti darbo skelbimą.")
    print("5. Išeiti iš programos.")
    print("------------------------------")
    option = input()
    match option:
        case "1":
            print("Atvaizduoju darbo skelbimus")
            for job in jobs:
                print(f"{job["id"]}. Pozicija: {job["position"]} | Darbo užmokestis: €{job["salary"]:.2f} | Lokacija: {job["location"]} | Įgūdžiai: {job["required skills"]}")
        case "2":
            print("Įtraukiu darbo skelbimą")
            print("Įveskite pozicijos pavadinimą:")
            position = input()
            print("Įveskite darbo užmokesčio dydį:")
            salary = float(input())
            print("Įveskite lokaciją:")
            location = input()
            print("Įveskite įgūdžius:")
            required_skills = input()
            job = {
                "id": id_counter,
                "position": position,
                "salary": salary,
                "location": location,
                "required skills": required_skills
            }
            jobs.append(job)
        case "3":
            print("Redaguoju darbo skelbimą")
            print("'Įrašykite id darbo skelbimo, kurį norite redaguoti:")
            edit_id = int(input())
            for job in jobs:
                if job["id"] == edit_id:
                    print("Įveskite pozicijos pavadinimą:")
                    job["position"] = input()
                    print("Įveskite darbo užmokesčio dydį:")
                    job["salary"] = int(input())
                    print("Įveskite lokaciją:")
                    job["location"] = input()
                    print("Įveskite įgūdžius:")
                    job["required skills"] = input()
        case "4":
            print("Trinu darbo skelbimą")
            print("'Įrašykite id darbo skelbimo, kurį norite trinti:")
            del_id = int(input())
            for job in jobs:
                if job["id"] == del_id:
                    jobs.remove(job)
                    print("Darbo skelbimas sėkmingai ištrintas")
                    break
        case "5":
            print("Išėjote iš programos")
            break
        case _:
            print("Negalimas pasirinkimas, bandykite iš naujo")
