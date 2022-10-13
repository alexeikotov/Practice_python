INPUT_CODE_DELIMITER = '# ---end----'

def read_data(file_name, x):
    file = open(file_name, x)
    content = file.read()
    file.close()
    return content

def prepare_md_file(md_file):
    md_file = md_file.split('##')
    prev_titels = md_file[0]
    prev_progs = '##' + "##".join(md_file[1:])
    return prev_titels, prev_progs
    
def write_data(file_name, data):
    file = open(file_name, 'w')
    content = "".join(data)
    file.write(content)
    file.close()    

def prepare_md_titles(data):
    title = description = None

    for line in data.split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description'):
            description = line.replace('# description ', '')
    
    return title, description        
    

def prepare_md_format_data(title, description, source_code):
    md_link = '-'.join(title.lower().split())
    
    md_title = """+ [{}](#{})\n""".format(title, md_link)
    md_code = """## {}

{}
    
```python
{}
```""".format(title, description, source_code.lstrip())
    return md_title, md_code

def convert_data(data):
    titles, source_code = data.split(INPUT_CODE_DELIMITER)  
    title, description = prepare_md_titles(titles)
    md_title, md_code = prepare_md_format_data(title, description, source_code)
    return md_title, md_code

def add_new_file_to_md(new_file, md_file):
    new_md_title, new_md_code = convert_data(new_file)
    prev_titles, prev_progs = prepare_md_file(md_file)
    template = """{}\n{}\n\n{}\n\n{}"""
    result = template.format(prev_titles.strip(), new_md_title.strip(),  prev_progs.strip(), new_md_code.strip())
    return result

def main():
    new_file = read_data('solution.py','r')
    md_file = read_data('matrix.md','r')
    result = add_new_file_to_md(new_file, md_file)

    write_data('matrix.md', result)



if __name__ == "__main__":
    main()
