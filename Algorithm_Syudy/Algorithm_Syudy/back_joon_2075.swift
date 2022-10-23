//
//  back_joon_2075.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/05/16.
//

import Foundation


class BigestNumberN {
    let N :Int
    var answer = 0
    
    init(inputN : Int) {
        N = inputN
    }
    
    func getAnswer() -> Int{
        var arr : Array<Int> = []
        for cnt in 0..<N {
            var temp : Array<Int> = []
            if let word = readLine() {
                temp = word.components(separatedBy: " ").map({ (value) in Int(value)! })
                for i in temp {
                    arr.append(i)
                    if cnt != 0 {
                        arr.sort(by: >)
                        arr.popLast()
                    }
                    
                }
            }
        }
        
        answer = arr[N-1]
        return answer
    }
}


//let s = BigestNumberN(inputN: Int(readLine()!)!)
//print(s.getAnswer())
