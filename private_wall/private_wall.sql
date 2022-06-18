Select * from messages;

Select * from users;

SELECT users.first_name as sender, users2.first_name as reciever, messages. * FROM users LEFT JOIN messages ON users.id = messages.sender_id LEFT JOIN users as users2 ON users2.id = messages.receiver_id WHERE users2.id = 1