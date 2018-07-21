# code-engine
Code-engine is a dead simple engine based on [Jinja2](http://jinja.pocoo.org/) to make you free from generation process.

It looks like a pipe. You push your data into the end of the pipe. Finally, the files will be generated at the other end.  
![diagram](/resources/code-engine-diagram.png)  

## Installation   
```
pip install code_engine
```

## Template definition files  
Template definition files include `definition` and `template`.  

### definition
```
    {
      "subscribe_name": "methods",
      "template_path": "./.template/service.template",
      "output_path": "./code/service.js"
    }
```
In this section, it tells the code-engine where get the template and where to output the file.  
- `subscribe_name` is used to subscribe the data when the data is pushed into the pipe.  
- `template_path` could be absolute path or relative path to the definition file.   
- `output_path` could be absolute path or relative path to the definition file.   



### template
```
function service(){}

service.prototype = {
  {% for method in method_names %}{{method}}: function(){}{%if not loop.last %},{% endif %}
  {% endfor %}
}
```  
In this section, it tells the code-engine how to generate the file with the subscribed data.  
Please go to [Jinja2](http://jinja.pocoo.org/) for documentation of the template syntax.  

## How to use it 
### Prepare
First prepare your definition files and templates.  Assuming the definition files are placed at `/var/your_project`.  
The definition file should have extension as `.ce` with json format. In this practice, there is only one, `service.ce`.  

*service.ce*
```
{
  "subscribe_name": "methods_data",
  "template_path": "/var/your_project/service.template",
  "output_path": "/var/your_project_src/service.js"
}
```

Based on the definition above, the template file `service.template` should be available.  

*service.template*
```
function service(){}

service.prototype = {
  {% for method in method_names %}{{method}}: function(){}{%if not loop.last %},{% endif %}
  {% endfor %}
}
```

After the defintion files and templates are ready, the code-engine can run.  

### Run
```
import code_engine

code_engine.publish("/var/your_project", "methods_data", {"method_names": ["search_project_by_name", "search_project_by_tag"]})
```

Then open the file at `/var/your_project_src/service.js`. The output would be like following.  
```
function service(){}

service.prototype = {
  search_project_by_name: function(){},
  search_project_by_tag: function(){}
}
```
# Summary
In this process, you only need take care of your data and templates. This would be useful when you try to generate a big scale of files.
