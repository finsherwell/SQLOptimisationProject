-- departments of the company
create table department (
	department_id int primary key,
	department_name varchar(50),
	staff_no int check (staff_no >= 0),
	staff_no_quota int check (staff_no_quota >= 0),
	created_at timestamp default current_timestamp,
	updated_at timestamp default current_timestamp
);

comment on table department is 'departments of the company';
comment on column department.department_id is 'unique id for the department';
comment on column department.department_name is 'name of the department';
comment on column department.staff_no is 'current number of staff';
comment on column department.staff_no_quota is 'maximum allowed staff';
comment on column department.created_at is 'record creation timestamp';
comment on column department.updated_at is 'record update timestamp';


-- roles in the company
create table company_roles (
	role_id int primary key,
	role_name varchar(50) unique,
	created_at timestamp default current_timestamp,
	updated_at timestamp default current_timestamp
);

comment on table company_roles is 'roles in the company';
comment on column company_roles.role_id is 'unique id for the role';
comment on column company_roles.role_name is 'unique role name (e.g., engineer, manager)';
comment on column company_roles.created_at is 'record creation timestamp';
comment on column company_roles.updated_at is 'record update timestamp';


-- company branch locations
create table branch (
	branch_id int primary key,
	branch_name varchar(50),
	created_at timestamp default current_timestamp,
	updated_at timestamp default current_timestamp
);

comment on table branch is 'company branch locations';
comment on column branch.branch_id is 'unique id for the branch';
comment on column branch.branch_name is 'branch name or location';
comment on column branch.created_at is 'record creation timestamp';
comment on column branch.updated_at is 'record update timestamp';


-- all employees in the company
create table employee (
	employee_id int primary key,
	first_name varchar(50),
	last_name varchar(50),
	birth_date date,
	sex varchar(10) check (sex in ('m', 'f', 'nb', 'undefined')),
	salary int check (salary >= 0),
	department_id int,
	role_id int,
	branch_id int,
	foreign key (department_id) references department(department_id) on delete set null on update cascade,
	foreign key (role_id) references company_roles(role_id) on delete set null on update cascade,
	foreign key (branch_id) references branch(branch_id) on delete set null on update cascade,
	created_at timestamp default current_timestamp,
	updated_at timestamp default current_timestamp,
	is_deleted boolean default false
);

comment on table employee is 'all employees in the company';
comment on column employee.employee_id is 'unique id for each employee';
comment on column employee.first_name is 'employee first name';
comment on column employee.last_name is 'employee last name';
comment on column employee.birth_date is 'date of birth';
comment on column employee.sex is 'gender';
comment on column employee.salary is 'annual salary';
comment on column employee.department_id is 'fk to department table';
comment on column employee.role_id is 'fk to company_roles table';
comment on column employee.branch_id is 'fk to branch table';
comment on column employee.created_at is 'record creation timestamp';
comment on column employee.updated_at is 'record update timestamp';
comment on column employee.is_deleted is 'soft delete flag';


-- clients that employees work with
create table client (
	client_id int primary key,
	client_name varchar(50),
	branch_id int,
	foreign key (branch_id) references branch(branch_id) on delete set null on update cascade,
	created_at timestamp default current_timestamp,
	updated_at timestamp default current_timestamp,
	is_deleted boolean default false
);

comment on table client is 'clients that employees work with';
comment on column client.client_id is 'unique client id';
comment on column client.client_name is 'name of the client';
comment on column client.branch_id is 'branch responsible for the client';
comment on column client.created_at is 'record creation timestamp';
comment on column client.updated_at is 'record update timestamp';
comment on column client.is_deleted is 'soft delete flag';


-- tracking which employees manage which branches and when
create table branch_manager (
	branch_id int,
	employee_id int,
	start_date date,
	end_date date,
	primary key(branch_id, employee_id),
	foreign key(branch_id) references branch(branch_id) on delete cascade on update cascade,
	foreign key(employee_id) references employee(employee_id) on delete cascade on update cascade,
	created_at timestamp default current_timestamp,
	updated_at timestamp default current_timestamp
);

comment on table branch_manager is 'tracking which employees manage which branches and when';
comment on column branch_manager.branch_id is 'fk to branch table';
comment on column branch_manager.employee_id is 'fk to employee table';
comment on column branch_manager.start_date is 'date the employee became manager';
comment on column branch_manager.end_date is 'date the employee stopped managing';
comment on column branch_manager.created_at is 'record creation timestamp';
comment on column branch_manager.updated_at is 'record update timestamp';


-- relationship between employees and clients (sales tracking)
create table works_with (
	employee_id int,
	client_id int,
	total_sales int check (total_sales >= 0),
	primary key(employee_id, client_id),
	foreign key (employee_id) references employee(employee_id) on delete cascade on update cascade,
	foreign key (client_id) references client(client_id) on delete cascade on update cascade,
	created_at timestamp default current_timestamp,
	updated_at timestamp default current_timestamp
);

comment on table works_with is 'relationship between employees and clients (sales tracking)';
comment on column works_with.employee_id is 'fk to employee table';
comment on column works_with.client_id is 'fk to client table';
comment on column works_with.total_sales is 'total sales from this client by this employee';
comment on column works_with.created_at is 'record creation timestamp';
comment on column works_with.updated_at is 'record update timestamp';


-- suppliers tied to a branch
create table branch_supplier (
	branch_id int,
	supplier_name varchar(50),
	supplier_type varchar(200),
	primary key (branch_id, supplier_name),
	foreign key (branch_id) references branch(branch_id) on delete cascade on update cascade,
	created_at timestamp default current_timestamp,
	updated_at timestamp default current_timestamp
);

comment on table branch_supplier is 'suppliers tied to a branch';
comment on column branch_supplier.branch_id is 'fk to branch table';
comment on column branch_supplier.supplier_name is 'name of the supplier';
comment on column branch_supplier.supplier_type is 'type of goods or services supplied';
comment on column branch_supplier.created_at is 'record creation timestamp';
comment on column branch_supplier.updated_at is 'record update timestamp';