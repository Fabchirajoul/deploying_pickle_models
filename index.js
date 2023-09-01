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
                "predictions_Jn": messages
            }
        );
     });
});

app.get("/api/Jr_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/jr_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions_Jr": messages
            }
        );
     });
});

app.get("/api/Jw_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/jw_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions_Jw": messages
            }
        );
     });
});


 

app.get("/api/q_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/q_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions_Q": messages
            }
        );
     });
});


app.get("/api/srf_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/srf_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions_srf": messages
            }
        );
     });
});


app.get("/api/esr_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/esr_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions_esr": messages
            }
        );
     });
});



app.get("/api/ucsvsr_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/ucsvsr_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions_ucsvsr": messages
            }
        );
     });
});
app.get("/api/rqd_model", function (req, res) {
    // run python code
    PythonShell.run('python-code/rqd_model.py', null).then(messages => {
        console.log(messages)
        res.json(
            {
                "predictions_rqd": messages
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
                "predictions_Ja": messages
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
                "predictions_rmr": messages
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
                "predictions_us": messages
            }
        );
     });
});



// Adding our port listener which is by defualt
let PORT = process.env.PORT || 3008;

app.listen(PORT, function () {
  console.log("CAPSTONE API WITH MODEL STARTING ON", PORT);
});