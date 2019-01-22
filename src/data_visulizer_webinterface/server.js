var express = require('express');
var app = express();
var server = require('http').createServer(app);
var io = require('socket.io')(server);
var express = require('express');
var session = require('express-session');
var session = require('express-session');
var bodyParser = require('body-parser');
var mail = require("nodemailer");
var sessionstore = require('sessionstore');
var os = require("os");
var chalk = require('chalk');
var json2csv = require('json2csv');
var mqtt = require('mqtt');
var path = require('path');
var uuidv1 = require('uuid/v1');
var randomstring = require("randomstring");
var client = mqtt.connect('mqtt://127.0.0.1')



var VERSION = "5.1";
var VERSION_IE = "5.1";
var port = process.env.PORT || 3014;







var transporter = mail.createTransport({
    host: 'smtp.strato.de',
    port: 465,
    secure: true, // true for 465, false for other ports
    auth: {
        user: "info@marcelochsendorf.com", // generated ethereal user
        pass: "fjieow3490580jsdifio" // generated ethereal password
    }
});



app.set('trust proxy', 1);
app.use(function (req, res, next) {
    if (!req.session) {
        return next() //handle error
    }
    next() //otherwise continue
});
app.set('views', __dirname + '/views');
app.engine('html', require('ejs').renderFile);
// Routing
app.use(express.static(path.join(__dirname, 'public')));
app.use(session({
    secret: 'ssshhfddghjhgewretjrdhfsgdfadvsgvshthhh',
    store: sessionstore.createSessionStore(),
    resave: true,
    saveUninitialized: true
}));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
    extended: true
}));

app.use(function (req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});




server.listen(port, function () {
    console.log('Server listening at port %d', port);
});




app.get('/', function (req, res) {
    sess = req.session;
    res.render('index.ejs', {
        key: req.query.key,
        err: 0,
        version: VERSION,
      
    });
});

app.post('/', function (req, res) {
   res.redirect('demo');
});


app.get('/index.html', function (req, res) {
    res.redirect('/');
});

app.get('/demo', function (req, res) {
    sess = req.session;
    res.render('demo.ejs', {
     

    });
});

app.get('/sender', function (req, res) {
    sess = req.session;
    res.render('sender.ejs', {


    });
});




app.get('/state', function (req, res) {
    sess = req.session;
    res.send("es liegt keine fehler vor");
});


client.on('connect', function () {
    client.subscribe('chemtechhack1234', function (err) {
        if (!err) {
         //   client.publish('presence', 'Hello mqtt')
        }
    })
})



client.on('chemtechhack1234', function (topic, message) {
    // message is Buffer

    io.emit('broadcast', JSON.parse(message.toString()));
    //io.emit('broadcast', { errors: [0, 1, 2, 3, 4, 5, 7, 8, 9], location: 'left', time: '12:39' });
    console.log(message.toString());

   //client.publish('chemteckhack1234alexa', 'true');

})


io.on('connection', function (socket) {
    socket.on('clear', function (msg) {
         console.log('message: ' + msg);
              client.publish('chemteckhack1234clear', 'true');
              let bufferOne = Buffer.from('0');
              client.publish('chemtechhack1234light', '1');
              console.log("send cleart");
    });


    socket.on('sendhammer', function (msg) {
        console.log('hammer message: ' + msg);
        client.publish('chemtechhack1234hammer', 'true');
        io.emit('broadcast', { errors: [0, 1, 2, 3, 4, 5, 7, 8, 9], location: 'right', time: '14:59' });

        setTimeout(() => {
            //   io.emit('msg', {abc:123});
            io.emit('msg', { errors: [0, 1, 2, 3, 4, 5, 1, 8, 9], location: 'left', time: '14:59' });
        }, 10000);
    });

    socket.on('sendunwucht', function (msg) {
        console.log('unwucht message: ' + msg);
        client.publish('chemtechhack1234hammer', 'true');
        io.emit('broadcast', { errors: [0, 1, 2, 3, 4, 5, 7, 8, 9], location: 'left', time: '14:59' });


        setTimeout(() => {
            //   io.emit('msg', {abc:123});
            io.emit('msg', { errors: [0, 1, 2, 3, 4, 5, 1, 8, 9], location: 'right', time: '14:59' });
        }, 10000);
    });
});




