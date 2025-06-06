from subprocess import run
from pathlib import Path


def run_all(repo_path: Path):
    """
    Run all scripts in the specified repository path.
    """
    for fn in repo_path.glob("sdk/samples/*.py"):
        print(f"Running script: {fn}")
        print("-" * 40)
        run(["python", str(fn)], check=True)


if __name__ == "__main__":
    this_dir = Path(__file__).parent.resolve()
    run_all(this_dir)  # Adjust the path as necessary
    print("All scripts executed successfully.")
