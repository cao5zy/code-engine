# seneca_server_template
## A template project to build microservice with seneca framework

### What does it do for you
This template project will help you create your microservice project that based on seneca framework quickly.

### Prerequisite
[Ansible](https://github.com/ansible/ansible) should be installed in your local environment.  
For ubuntu user, run following command to install  

    sudo apt-get install ansible

### Try it
#### download the code  

    mkdir project_folder
    cd project_folder
    wget https://github.com/cao5zy/seneca_server_template/archive/1.0.3.zip && unzip 1.0.3.zip && mv seneca_server_template-1.0.3 .seneca_server_template && rm 1.0.3.zip 
    
    
#### Input methods and configurations of your service   
Go to `.seneca_server_template`. Please open build.yaml file, then input methods and configurations.  

    vars:
      template_folder: "./app_template"
      deploy_folder: "./output" # the folder that will store the generated files for service. You can specify a absolute path or a relative to current folder
      app_name: "seneca_service" # the name of service
      methods: # a list of dict object, with key, name and role
      - { name: "add"} 
      default_configs: # a list which will be stored in defaults/main.yml
      - port
        
In "methods" section, you input your methods of your service interface in json object form.  
"role" can be regarded as namespace of your methods. It is useful when you try to place your service behind the proxy.  
"name" is the name of your method.  
Items in "methods" are list in YAML syntax. So don't forget "-" before your method item.  
In "configs" section, you input the configurations for your service.  
"port" is a must. It defines the port number for your service.
If the value is string type, you must wrap it with \".
Items in "config" are dictionary in YAML syntax. So don't forget 2 spaces indent before the item.

That's all you currently have to do with the yaml file. For more information about yaml, please follow the [link](http://www.yaml.org/)


#### How to work with the generated code
When the files are generated, the structure looks like following.   

    code
      |- app.js
      |- config
          |- default.json
          |- log4js.json
      |- config.js
      |- deploy
          |- roles
	      |- templates
	          |- default.json.template
	      |- defaults
	          |- main.yml
      |- implemenation.js
      |- package.json
      |- service.js

You should write your own code in implementation.js  

    (function(factory){
        module.exports = factory(require('log4js').getLogger('implementation'));
    }(function(logger){
        function implementation(){};

        implementation.prototype = {
	    add: function(param, callback) {}    //your code here please!
        };
        return new implementation();
    }));


