const express = require('express');
const path = require('path');
const db = require('./config/mongoose');
const Contact = require('./models/contact');
const port = 8000;
const app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded());
app.use(express.static('assets'));

// My global Array of Contacts
var contactList = [
	{
		name: 'Arpan',
		phone: '1111111111',
	},
	{
		name: 'Tony Stark',
		phone: '1234567890',
	},
	{
		name: 'Coding Ninjas',
		phone: '12131321321',
	},
];

// For URL /Practice
app.get('/practice', function (req, res) {
	return res.render('practice', {
		title: 'Let us play with ejs',
	});
});

// To send Respond to browser from Server
app.get('/', function (req, res) {
	Contact.find({}, (err, myConto) => {
		if (err) {
			console.log('Error in fetching Contacts from DataBase');
			return;
		}

		return res.render('home', {
			title: 'Contact List',
			contact_list: myConto,
		});
	});
});

// To add any contact in Our Contact List
app.post('/create-contact', function (req, res) {
	//contactList.push(req.body);
	//return res.redirect('/');
	Contact.create(req.body, (err, newContact) => {
		if (err) {
			console.log('Error');
			return;
		}
		console.log('***********', newContact);
		return res.redirect('back');
	});
});

app.listen(port, function (err) {
	if (err) {
		console.log('Error in running the server', err);
	}
	console.log('Yup!My Server is running on Port', port);
});

// TO delete any contact from Conatct List
app.get('/delete-contact/', function (req, res) {
	// console.log(req.query);
	// let phone = req.query.phone;
	let id = req.query.id;
	Contact.findByIdAndDelete(id, (err) => {
		if (err) {
			console.log('Error in deleting contact from DataBase');
			return;
		}
		return res.redirect('back');
	});
});
