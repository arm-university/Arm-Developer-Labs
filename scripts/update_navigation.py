import os
from pathlib import Path 
import yaml

undergraudate_dir = "../docs/Undergraduate-Level"
masters_dir = "../docs/Masters-Level"
phd_dir = "../docs/PhD-Level"

undergraduate_pathlist = Path(undergraudate_dir).rglob('*.md')
masters_pathlist = Path(masters_dir).rglob('*.md')
phd_pathlist = Path(phd_dir).rglob('*.md')

navigation = '../docs/_data/navigation.yml'

def process_yml(pathlist, level: str):
    with open(navigation, 'r') as f:
        lines = f.readlines()
        
    header = lines[:18] 
    partial_content = ''.join(lines[18:])

    yam_tab = yaml.safe_load(partial_content)
    
    yam_tab[level][0]['children'].clear()
    
    for path in pathlist:
        path_in_str = str(path)[7:].replace(".md", ".html")
        
        if any(map(lambda sub: sub in path_in_str, ("undergraduate.html", "masters.html", "phd.html"))):
            continue

        title = path_in_str.rsplit('/')[-1].replace(".html", "")
        yam_tab[level][0]['children'].append({'title': title, 'url': path_in_str})
    
    new_yaml_text = yaml.safe_dump(yam_tab, sort_keys=False)
    
    with open(navigation, 'w') as f:
        f.write(''.join(header))
        f.write(new_yaml_text)
        
if __name__ == "__main__":
    process_yml(undergraduate_pathlist, 'undergraduate')
    process_yml(masters_pathlist, 'masters')
    process_yml(phd_pathlist, 'phd')