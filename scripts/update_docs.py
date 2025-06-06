import os
import re
import shutil
from pathlib import Path
import frontmatter

projects_dir = "../Projects/Projects"
extended_projects_dir = "../Projects/Extended-Team-Projects"

projects_pathlist = [Path("../Projects/projects.md")]
projects_projects_pathlist = Path(projects_dir).rglob('*.md')
projects_extended_project_pathlist = Path(extended_projects_dir).rglob('*.md')
research_pathlist = [Path("../Research/research.md")]

docs_projects_dir = "../docs/Projects"
docs_projects_projects_dir = "../docs/Projects/Projects"
docs_research_dir = "../docs/Research"
docs_extended_project_dir = "../docs/Projects/Extended-Team-Projects"
docs_img_dir = "../docs/images"

index_frontmatter = """---
title: Academic Projects Repository
tags: TeXt
article_header:
  type: main_cover
  image:
    src: ./images/DeveloperLabs_Header.png
---
"""

def clean() :
    clean_lst = [docs_projects_dir,docs_projects_projects_dir, docs_research_dir, docs_extended_project_dir]
    for dirpath in clean_lst:
        if os.path.exists(dirpath) and os.path.isdir(dirpath):
            shutil.rmtree(dirpath)
            os.makedirs(dirpath)
        else:
            os.makedirs(dirpath)

def convert_md_images_to_html(md_text: str, doc_path: Path, docs_dir: str) -> str:
    pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    docs_dir_path = Path(docs_dir)
    
    def replace(match):
        img_path = match.group(1)

        if doc_path.resolve() == Path("../README.md").resolve() and img_path == "./images/DeveloperLabs_Header.png":
            return ""
        
        elif doc_path.resolve() == Path("../Research/research.md").resolve() and img_path == "../images/Research_on_arm_banner.png":
            return ""
        
        source_path = (doc_path.parent / img_path).resolve()

        target_folder = (docs_dir_path / "images").resolve()
        target_folder.mkdir(parents=True, exist_ok=True)
        
        if source_path.is_file():
            shutil.copy2(source_path, target_folder)
        else:
            print(f"Warning: {source_path} does not exist in {doc_path}!")
        
        new_img_path = f"./images/{Path(img_path).name}"
        
        if "ACA_badge.jpg" in new_img_path:
            return f'<img class="image image--l" src="{new_img_path}"/>'
            
        return f'<img class="image image--xl" src="{new_img_path}"/>'

    return re.sub(pattern, replace, md_text)

def convert_md(md_text: str) -> str:
    pattern_link = "[Developer Labs Website](https://arm-university.github.io/Arm-Developer-Labs/)"
    replacement_link = "[Developer Labs Repository](https://github.com/arm-university/Arm-Developer-Labs)"
    pattern_youtube = "[![Arm-CMU collaboration](https://img.youtube.com/vi/zaRozkrcix0/0.jpg)](https://www.youtube.com/watch?v=zaRozkrcix0)"
    replacement_youtube = '<iframe width="560" height="315" src="https://www.youtube.com/embed/zaRozkrcix0?si=eRZirXrv5300fnBc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'

    replaced_md = md_text

    if pattern_youtube in replaced_md:
        replaced_md = replaced_md.replace(pattern_youtube, replacement_youtube)
    if pattern_link in replaced_md:
        replaced_md = replaced_md.replace(pattern_link, replacement_link)

    return replaced_md

def format_content(pathlist, academic_level, docs_path):
    for path in pathlist:
        path = Path(path)

        if path.name == "README.md":
            continue

        raw_text = path.read_text(encoding="utf-8")
        post = frontmatter.loads(raw_text)
        body = post.content
    
        if path.name in ["projects.md", "research.md"]:

            post.metadata["article_header"] = {
                "type": "cover",
                "image": {
                    "src": "/images/DeveloperLabs_Header.png",
                },
            }
        
        post.metadata["layout"] = "article"
        
        if path.name == "projects.md":
            pass
        
        elif academic_level == "projects":
            post.metadata["sidebar"] = {
                "nav": academic_level,
            }
        
        formatted_content = frontmatter.dumps(post)
        
        converted_content = convert_md_images_to_html(
            formatted_content,
            path,
            docs_path,
        )

        out_file = Path(docs_path, path.name)
        out_file.write_text(converted_content, encoding="utf-8")

        
def format_index():
    src = "../README.md"
    docs_path = "../docs"
    with open(src, 'r', encoding='utf-8') as f:
        formatted_content = convert_md(index_frontmatter + f.read())
        converted_content = convert_md_images_to_html(
            formatted_content,
            Path(src),
            docs_path
        )
        out_file = os.path.join(docs_path, "index.md")
        with open(out_file, 'w', encoding='utf-8') as out_f:
            out_f.write(converted_content)


def main():
    clean()
    format_index()
    format_content(projects_pathlist, "projects", docs_projects_dir)
    format_content(projects_projects_pathlist, "projects", docs_projects_projects_dir)
    format_content(research_pathlist, "research", docs_research_dir)
    format_content(projects_extended_project_pathlist, "research", docs_extended_project_dir)
    
if __name__ == "__main__":
    main()