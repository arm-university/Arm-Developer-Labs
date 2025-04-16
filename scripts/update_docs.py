import os
import re
import shutil
from pathlib import Path

projects_undergraduate_dir = "../Projects/Undergraduate"
projects_masters_dir = "../Projects/Masters"
research_phd_dir = "../Research/PhD"

projects_pathlist = [Path("../Projects/projects.md")]
projects_undergraduate_pathlist = Path(projects_undergraduate_dir).rglob('*.md')
projects_masters_pathlist = Path(projects_masters_dir).rglob('*.md')
research_pathlist = [Path("../Research/research.md")]
research_phd_pathlist = Path(research_phd_dir).rglob('*.md')

docs_projects_dir = "../docs/Projects"
docs_undergraudate_dir = "../docs/Projects/Undergraduate"
docs_masters_dir = "../docs/Projects/Masters"
docs_research_dir = "../docs/Research"
docs_phd_dir = "../docs/Research/PhD"
docs_img_dir = "../docs/images"

contents_frontmatter = """---
layout: article
title: {title}
sidebar:
  nav: {level}
---
"""

index_frontmatter = """---
title: Academic Projects Repository
tags: TeXt
article_header:
  type: cover
  image:
    src: ./images/Research_on_arm_banner.png
---
"""

def clean() :
    clean_lst = [docs_projects_dir,docs_undergraudate_dir, docs_masters_dir, docs_research_dir, docs_phd_dir]
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
        print(match)
        img_path = match.group(1)

        if doc_path.resolve() == Path("../README.md").resolve() and img_path == "./images/Research_on_arm_banner.png":
            return ""
        
        source_path = (doc_path.parent / img_path).resolve()

        if img_path.startswith("../images"):
            target_folder = (docs_dir_path.parent / "images").resolve()
        else:
            target_folder = (docs_dir_path / "images").resolve()

        target_folder.mkdir(parents=True, exist_ok=True)
        
        if source_path.is_file():
            shutil.copy2(source_path, target_folder)
        else:
            print(f"Warning: {source_path} does not exist in {doc_path}!")
        
        new_img_path = f"./images/{Path(img_path).name}"
        print(new_img_path)
        return f'<img class="image image--xl" src="{new_img_path}"/>'

    return re.sub(pattern, replace, md_text)

def convert_md_videos_to_html(md_text: str) -> str:
    pattern = re.compile(
        r'\[\s*<img[^>]*src="https:\/\/img\.youtube\.com\/vi\/zaRozkrcix0\/0\.jpg"[^>]*>\s*\]\(https:\/\/www\.youtube\.com\/watch\?v=zaRozkrcix0\)'
    )

    replacement = (
        '<iframe width="560" height="315" src="https://www.youtube.com/embed/zaRozkrcix0?si=eRZirXrv5300fnBc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
    )

    return re.sub(pattern, replacement, md_text)

def format_content(pathlist, academic_level, docs_path):
    for path in pathlist:
        path_in_str = str(path)
        
        if "README.md" in path_in_str:
            continue
        
        with open(path_in_str, 'r', encoding='utf-8') as f:
            content_title = f.readline()[2:]
            content_level = academic_level
            content = f.read()
            
            formatted_frontmatter = contents_frontmatter.format(
                title=content_title,
                level=content_level
            )
            formatted_content = formatted_frontmatter + content
            
            converted_content = convert_md_images_to_html(
                formatted_content,
                path,
                docs_path
            )
            
            out_file = os.path.join(docs_path, path.name)
            with open(out_file, 'w', encoding='utf-8') as out_f:
                out_f.write(converted_content)
        
def format_index():
    src = "../README.md"
    docs_path = "../docs"
    with open(src, 'r', encoding='utf-8') as f:
        formatted_content = index_frontmatter + f.read()
        converted_content = convert_md_videos_to_html(
            convert_md_images_to_html(
                formatted_content,
                Path(src),
                docs_path
            )
        )
        out_file = os.path.join(docs_path, "index.md")
        with open(out_file, 'w', encoding='utf-8') as out_f:
            out_f.write(converted_content)
            
def main():
    clean()
    format_index()
    format_content(projects_pathlist, "projects", docs_projects_dir)
    format_content(projects_undergraduate_pathlist, "projects", docs_undergraudate_dir)
    format_content(projects_masters_pathlist, "projects", docs_masters_dir)
    format_content(research_pathlist, "research", docs_research_dir)
    format_content(research_phd_pathlist, "research", docs_phd_dir)
    
if __name__ == "__main__":
    main()