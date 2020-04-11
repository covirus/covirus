def test_list_dataset_files(wcota_dataset):
    wcota_dir_unix = "/tmp/covirus/data/datasets/br/covid19br/"
    wcota_dir_win = "/tmp/covirus/data/datasets/br/covid19br\\"
    filename = "cases-brazil-cities.csv"
    win_path = wcota_dir_win + filename
    unix_path = wcota_dir_unix + filename

    files = wcota_dataset.list_dataset_files()
    assert win_path in files or unix_path in files
