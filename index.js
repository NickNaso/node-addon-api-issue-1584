'use strict';

const addon = require('bindings')('addon');

console.log(addon.echo('Hello, World!'));