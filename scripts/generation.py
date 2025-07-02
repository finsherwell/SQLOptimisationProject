from faker import Faker
import csv
import random
from datetime import datetime

fake = Faker()

# Config
NUM_DEPARTMENTS = 250
NUM_ROLES = 100
NUM_BRANCHES = 100
NUM_EMPLOYEES = 200_000
NUM_CLIENTS = 25_000
NUM_BRANCH_MANAGERS = 2_000
NUM_WORKS_WITH = 100_000
NUM_BRANCH_SUPPLIERS = 2_000
CHUNK_SIZE = 10_000  # for employees only

def write_csv(filename, header, rows):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

# 1. Departments
departments = [
    [
        i,
        fake.bs().title()[:50],
        random.randint(5, 500),
        random.randint(100, 1000),
        fake.date_time_this_decade(),
        fake.date_time_this_year()
    ]
    for i in range(1, NUM_DEPARTMENTS + 1)
]
write_csv("department.csv",
          ["department_id", "department_name", "staff_no", "staff_no_quota", "created_at", "updated_at"],
          departments)

# 2. Company Roles
roles = []
role_names = set()
for i in range(1, NUM_ROLES + 1):
    # Ensure unique role names
    role_name = fake.job()
    while role_name in role_names:
        role_name = fake.job()
    role_names.add(role_name)
    roles.append([i, role_name[:50], fake.date_time_this_decade(), fake.date_time_this_year()])
write_csv("company_roles.csv",
          ["role_id", "role_name", "created_at", "updated_at"],
          roles)

# 3. Branches
branches = [
    [i, fake.city()[:50], fake.date_time_this_decade(), fake.date_time_this_year()]
    for i in range(1, NUM_BRANCHES + 1)
]
write_csv("branch.csv",
          ["branch_id", "branch_name", "created_at", "updated_at"],
          branches)

# 4. Employees (in chunks)
with open("employee.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "employee_id", "first_name", "last_name", "birth_date", "sex",
        "salary", "department_id", "role_id", "branch_id",
        "created_at", "updated_at", "is_deleted"
    ])

for start_id in range(1, NUM_EMPLOYEES + 1, CHUNK_SIZE):
    end_id = min(start_id + CHUNK_SIZE - 1, NUM_EMPLOYEES)
    rows = []
    for i in range(start_id, end_id + 1):
        sex_choice = random.choice(['m', 'f', 'nb', 'undefined'])
        rows.append([
            i,
            fake.first_name(),
            fake.last_name(),
            fake.date_of_birth(minimum_age=20, maximum_age=65),
            sex_choice,
            random.randint(30000, 200000),
            random.randint(1, NUM_DEPARTMENTS),
            random.randint(1, NUM_ROLES),
            random.randint(1, NUM_BRANCHES),
            fake.date_time_this_decade(),
            fake.date_time_this_year(),
            random.choice([False, False, False, True])  # 25% soft deleted
        ])
    with open("employee.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print(f"Generated employees {start_id}-{end_id}")

# 5. Clients
clients = [
    [
        i,
        fake.company()[:50],
        random.randint(1, NUM_BRANCHES),
        fake.date_time_this_decade(),
        fake.date_time_this_year(),
        random.choice([False, False, False, True])
    ]
    for i in range(1, NUM_CLIENTS + 1)
]
write_csv("client.csv",
          ["client_id", "client_name", "branch_id", "created_at", "updated_at", "is_deleted"],
          clients)

# 6. Branch Managers
branch_managers = []
for _ in range(NUM_BRANCH_MANAGERS):
    branch_id = random.randint(1, NUM_BRANCHES)
    employee_id = random.randint(1, NUM_EMPLOYEES)
    start_date = fake.date_between(start_date='-5y', end_date='-1y')
    end_date = fake.date_between(start_date=start_date, end_date='today')
    created_at = fake.date_time_this_decade()
    updated_at = fake.date_time_this_year()
    branch_managers.append([
        branch_id, employee_id, start_date, end_date, created_at, updated_at
    ])
write_csv("branch_manager.csv",
          ["branch_id", "employee_id", "start_date", "end_date", "created_at", "updated_at"],
          branch_managers)

# 7. Works With
works_with = []
existing_pairs = set()
for _ in range(NUM_WORKS_WITH):
    employee_id = random.randint(1, NUM_EMPLOYEES)
    client_id = random.randint(1, NUM_CLIENTS)
    # Avoid duplicates for PK (employee_id, client_id)
    while (employee_id, client_id) in existing_pairs:
        employee_id = random.randint(1, NUM_EMPLOYEES)
        client_id = random.randint(1, NUM_CLIENTS)
    existing_pairs.add((employee_id, client_id))
    total_sales = random.randint(0, 100000)
    created_at = fake.date_time_this_decade()
    updated_at = fake.date_time_this_year()
    works_with.append([
        employee_id, client_id, total_sales, created_at, updated_at
    ])
write_csv("works_with.csv",
          ["employee_id", "client_id", "total_sales", "created_at", "updated_at"],
          works_with)

# 8. Branch Suppliers
branch_supplier = []
existing_supplier_pairs = set()
supplier_types = ["Technology", "Catering", "HR", "Logistics", "Cleaning", "Maintenance"]
for _ in range(NUM_BRANCH_SUPPLIERS):
    branch_id = random.randint(1, NUM_BRANCHES)
    supplier_name = fake.company()[:50]
    while (branch_id, supplier_name) in existing_supplier_pairs:
        supplier_name = fake.company()[:50]
    existing_supplier_pairs.add((branch_id, supplier_name))
    supplier_type = random.choice(supplier_types)
    created_at = fake.date_time_this_decade()
    updated_at = fake.date_time_this_year()
    branch_supplier.append([
        branch_id, supplier_name, supplier_type, created_at, updated_at
    ])
write_csv("branch_supplier.csv",
          ["branch_id", "supplier_name", "supplier_type", "created_at", "updated_at"],
          branch_supplier)

print("All CSV files generated successfully.")
