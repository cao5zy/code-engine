(function(factory){
    module.exports = factory(require('config'));
}(function(config){
    return require('./config/default.js');
}));
