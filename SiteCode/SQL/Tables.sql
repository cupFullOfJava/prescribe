create table users
	(username varchar(15) not null unique,
	 user_pw varchar(12), 
	 primary key (username)
	 );
	 
create table searches
	(username varchar(15) not null unique,
	 artist_id numeric(12) not null unique,
	 primary key (artist_id),
	 foreign key (username) references users(username)
	 );
	 
