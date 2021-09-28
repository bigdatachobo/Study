import cv2

src1  = cv2.imread('images/airplane.bmp', cv2.IMREAD_COLOR)
src2  = cv2.imread('images/field.bmp', cv2.IMREAD_COLOR)

dst1 = cv2.addWeighted(src1, 1, src2, 0, 0.0)
dst2 = cv2.addWeighted(src1, 0.75, src2, 0.25, 0.0)
dst3 = cv2.addWeighted(src1, 0.5, src2, 0.5, 0.0)
dst4 = cv2.addWeighted(src1, 0.25, src2, 0.75, 0.0)
dst5 = cv2.addWeighted(src1, 0, src2, 1, 0.0)

titles = ['dst1','dst2','dst3','dst4','dst5']
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey()
cv2.destroyAllWindows()

