# code-engine
Code-engine is a dead simple engine based on [Jinja2](http://jinja.pocoo.org/) to make you free from generation process.

```
from code_engine import app

app.publish(template_path, json_data, output_path)

```

Instructions
- The folder structure in `template_path` will be mapped directly to the structure in `output_path`.
- The template file is end with `.t`

## Case Studies
### Generate the files based on templates
#### Setup the templates
- template path: /var/templates
- structure
```
server.js.t
config/
  - config.js.t

```
#### Setup the data
```
{
  name: service1,
  port: 8088
}
```
Then run the code below.
```
app.publish("/var/templates", data, "/var/project1")

```
In the path `/var/project1`, you will find the following files.
```
server.js
config/
  - config.js

```
