#lang racket

#|
This code is used to solve the following hackerrank challenges:

1. https://www.hackerrank.com/challenges/eval-ex
For up to 50 test cases, print e^(x) where -20<=x<=20

2. https://www.hackerrank.com/challenges/area-under-curves-and-volume-of-revolving-a-curv
For an expression of the form a1*x**b1 + a2*x**b2 + a3*x**b3 + ... + an*x**bn
Where -1000 <= a <= 1000, -20 <= b <= 20:
Calculate the area under the curve of the funciton and volume revolving the curve in the domain 1 <= L < R <= 20
|#


#lang racket

#|
(define n (read))

(define args
  (lambda () 
    (let ([arg (read)])
       (if (eof-object? arg) 
           '()
           (cons arg (args))
           )
       )
    )
  )

(define l (args))
|#

(define coef (map string->number (string-split (read-line))))
(define pow (map string->number (string-split (read-line))))
(define limits (map string->number (string-split (read-line))))
(define a (car limits))
(define b (cadr limits))

(define printlist
  (lambda (l)
    (if (not (null? l))
        (begin
         (display (car l))
         (display "\n")
         (printlist (cdr l))
         )
        (void 1)
    )
  )
  )

; A custom made foldr
(define accumulateList
  (lambda (first action member)
    (lambda (l)
      (letrec ([accum
                (lambda (l r)
                  (if (null? l)
                      r
                      (accum (cdr l) (action (member l) r))
                      )
                  )]
               )
        (accum l first)
        )
      )
    )
  )

(define reverseList
  (accumulateList '() cons car)
  )

(define return1
    (lambda (x)
      1
      )
    )

(define lengthList
  (accumulateList 0 + return1)
  )

(define factorial
  (lambda (n [a 1])
    (if (> n 0)
        (factorial (- n 1) (* n a))
        a
        )
    )
  )

(define taylorTerm
  (lambda (x)
    (lambda (n)
      (/ (expt x n) (factorial n))
    )
    )
  )

; an inclusive version of python range
(define rangeInclusive
  (lambda (a b [interval 1] [l '()])
    (if (> a b)
        (reverse l)
        (rangeInclusive (+ a interval) b interval (cons a l))
        )
    )
  )

; python range implemented in racket
(define range
  (lambda (a b [interval 1] [l '()])
    (if (< a b)
        (range (+ a interval) b interval (cons a l))
        (reverse l)        
        )
    )
  )

(define naturalNumbers
  (lambda (n)
    (rangeInclusive 0 n)
    )
  )

; calculates e^x
(define ex
  (lambda (x)
    ((accumulateList 0 + (lambda (l)
                          ((taylorTerm x) (car l)))) (naturalNumbers 9))
    )
  )

; python zip implemented in racket
(define zip
  (lambda (l1 l2 [r '()])
    (if (null? l1)
        r
        (zip (cdr l1) (cdr l2)  (cons (cons (car l1) (car l2)) r))
        )
    )
  )

; makes a function out of the coefficients and powers provided
(define makeFunction
  (lambda (coef pow)
    (lambda (x)
      ((accumulateList 0 + (lambda (l)
                            (* (expt x (cdar l)) (caar l)))) (zip coef pow))
      )
    )
  )

; calculates the area under the curve of a function
(define area
  (lambda (f a b interval)
    ((accumulateList 0 + (lambda (l)
                           (* interval (f (car l))))) (rangeInclusive a b interval))
    )
  )

; calculates the volume of the revolving curve of a function
(define volume
  (lambda (f a b interval)
    ((accumulateList 0 + (lambda (l)
                           (* interval (* pi (expt (f (car l)) 2))))) (rangeInclusive a b interval))
    )
  )

(display (area (makeFunction coef pow) a b 0.001))
(display "\n")
(display (volume (makeFunction coef pow) a b 0.001))