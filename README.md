### Syntax for Manage Database Flask

`flask db init`
Create instance and migrations folders
`flask db migrate -m “inital commit”`
Creates the database.db file in the instance folder
`flask db upgrade`
Creates the user tables and other tables based on the schema specified in the models.
