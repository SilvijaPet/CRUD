from data import load_jobs
from list_CRUD import *

jobs = load_jobs()
id_counter = 3

while True:
    print_info()
    option = input()
    match option:
        case "1":
            print_jobs(jobs)
        case "2":
            id_counter = create_job(jobs,id_counter)
        case "3":
            edit_job(jobs)
        case "4":
            delete_job(jobs)
        case "5":
            print("Išėjote iš programos")
            break
        case _:
            print("Negalimas pasirinkimas, bandykite iš naujo")