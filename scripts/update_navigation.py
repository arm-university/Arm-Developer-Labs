import os
from pathlib import Path 
import yaml

projects_undergraduate_dir = "../Projects/Accessible"
projects_masters_dir = "../Projects/Advanced"
research_dir = "../Research/PhD"
extended_projects_dir = "../Research/Extended-Team-Projects"

projects_undergraduate_pathlist = Path(projects_undergraduate_dir).rglob('*.md')
projects_masters_pathlist = Path(projects_masters_dir).rglob('*.md')
research_phd_pathlist = Path(research_dir).rglob('*.md')
research_extended_project_pathlist = Path(extended_projects_dir).rglob('*.md')

navigation = '../docs/_data/navigation.yml'

def process_yml(pathlist, level: str, tab: str):
    with open(navigation, 'r') as f:
        lines = f.readlines()
        
    header = lines[:12] 
    partial_content = ''.join(lines[12:])

    yam_tab = yaml.safe_load(partial_content)
    
    if tab == 'research':
        if level == 'phd':
            yam_tab[tab][0]['children'].clear()
            
            for path in pathlist:
                path_in_str = str(path)[2:].replace(".md", ".html")
                title = path_in_str.rsplit('/')[-1].replace(".html", "")
                yam_tab[tab][0]['children'].append({'title': title, 'url': path_in_str})
            
            new_yaml_text = yaml.safe_dump(yam_tab, sort_keys=False)
            
            with open(navigation, 'w') as f:
                f.write(''.join(header))
                f.write(new_yaml_text)
        else:
            yam_tab[tab][1]['children'].clear()
        
            for path in pathlist:
                path_in_str = str(path)[2:].replace(".md", ".html")
                title = path_in_str.rsplit('/')[-1].replace(".html", "")
                yam_tab[tab][1]['children'].append({'title': title, 'url': path_in_str})
            
            new_yaml_text = yaml.safe_dump(yam_tab, sort_keys=False)
            
            with open(navigation, 'w') as f:
                f.write(''.join(header))
                f.write(new_yaml_text)
    else:
        if level == 'accessible':
            yam_tab[tab][0]['children'].clear()
        
            for path in pathlist:
                path_in_str = str(path)[2:].replace(".md", ".html")
                title = path_in_str.rsplit('/')[-1].replace(".html", "")
                yam_tab[tab][0]['children'].append({'title': title, 'url': path_in_str})
            
            new_yaml_text = yaml.safe_dump(yam_tab, sort_keys=False)
            
            with open(navigation, 'w') as f:
                f.write(''.join(header))
                f.write(new_yaml_text)
        else:
            yam_tab[tab][1]['children'].clear()
        
            for path in pathlist:
                path_in_str = str(path)[2:].replace(".md", ".html")
                title = path_in_str.rsplit('/')[-1].replace(".html", "")
                yam_tab[tab][1]['children'].append({'title': title, 'url': path_in_str})
            
            new_yaml_text = yaml.safe_dump(yam_tab, sort_keys=False)
            
            with open(navigation, 'w') as f:
                f.write(''.join(header))
                f.write(new_yaml_text)
        
if __name__ == "__main__":
    process_yml(projects_undergraduate_pathlist, 'accessible', 'projects')
    process_yml(projects_masters_pathlist, 'advanced', 'projects')
    process_yml(research_phd_pathlist, 'phd', 'research')
    process_yml(research_extended_project_pathlist, 'extended-team-project', 'research')