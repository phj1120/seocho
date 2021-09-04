import os
import shutil
import numpy as np

pwd = os.getcwd()

# train 디렉터리 생성
train_datasets_directory = os.path.join(pwd, "datasets/train")
if not os.path.exists(train_datasets_directory):
    os.makedirs(train_datasets_directory)

# test 디렉터리 생성
test_datasets_directory = os.path.join(pwd, "datasets/test")
if not os.path.exists(test_datasets_directory):
    os.makedirs(test_datasets_directory)


# 제일 적은 이미지 개수
member_name_path = 'filtering_images'
member_name_list = os.listdir(member_name_path)

print(member_name_list)
img_number = []
for i, name in enumerate(member_name_list):
    member_imgs_path = os.path.join(member_name_path, name)
    member_imgs_number = len(os.listdir(member_imgs_path))
    img_number.append(member_imgs_number)

min_img_number = img_number[np.argmin(img_number)]


for i, name in enumerate(member_name_list):
    # train 디렉터리 생성
    train_datasets_directory_name = os.path.join(train_datasets_directory, str(i))
    if not os.path.exists(train_datasets_directory_name):
        os.makedirs(train_datasets_directory_name)

    # test 디렉터리 생성
    test_datasets_directory_name = os.path.join(test_datasets_directory, str(i))
    if not os.path.exists(test_datasets_directory_name):
        os.makedirs(test_datasets_directory_name)
    
    count = 1
    file_list = os.listdir(os.path.join("filtering_images", name))
    for file in file_list:
        source_file = os.path.join("filtering_images", name, file)
        
        # 합습 데이터 셋 0.7 / 테스트 데이터 셋 0.3
        rate = 0.7
        if count < min_img_number * rate:
            shutil.copy(source_file, f"{train_datasets_directory_name}/{count}.jpg")
            print(f"[{name}] 학습 데이터셋 {count}개 저장완료")
        elif count <= min_img_number:
            shutil.copy(source_file, f"{test_datasets_directory_name}/{count-int(min_img_number*rate)}.jpg")
            print(f"[{name}] 테스트 데이터셋 {count-int(min_img_number*rate)}개 저장완료")
        else:
            break
        count += 1
        
    print(f"[{name}] 저장 완료")
