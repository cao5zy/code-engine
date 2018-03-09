# seneca_server_template
## A template project to build microservice with seneca framework

### Guideline
The ansible should be installed in your local environment.  
The values should be modified in the build.yaml when it is used to your real project.

### Install Ansible
Please refer to [Ansible Github](https://github.com/ansible/ansible) for details. Generally, if you work on Ubuntu, you can install ansible as follow command.  
    sudo apt-get install ansible

### Clone the code

    mkdir code
    git clone https://github.com/cao5zy/seneca_server_template.git
    cd code
    ansible-playbook build.yaml # run it after you finish your service definition.
    
### Service definition
Please follow the comments on vars section. Follow the link here if you are interested in [YAML](http://www.yaml.org/)

    vars:
      template_folder: "./app_template"
      deploy_folder: "./output" # the folder that will store the generated files for service. You can specify a absolute path or a relative to current folder
      app_name: "seneca_service" # the name of service
      methods: # a list of dict object, with key, name and role
      - { name: "add" , role: "app"} 
      configs: # a dict object to set the config
        port: 8080
        protocol: \"http\" # if the value is string, the \" should wrap the value
        
Generally, methods are defined at methods and configurations are set at configs. You can specify any configuration here however the "port" is a must.
