def output(tags_list):
    with open("output.html", "w") as f:
        for tag in tags_list:
            f.write(str(tag))
            f.write('\n\n')
