(function(factory){
    module.exports = factory(require('log4js').getLogger('service'),
			     require('./config'),
			     require('./implementation')
    );
}
 (function(logger, config, impl){
     return function(options){
	 {% for method in methods %}this.add({"role":"{{method.role}}", "name":"{{method.name}}"}, function(args, response){
	     impl.{{method.name}}(args, response);
	 });
	 {% endfor %}

	 this.add({"name": "test"}, function(args, response){
	     response(null, {'result': 'OK'});
	 });
     };
 }));
