import os

README_FILE = "README.md"
PROJECT_LIST_START = "<!-- PROJECT LIST START -->"
PROJECT_LIST_END = "<!-- PROJECT LIST END -->"

def get_projects():
    projects = []
    for item in os.listdir():
        if os.path.isdir(item) and item not in ['.git', '__pycache__', '.github']:
            if os.path.exists(os.path.join(item, 'README.md')):
                projects.append(item)
    return sorted(projects)

def update_readme(projects):
    with open(README_FILE, 'r') as file:
        content = file.read()

    before = content.split(PROJECT_LIST_START)[0]
    after = content.split(PROJECT_LIST_END)[1]

    project_list = "\n".join([f"- [{project}](./{project}/README.md)" for project in projects])
    new_content = f"{before}{PROJECT_LIST_START}\n{project_list}\n{PROJECT_LIST_END}{after}"

    with open(README_FILE, 'w') as file:
        file.write(new_content)

def main():
    projects = get_projects()
    update_readme(projects)
    print("README.md updated successfully!")

if __name__ == "__main__":
    main()