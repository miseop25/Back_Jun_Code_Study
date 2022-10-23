//
//  RightRect.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/03/21.
//

import Foundation
class RightRect
{
    var answer : Int64 = 0
    var weight : Int
    var height : Int
    
    init(w : Int, h : Int){
        weight = w
        height = h
    }
    
    func gcd(_ a: Int, _ b: Int) -> Int {
        if b == 0 {
            return a
        } else {
            return gcd(b, a%b)
        }
    }
    
    func getAnswer() -> Int64 {
        
        if weight == 1 || height == 1 {
            return 0
        }
        if weight == height {
            return Int64(weight * height - weight)
        }
        let gcdNum = gcd(weight, height)
        answer = Int64(weight * height - (weight + height - gcdNum))
        return answer
    }
}

func solution(_ w:Int, _ h:Int) -> Int64{
    var answer:Int64 = 0
    let s = RightRect(w: w, h: h)
    answer = s.getAnswer()
    
    
    return answer
}
