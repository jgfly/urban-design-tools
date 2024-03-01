(defun c:DrawRectWithMouse ()
  (setq p1 (getpoint "\n选择第一个点: "))
  (setq p2 (getpoint p1 "\n选择第二个点以确定矩形的一条边: "))
  ;; 计算第一条边的方向向量和长度
  (setq dx (- (car p2) (car p1)))
  (setq dy (- (cadr p2) (cadr p1)))
  ;; 获取第三个点以确定矩形的宽度和方向
  (setq p3 (getpoint "\n移动鼠标确定矩形的宽度和方向: "))
  
  ;; 计算p1到p3的向量
  (setq dx1 (- (car p3) (car p1)))
  (setq dy1 (- (cadr p3) (cadr p1)))
  
  ;; 计算p1到p2的向量长度
  (setq len (sqrt (+ (* dx dx) (* dy dy))))
  
  ;; 计算第三点p3到p1p2线的垂直距离
  (setq width (abs (/ (- (* dx1 dy) (* dy1 dx)) len)))
  
  ;; 确定垂直方向向量
  (setq vx (/ dy len))
  (setq vy (- (/ dx len)))
  
  ;; 判断p3相对于p1p2的位置来决定宽度的方向
  (setq side (if (< (* dx1 dy) (* dy1 dx)) -1 1))
  
  ;; 计算矩形的其它两个点
  (setq p4 (list (+ (car p1) (* side vx width)) (+ (cadr p1) (* side vy width))))
  (setq p5 (list (+ (car p2) (* side vx width)) (+ (cadr p2) (* side vy width))))
  
  ;; 绘制矩形
  (command "._pline" p1 p2 p5 p4 "c")
  (princ)
)
