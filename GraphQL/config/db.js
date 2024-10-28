const seq = require('sequelize');

const seq = new seq('xy', 'root', 'sanju', {
    host: 'localhost',
    dialect: 'mysql',
    logging: true
});

seq.authenticate()
    .then(() => {
        console.log('Connection has been established successfully.');
    })
    .catch(err => {
        console.error('Unable to connect to the database:', err);
    });


    module.exports = seq;