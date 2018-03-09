(function(factory){
    module.exports = factory(require('log4js').getLogger('implementation'));
}(function(logger){
    function implementation(){};

    implementation.prototype = {
	//your code here please!
    };
    return new implementation();
}));
