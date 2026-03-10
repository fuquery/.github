"""
Post sync hook for repo to configure the devcontainer.
"""

from pathlib import Path
import shutil

MANIFEST_PATH = "manifest"

def main(repo_topdir=None, **kwargs):
    """Main function invoked directly by repo.

    We must use the name "main" as that is what repo requires.

    Args:
      repo_topdir: The absolute path to the top-level directory of the repo workspace.
      kwargs: Leave this here for forward-compatibility.
    """
    repo = Path(repo_topdir)
    devcontainer_path = repo / ".devcontainer"
    devcontainer_path.mkdir(exist_ok=True)
    
    configuration = repo / MANIFEST_PATH / "devcontainer.json"
    if configuration.exists():
        shutil.copy(configuration, devcontainer_path / "devcontainer.json")
        print("Devcontainer configuration applied successfully.")
    else:
        print(f"Warning: No devcontainer.json found at {configuration}. Skipping devcontainer configuration.")

if __name__ == "__main__":
    main()