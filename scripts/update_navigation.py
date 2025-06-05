import os
from pathlib import Path 
import yaml
import frontmatter

projects_dir = "../Projects/Projects"
extended_projects_dir = "../Projects/Extended-Team-Projects"

projects_pathlist = Path(projects_dir).rglob('*.md')
extended_project_pathlist = Path(extended_projects_dir).rglob('*.md')

navigation = '../docs/_data/navigation.yml'

def process_yml(pathlist, level: str, tab: str):
    with open(navigation, 'r') as f:
        lines = f.readlines()
        
    header = lines[:6] 
    partial_content = ''.join(lines[6:])

    yam_tab = yaml.safe_load(partial_content)
    
    if level == 'projects':
        yam_tab[tab][0]['children'].clear()
    
        for path in pathlist:
            path_in_str = "_posts" + str(path)[2:].replace(".md", ".html")
            title = path_in_str.rsplit('/')[-1].replace(".html", "")
            post = frontmatter.load(path)  
            platform = post.metadata.get("platform")
            sw_hw = post.metadata.get("sw-hw")
            support_level = post.metadata.get("support-level")
            subjects = post.metadata.get("subjects")
            yam_tab[tab][0]['children'].append({'title': title, 'url': path_in_str, 'subjects': subjects, 'platform': platform, 'sw-hw': sw_hw, 'support-level': support_level})
        
        new_yaml_text = yaml.safe_dump(yam_tab, sort_keys=False)
        
        with open(navigation, 'w') as f:
            f.write(''.join(header))
            f.write(new_yaml_text)
    
    elif level == 'extended-team-project':
        yam_tab[tab][1]['children'].clear()
    
        for path in pathlist:
            path_in_str = "_posts" + str(path)[2:].replace(".md", ".html")
            title = path_in_str.rsplit('/')[-1].replace(".html", "")
            post = frontmatter.load(path)  
            platform = post.metadata.get("platform")
            sw_hw = post.metadata.get("sw-hw")
            support_level = post.metadata.get("support-level")
            subjects = post.metadata.get("subjects")
            yam_tab[tab][1]['children'].append({'title': title, 'url': path_in_str, 'subjects': subjects, 'platform': platform, 'sw-hw': sw_hw, 'support-level': support_level})
        
        new_yaml_text = yaml.safe_dump(yam_tab, sort_keys=False)
        
        with open(navigation, 'w') as f:
            f.write(''.join(header))
            f.write(new_yaml_text)
        
if __name__ == "__main__":
    process_yml(projects_pathlist, 'projects', 'projects')
    process_yml(extended_project_pathlist, 'extended-team-project', 'projects')