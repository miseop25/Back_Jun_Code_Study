//
//  DiskController.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/03/28.
//

import Foundation

class DiskController {
    var que : [[Int]] = []
    var time = 0
    var working:[Int] = []
    var ans_lists:[Int] = []
    var check = false
    var answer = 0
    
    init(jobs: [[Int]]) {
        for val in jobs {
            que.append(val)
        }
        que.sort { (a, b) -> Bool in
            return a[1] > b[1]
        }
    }
    
    func makeAnswer() {
        while que.count > 0 {
            que.sort { (a, b) -> Bool in
                return a[1] > b[1]
            }
            if working.count == 0 {
                for _ in 0...que.count {
                    let temp = que.popLast()
                    if temp![0] <= time {
                        ans_lists.append(time - temp![0] + temp![1])
                        working.append(temp![1])
                        check = true
                        break
                    }
                    else {
                        que.insert(temp!, at: 0)
                    }
                }
                
                if check {
                    que.sort { (a, b) -> Bool in
                        return a[1] > b[1]
                    }
                    check = false
                } else {
                    time += 1
                }
            }
            else {
                time += working.popLast()!
            }
                
        }
        var sum = 0
        for val in ans_lists {
            sum += val
        }
        answer = Int(  sum / ans_lists.count)
        
    }
    func getAnswer() -> Int {
        makeAnswer()
        return answer
    }
    
    
    
}


func solution(_ jobs:[[Int]]) -> Int {
    let dc = DiskController(jobs: jobs)
    
    return dc.getAnswer()
}
