import argparse

def main():
    parser = argparse.ArgumentParser(description="GitHub Summary CLI")
    parser.add_argument("-u", "--user", required=True, help="GitHub username")
    parser.add_argument("-p", "--project", required=True, help="GitHub project name")
    args = parser.parse_args()

    print(f"Generating summary for https://github.com/{args.user}/{args.project}")
    # здесь твоя логика
