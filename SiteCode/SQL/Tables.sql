create table users
	(username varchar(15) not null unique,
	 user_pw varchar(12), 
	 primary key (user_id)
	 );
	 
create table searches
	(user_id varchar(15) not null unique,
	 search_id numeric(12) not null unique,
	 primary key (search_id)
	 foreign key (user_id) references users
	 );
	 
