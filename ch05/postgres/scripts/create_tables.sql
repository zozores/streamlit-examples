CREATE TABLE Paygrades (
	id SERIAL,
	base_salary varchar(255) NOT NULL,
	reimbursement varchar(255),
	bonuses varchar(255),
	PRIMARY KEY (id)
);

CREATE TABLE Persons (
	id SERIAL,
	name varchar(255) NOT NULL,
	date_of_birth varchar(255) NOT NULL,
	paygrade_id int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (paygrade_id) REFERENCES Paygrades(id)
);
