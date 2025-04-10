import os
import re
import shutil
from pathlib import Path

undergraudate_dir = "../Undergraduate-Level"
masters_dir = "../Masters-Level"
phd_dir = "../PhD-Level"

undergraduate_pathlist = Path(undergraudate_dir).rglob('*.md')
masters_pathlist = Path(masters_dir).rglob('*.md')
phd_pathlist = Path(phd_dir).rglob('*.md')

docs_undergraudate_dir = "../docs/Undergraduate-Level"
docs_masters_dir = "../docs/Masters-Level"
docs_phd_dir = "../docs/PhD-Level"
docs_img_dir = "../docs/images"

contents_frontmatter = """---
layout: article
title: {title}
sidebar:
  nav: {level}
---
"""

tabs_frontmatter = """---
layout: article
title: Page - Sidebar
sidebar:
  nav: {level}
---

test
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
    clean_lst = [docs_undergraudate_dir, docs_masters_dir, docs_phd_dir, docs_img_dir]
    for dirpath in clean_lst:
        if os.path.exists(dirpath) and os.path.isdir(dirpath):
            shutil.rmtree(dirpath)
            os.makedirs(dirpath)
        else:
            os.makedirs(dirpath)

def convert_md_images_to_html(md_text: str, doc_path: Path, docs_dir: str) -> str:
    pattern = r'!\[[^\]]*\]\(([^)]+)\)'
    matches = re.findall(pattern, md_text)

    docs_dir_path = Path(docs_dir)

    for match in matches:
        source_path = (doc_path.parent / match).resolve()

        if match.startswith("../images"):
            target_folder = (docs_dir_path.parent / "images").resolve()
        else:
            target_folder = (docs_dir_path / "images").resolve()

        target_folder.mkdir(parents=True, exist_ok=True)
        
        if source_path.is_file():
            shutil.copy2(source_path, target_folder)
        else:
            print(f"Warning: {source_path} does not exist in {doc_path}!")

    replacement = r'<img class="image image--xl" src="\1"/>'
    return re.sub(pattern, replacement, md_text)

def convert_md_videos_to_html(md_text: str) -> str:
    pattern = re.compile(
        r"\[!\[Arm-CMU collaboration\]\(https://img\.youtube\.com/vi/zaRozkrcix0/0\.jpg\)\]\(https://www\.youtube\.com/watch\?v=zaRozkrcix0\)"
    )

    replacement = (
        '<iframe width="560" height="315" src="https://www.youtube.com/embed/zaRozkrcix0?si=hapHmGSGxZZOlqiQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'
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
    
    tab_file = os.path.join(docs_path, academic_level + ".md")
    tabs_content = tabs_frontmatter.format(level=academic_level)
    with open(tab_file, 'w', encoding='utf-8') as f:
        f.write(tabs_content)
        
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
    format_content(undergraduate_pathlist, "undergraduate", docs_undergraudate_dir)
    format_content(masters_pathlist, "masters", docs_masters_dir)
    format_content(phd_pathlist, "phd", docs_phd_dir)
    
if __name__ == "__main__":
    main()