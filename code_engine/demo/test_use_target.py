



def test_use_target():
    publish(folderpath, subscribe_name, data, output_folder)

    content = contents_of(output_path)

    assert_that(content).contains("def main(){}")
    
