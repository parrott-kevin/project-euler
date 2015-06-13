'use strict';

var express = require('express');
var path = require('path');

var app = express();

app.use('/', express.static(path.join(__dirname, 'public/dist')));

module.exports = app;