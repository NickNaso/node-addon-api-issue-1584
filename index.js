'use strict';

const except = require('bindings')('addon');

console.log(addon.echo('Hello, World!'));