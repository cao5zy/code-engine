The code engine will collect the file with extension `.ce` to generate the configuration file.  
```
{
  "subscribe_name": "the name to subscribe data in the pipeline",
  "template": "file path of template. It could be relative path to the current folder",
  "output_dir": "the directory to store the generated file. If it is omitted, it will be generated at the same path as the template"
}
```

Then it will generate the file with extension `.ce.staging` which contains `variables`. 
```
{
  "subscribe_name": "the name to subscribe data in the pipeline",
  "template": "file path of template. It could be relative path to the current folder",
  "output_dir": "the directory to store the generated file. If it is omitted, it will be generated at the same path as the template",
  "variables": {"data": "123"}
}
```

Finally, the files with extension `.ce.staging` are used to generate the real code. After the code generation, the files with extension `.ce.staging` are removed automatically.  

