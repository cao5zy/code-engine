(function(factory){
    module.exports = factory(require('seneca')(),
			     require('log4js'),
			     require('./service'),
			     require('./config')
			    );
}(function(seneca, log4js, service, config){
    log4js.configure("./config/log4js.json");
    seneca.use(service);
    seneca.listen(config.port);
}));
