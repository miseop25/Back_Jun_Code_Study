//
//  back_joon_1110.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/04/14.
//

import Foundation


class PlusCycle {
    var N = 0
    var answer = 1
    
    func inputParm() {
        let input = readLine()!
        N = Int(input)!
    }
    
    func makeAnswer() {
        var new = N
        while true {
            let a = Int(new/10)
            let b = Int(new%10)
            let c = a + b
            new = (b*10) + Int(c%10)
            if new == N {
                break
            }else {
                answer += 1
            }
        }
    }
    
    func printAnswer() {
        print(answer)
    }
    
}
//
//let pc = PlusCycle()
//pc.inputParm()
//pc.makeAnswer()
//pc.printAnswer()
