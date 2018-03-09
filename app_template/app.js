(function(factory){
    module.exports = factory(require('seneca')(),
			     require('logger').getLogger('app'),
			     require('./service'),
			     require('./config')
			    );
}(function(seneca, logger, service){
    seneca.use(service);
    seneca.listen(config.port);
}));
