import cv2
pic = { 1:['fig1.png', 'fig1.png'],
        2:['4.jpg','5.jpg'],
        3:['aa1.jpg', 'aa2.jpg']}
src1  = cv2.imread('images/'+pic[3][0], cv2.IMREAD_COLOR)
#src1 = src1[:500,:600,:]
src2  = cv2.imread('images/'+pic[3][1], cv2.IMREAD_COLOR)
#src2 = src2[:500,:600,:]
dst = cv2.absdiff(src1, src2)

titles = ['src1', 'src2', 'dst']
for t in titles: cv2.imshow(t, eval(t))
cv2.waitKey()
cv2.destroyAllWindows()

