//
//  NumberGame.swift
//  Algorithm_Syudy
//
//  Created by Minseop Kim on 2022/04/06.
//

import Foundation

class NumberGame {
    var aTeam : [Int]
    var bTeam : [Int]
    var answer = 0
    
    init(a : [Int], b : [Int]) {
        aTeam = a
        bTeam = b
    }
    
    func makeAnswer() {
        aTeam.sort(by: <)
        bTeam.sort(by: <)
        

        while aTeam.count > 0  && bTeam.count > 0{
            if Int(aTeam.last!) < Int(bTeam.last!) {
                answer += 1
                aTeam.popLast()
                bTeam.popLast()
            }else {
                aTeam.popLast()
            }
        }
    }
    
}


func solution(_ a:[Int], _ b:[Int]) -> Int {
    let ng = NumberGame(a: a, b: b)
    ng.makeAnswer()
    return ng.answer
}

