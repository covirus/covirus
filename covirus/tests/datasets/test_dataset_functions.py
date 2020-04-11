def test_list_dataset_files(wcota_dataset):
    wcota_dir = "/tmp/covirus/data/datasets/br/covid19br/"
    assert wcota_dir + "cases-brazil-cities.csv" in wcota_dataset.list_dataset_files()
