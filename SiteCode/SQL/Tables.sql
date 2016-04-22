create table users
	(id int auto_increment,
	 email varchar(60) not null unique,
	 firstname varchar(75),
	 lastname varchar(75),
	 user_pw char(66),
	 primary key (id)
	 ) ENGINE = InnoDB;
	 
create table searches
	(user_id int,
	 artist_id varchar(100),
	 primary key (user_id, artist_id),
	 foreign key (user_id)
	    references users (id)
	    on delete cascade
	    on update cascade
	 ) ENGINE = InnoDB;
	 
