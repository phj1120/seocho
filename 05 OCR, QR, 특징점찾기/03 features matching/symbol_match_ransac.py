import os
import shutil
import cv2, numpy as np

# 사진에 로고가 포함되어 있는지 확인
def detect_logo(logo_path, img_path):
    img1 = cv2.imread(logo_path)
    img2 = cv2.imread(img_path)

    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    # ORB, BF-Hamming 로 knnMatch
    detector = cv2.ORB_create()
    kp1, desc1 = detector.detectAndCompute(gray1, None)
    kp2, desc2 = detector.detectAndCompute(gray2, None)
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(desc1, desc2)

    # 매칭 결과를 거리기준 오름차순으로 정렬
    matches = sorted(matches, key=lambda x:x.distance)
    # 모든 매칭점 그리기 ---④
    res1 = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, \
                        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

    # 매칭점으로 원근 변환 및 영역 표시
    src_pts = np.float32([ kp1[m.queryIdx].pt for m in matches ])
    dst_pts = np.float32([ kp2[m.trainIdx].pt for m in matches ])

    # RANSAC으로 변환 행렬 근사 계산, 숫자 조절해가며 성능 맞출것
    mtrx, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 20)
    h,w = img1.shape[:2]
    pts = np.float32([ [[0,0]],[[0,h-1]],[[w-1,h-1]],[[w-1,0]] ])
    dst = cv2.perspectiveTransform(pts,mtrx)
    img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

    # 정상치 매칭만 그리기
    matchesMask = mask.ravel().tolist()
    res2 = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, \
                        matchesMask = matchesMask,
                        flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

    # 모든 매칭점과 정상치 비율
    accuracy=float(mask.sum()) / mask.size
    print("accuracy: %d/%d(%.2f%%)"% (mask.sum(), mask.size, accuracy))

    # 결과 출력
    # cv2.imshow('Matching-All', res1)
    # cv2.imshow('Matching-Inlier ', res2)
    # cv2.waitKey()
    # cv2.destroyAllWindows()

    return mask.sum()


def move_img(logo_path):
    test_folder_path = f'img/test_img'
    count = 0
    imgs = os.listdir(test_folder_path)
    for img in imgs:
        img_path = f'img/test_img/{img}'
        detect_result = detect_logo(logo_path, img_path)
        if detect_result >= 32:
            count += 1
            logo_name = logo_path[4:-9]
            result_folder_path = f'img/result/{logo_name}'
            if not os.path.isdir(result_folder_path):
                os.makedirs(result_folder_path)
            shutil.copy(img_path, f'{result_folder_path}/{logo_name}_{count}{img[-4:]}')

starbucks_logo_path = 'img/starbucks_logo.jpg'
hollys_logo_path = 'img/hollys_logo.jpg'
back_logo_path = 'img/back_logo.jpg'

# 각 로고에 맞게 값을 찾바꿔가며 테스트 진행
move_img(starbucks_logo_path)
move_img(hollys_logo_path)
move_img(back_logo_path)