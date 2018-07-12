(function(factory){
    module.exports = factory(require('log4js').getLogger('service'),
			     require('./config'),
			     require('./implementation')
    );
}
 (function(logger, config, impl){
     return function(options){
	 {% for method in methods %}this.add({"action": "{{method.name}}"}, function(msg, respond){
	     impl.{{method.name}}(msg.param, (data)=>respond(data, null));
	 });
	 {% endfor %}

	 this.add({"name": "test"}, function(args, response){
	     response(null, {'result': 'OK'});
	 });
     };
 }));
