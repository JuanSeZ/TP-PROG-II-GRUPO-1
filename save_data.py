def save():
    # Guarda registros de ciudadanos
    with open('registered_citizen.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        with open("registered_citizen.csv", "a") as a:
            writer = csv.writer(a)
            for citizen in Citizen_record.citizen_list:
                for row in reader:
                    for col in row:
                        if col == str(citizen.cuil):
                            return
                writer.writerow([citizen.cuil, citizen.cellphone, citizen.password])


