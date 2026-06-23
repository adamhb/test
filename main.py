from datetime import datetime


def main():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("output.txt", "w") as f:
        f.write(current_time)


if __name__ == "__main__":
    main()
