#lang racket

#|
Challenge link: https://www.hackerrank.com/challenges/lambda-march-compute-the-area-of-a-polygon

Calculates the area induced by a polygon with n points in the coordinates (x,y).
Constraints:
4 <= n <= 1000
0 <= x,y <= 1000
|#

(define test-count (car (map string->number (string-split (read-line)))))

(define distance2p
  (lambda (p1 p2)
    (expt (+ (expt (- (car p1) (car p2)) 2) 
                                                  (expt (- (cadr p1) (cadr p2)) 2)
                                                  )
                                         (/ 1 2)
          )
    )
  )
(define calcArea
  (lambda (n startingCod [prevCod startingCod] [a 0])
    (if (> n 0)
        (let ([cod (map string->number (string-split (read-line)))])
          (calcArea (- n 1) startingCod cod 
                        (+ a (* (+ (car prevCod) (car cod)) (- (cadr prevCod) (cadr cod))) 0.0))
          )
        (/ (+ a (* (+ (car prevCod) (car startingCod)) (- (cadr prevCod) (cadr startingCod)))) -2)
          )
    )
  )

(calcArea (- test-count 1) (map string->number (string-split (read-line))))