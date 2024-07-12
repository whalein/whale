import exrex


def get_txt_contents(file_name="muben.txt"):
    with open(f"{file_name}", "r", encoding="utf-8") as f:
        dict_list = f.read().splitlines()
        return dict_list


def put_txt_contents(url, dict_list, filename="mulu"):
    with open(f"{filename}.txt", "w", encoding="utf-8") as f:
        for value in dict_list:
            mulu = list(exrex.generate(f"{url}/{value}"))
            f.write(mulu[0]+"\n")


if __name__ == '__main__':
    url = input("请输入url:")
    put_txt_contents(url, get_txt_contents())
