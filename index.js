import express from "express"; 

import { PythonShell } from 'python-shell'


const app = express();

// Declaring the static middleware

app.use(express.static("public"));

// Makes req.body works (This is known as the middleware)
app.use(express.json());

// Section that lists all the available price plan starts here


app.get("/api/Jn_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/jn_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
     });
});



app.get("/api/Ja_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/ja_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
     });
});



app.get("/api/rmr_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/rmr_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
     });
});


app.get("/api/mus_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/mus_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions": messages
            }
        );
     });
});



// Adding our port listener which is by defualt
let PORT = process.env.PORT || 3008;

app.listen(PORT, function () {
  console.log("Price Plan API with SQL starting on port", PORT);
});