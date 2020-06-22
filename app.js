var express = require('express');
var http = require('http');
var axios = require('axios');
var app = express();

app.use(express.static(__dirname + '/public'));
app.use(express.json());

// This is the API format to check userid and password
// localhost:5000/

// this is the api Format to create new Account
// localhost:5000/create?username=David&password=123456

app.post("/login", async (request, response) => {

    var options = {
        host: 'localhost',
        port: 5000,
        path: `/?username=${request.body.username}&password=${request.body.password}`,
        method: 'GET'
    };
    
    var x = http.request(options, function (res) {
        console.log("Connected");
        res.on('data', function (data) {
            var result = data.toString('utf-8');
            if (result === "true") {
                response.status(200).json({
                    msg: "Login Successfully",
                });
            }
            else {
                response.status(403).json({ error: "Forbidden" });
            }
        });
    });

    x.end();

});

app.post("/signup", (req, response) => {

    var signupoptions = {
        host: 'localhost',
        port: 5000,
        path: `/create?username=${req.body.username}&password=${req.body.password}`,
        method: 'GET'
    };

    var x = http.request(signupoptions, function (res) {
        console.log("Connected");
        res.on('data', function (data) {
            var result = data.toString('utf-8');
            if (result === "ok create") {
                response.status(201).json({
                    msg: "Register Successfully",
                });
            }
            // else {
            //     res.status(400).json({
            //         errormsg: "E-mail Already Register try another e-mail",
            //     });
            // }
        });
    });

    x.end();
});

http.createServer(app).listen(3000);