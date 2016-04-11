create table users
	(email varchar(60) not null unique,
	 firstname varchar(75),
	 lastname varchar(75),
	 user_pw char(66),
	 primary key (email)
	 );
	 
create table searches
	(email varchar(15) not null unique,
	 artist_id varchar(30),
	 primary key (artist_id),
	 foreign key (email) references users(email)
	 );
	 
