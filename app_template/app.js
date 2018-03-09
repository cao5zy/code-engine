(function(factory){
    module.exports = factory(require('seneca')(),
			     require('log4js').getLogger('app'),
			     require('./service'),
			     require('./config')
			    );
}(function(seneca, logger, service, config){
    seneca.use(service);
    seneca.listen(config.port);
}));
