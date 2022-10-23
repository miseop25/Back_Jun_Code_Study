//
//  EntryJudge.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/03/28.
//

import Foundation

class EnteryJudge {
    var left = 1
    var right : Int
    var answer : Int64
    let person : Int
    let times : [Int]
    
    init(n : Int, t : [Int]) {
        person = n
        times = t
        right = Int(times.max()! * person)
        answer = 0
    }
    
    func binSerch() {
        while left <= right {
            let mid = Int((left + right)/2)
            var tempPerson = 0
            for t in times {
                tempPerson += Int(mid / t)
                if tempPerson >= person {
                    break
                }
            }
            
            if tempPerson >= person {
                answer = Int64(mid)
                right = mid - 1
            }else {
                left = mid + 1
            }
        }
    }
    
    func getAnswer() -> Int64 {
        binSerch()
        return answer
    }
    
}


func solution(_ n:Int, _ times:[Int]) -> Int64 {
    let EJ = EnteryJudge(n: n, t: times)
    return EJ.getAnswer()
}

